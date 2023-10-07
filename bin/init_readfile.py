import configparser
from filegroup_exists_check import filegroup_exists_check

def init_readfile(config_path):
    import configparser
    import glob
    import os

    config_reader = configparser.ConfigParser()
    config_reader.read(config_path)
    source_directory_path = config_reader['DEFAULT']['SourceDirectory']
    source_file_list=[]

    for file in glob.glob(source_directory_path+'\*.csv',recursive = True):
        source_file_list.append(os.path.basename(file))
        
    for file in source_file_list:
        filegroup_exists_check(config_path,file)








config_path = r'C:\programs\pyprojects\FileIngestion\config\config.ini'

init_readfile(config_path)