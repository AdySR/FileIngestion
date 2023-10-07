import configparser
from bin.filegroup_exists_check import filegroup_exists_check


file_name= 'organizationss_1.csv'
config_path = r'C:\programs\pyprojects\FileIngestion\config\config.ini'

print(filegroup_exists_check(config_path,file_name))