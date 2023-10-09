import configparser
import re

config_reader = configparser.ConfigParser()
config_path = r'C:\programs\pyprojects\FileIngestion\config\config.ini'

config_reader.read(config_path)
print(config_reader.sections())

filegroup_list = config_reader['DEFAULT']['FileGroupList']

filegroup_list = filegroup_list.split(',')
print(filegroup_list)

filename_path = config_reader['DEFAULT']['SourceDirectory']
print(filename_path)

file_name= 'organizations_1.csv'

print(file_name.index('_'))
file_name_lookup = file_name[0:file_name.index('_')].lower()
print(file_name_lookup)

if any(file_name_lookup in listitem.lower() for listitem in filegroup_list): 
    print('exists1')



# find = re.compile(r"^(.*?)\..*")

# read_config =configparser.ConfigParser()
# update_config =configparser.ConfigParser()
# refresh_config = configparser.ConfigParser()
# config_path = r'C:\programs\pyprojects\FileIngestion\config\config.ini'
# read_config.read(config_path)

# dir_output = read_config['DEFAULT']['dir_output']
# dir_source = read_config['DEFAULT']['dir_source']
# archive = read_config['DEFAULT']['archive']


# print(dir_output)
# print(dir_source)
# print(archive)
