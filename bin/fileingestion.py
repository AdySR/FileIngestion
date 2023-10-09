
def init_readfile(config_path):
    import configparser
    import glob
    import os

    config_reader = configparser.ConfigParser()
    config_reader.read(config_path)
    source_directory_path = config_reader['DEFAULT']['SourceDirectory']
    source_file_list=[]
    source_file_dict={}

    for file in glob.glob(source_directory_path+'\*.csv',recursive = True):
        source_file_list.append(os.path.basename(file))
        source_file_dict[os.path.basename(file)] = file
    
    for file in source_file_list:
        
        if(filegroup_exists_check(config_path,file)):
            print('##DEBUG## file found-', file, source_file_dict[file])
            load_existing_file_group(source_file_dict[file], file[0:file.index('_')].lower())
        else:
            print('##DEBUG## file Not found-', file, source_file_dict[file])
            columndatatype , sep , header = filemeta_collector(source_file_dict[file])
            if None not in (columndatatype , sep , header):
                process_new_file_group(config_path, file[0:file.index('_')].lower(), str(columndatatype) , sep , str(header))
                load_existing_file_group(source_file_dict[file], file[0:file.index('_')].lower())





def process_new_file_group(config_path, filegroup ,columndatatype , sep , header):
    import configparser
    update_config =configparser.ConfigParser()
    update_config.add_section(filegroup)

    update_config.set(filegroup,'delimiter',sep)
    update_config.set(filegroup,'column_list',header)
    update_config.set(filegroup,'column_metadata',columndatatype)

    with open(config_path,'a') as configfile:
        configfile.write('\n\n')
        update_config.write(configfile)
        configfile.close()

    refresh_config = configparser.ConfigParser()
    refresh_config.read(config_path)
    filegroup_list = refresh_config['DEFAULT']['FileGroupList']
    filegroup_list = filegroup_list.split(',')
    filegroup_list.append(filegroup)
    filegroup_list=str(filegroup_list)[1:-1]
    filegroup_list = filegroup_list.replace("'",'')

    refresh_config.set('DEFAULT','FileGroupList',str(filegroup_list))

    with open(config_path, 'w') as configfile:
        refresh_config.write(configfile)
        configfile.close()






def filegroup_exists_check(config_path, file_name):
    import configparser
    config_reader = configparser.ConfigParser()
    config_reader.read(config_path)
    filegroup_list = config_reader['DEFAULT']['FileGroupList']
    filegroup_list = filegroup_list.split(',')
    file_name_lookup = file_name[0:file_name.index('_')].lower()

    if any(file_name_lookup in listitem.lower() for listitem in filegroup_list):
        print('present - ',file_name_lookup)
        return True
    else:
        print('not present - ',file_name_lookup)
        return False






def filemeta_collector(full_file_path):
    import pandas as pd
    import csv

    with open(full_file_path) as fp:
        reader = csv.reader(fp)
        headers = next(reader)

    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(str(headers))
    detect_delimiter = dialect.delimiter
    generic_df = pd.read_csv(full_file_path, sep=detect_delimiter)
    column_datatype_dict = generic_df.dtypes.apply(lambda x: x.name).to_dict()
    return column_datatype_dict ,  detect_delimiter , headers





def load_existing_file_group(file_path, filegroup):
    print(file_path , '#####', filegroup)
    pass
