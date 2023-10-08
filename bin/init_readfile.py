import configparser
from filegroup_exists_check import filegroup_exists_check
from filemeta_collector import filemeta_collector

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
        else:
            print('##DEBUG## file Not found-', file, source_file_dict[file])
            columndatatype , sep , header = filemeta_collector(source_file_dict[file])
    
    print(columndatatype)
    print(type(str(columndatatype)))
    print(sep)
    print(type(sep))
    print(header)
    print(type(str(header)))



config_path = r'C:\programs\pyprojects\FileIngestion\config\config.ini'

init_readfile(config_path)
