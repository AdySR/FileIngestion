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

    # print(columndatatype)
    # print(filegroup)
    # # print(type(str(columndatatype)))
    # print(sep)
    # # print(type(sep))
    # print(header)
    # # print(type(str(header)))
    # file_name_lookup = filegroup[0:filegroup.index('_')].lower()
    # print(file_name_lookup)




