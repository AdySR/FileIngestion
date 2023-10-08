def process_new_file_group(filegroup, columndatatype , sep , header):
    print(columndatatype)
    print(filegroup)
    # print(type(str(columndatatype)))
    print(sep)
    # print(type(sep))
    print(header)
    # print(type(str(header)))
    file_name_lookup = filegroup[0:filegroup.index('_')].lower()
    print(file_name_lookup)





def filegroup_exists_check(config_path, file_name):
    import configparser
    config_reader = configparser.ConfigParser()
    config_reader.read(config_path)
    filegroup_list = config_reader['DEFAULT']['FileGroupList']
    filegroup_list = filegroup_list.split(',')
    file_name_lookup = file_name[0:file_name.index('_')].lower()

    if any(file_name_lookup in listitem.lower() for listitem in filegroup_list):
        # print('present - ',file_name_lookup)
        return True
    else:
        # print('not present - ',file_name_lookup)
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
