import configparser
config_path = r'C:\programs\pyprojects\FileIngestion\config\config.ini'
update_config =configparser.ConfigParser()
filegroup ='people'
update_config.add_section(filegroup)


with open(config_path,'a') as configfile:
    configfile.write('\n\n')
    update_config.write(configfile)
    configfile.close()

refresh_config = configparser.ConfigParser()
refresh_config.read(config_path)
filegroup_list = refresh_config['DEFAULT']['FileGroupList']
filegroup_list = filegroup_list.split(',')
filegroup_list.append(filegroup)
print(filegroup_list)

filegroup_list=str(filegroup_list)[1:-1]
filegroup_list = filegroup_list.replace("'",'')


refresh_config.set('DEFAULT','FileGroupList',str(filegroup_list))

with open(config_path, 'w') as configfile:
    refresh_config.write(configfile)
    configfile.close()

# refresh_config.set('DEFAULT','FileGroupList',filegroup_list)


print(filegroup_list)

