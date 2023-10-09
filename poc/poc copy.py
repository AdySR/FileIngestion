import configparser

refresh_config = configparser.ConfigParser()
config_path = r'C:\programs\pyprojects\FileIngestion\config\config.ini'
filegroup_list =  'EMPLOYEE , USER'

refresh_config.read(config_path)
refresh_config.set('DEFAULT','FileGroupList',filegroup_list)

with open(config_path, 'w') as configfile:
    refresh_config.write(configfile)
    configfile.close()
