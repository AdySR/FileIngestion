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

