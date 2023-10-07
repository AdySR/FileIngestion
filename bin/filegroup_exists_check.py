def filegroup_exists_check(config_path, file_name):
    import configparser
    config_reader = configparser.ConfigParser()
    config_reader.read(config_path)
    filegroup_list = config_reader['DEFAULT']['FileGroupList']
    filegroup_list = filegroup_list.split(',')
    file_name_lookup = file_name[0:file_name.index('_')].lower()

    if any(file_name_lookup in listitem.lower() for listitem in filegroup_list):
        print('present - ',file_name_lookup)
        return True
    else:
        print('not present - ',file_name_lookup)
        return False



# file_name= 'organizations_1.csv'
# config_path = r'C:\programs\pyprojects\FileIngestion\config\config.ini'
# print(filegroup_exists_check(config_path,file_name))