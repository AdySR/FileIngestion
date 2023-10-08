def process_new_file_group(config_path, filegroup):
    # , columndatatype , sep , header):
    import configparser
    update_config =configparser.ConfigParser()
    update_config.read(config_path)
    update_config.add_section(filegroup)
    # update_config.set('EMPLOYEE','delimiter',';')
    # update_config.set('EMPLOYEE','select_columns','empid, emp_name, emp_doj')
    # update_config.set('EMPLOYEE','column_metadata_dict','empid: int, emp_name: string(100), emp_doj: date')

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




