import configparser

read_config =configparser.ConfigParser()
update_config =configparser.ConfigParser()
refresh_config = configparser.ConfigParser()
config_path = r'C:\programs\pyprojects\FileIngestion\config\config.ini'
read_config.read(config_path)

dir_output = read_config['DEFAULT']['dir_output']
dir_source = read_config['DEFAULT']['dir_source']
archive = read_config['DEFAULT']['archive']


print(dir_output)
print(dir_source)
print(archive)

details_dict = dict(read_config.items('DEFAULT'))
list_sections = read_config.sections()
print(list_sections)

print(details_dict)

DEFAULT_SECTION = read_config['DEFAULT']

dir_output_path = DEFAULT_SECTION['dir_output']
print('\n',dir_output_path)

filegroup_list =  'EMPLOYEE , USER'



update_config.add_section('EMPLOYEE')
update_config.set('EMPLOYEE','delimiter',';')
update_config.set('EMPLOYEE','select_columns','empid, emp_name, emp_doj')
update_config.set('EMPLOYEE','column_metadata_dict','empid: int, emp_name: string(100), emp_doj: date')

update_config.add_section('USER')
update_config.set('USER','delimiter',';')
update_config.set('USER','select_columns','userid, user_name, user_doj')
update_config.set('USER','column_metadata_dict','userid: int, user_name: string(100), user_doj: date')

with open(config_path,'a') as configfile:
    configfile.write('\n\n')
    update_config.write(configfile)
    configfile.close()

