def process_new_file_group(filegroup, columndatatype , sep , header):
    print(columndatatype)
    print(filegroup)
    # print(type(str(columndatatype)))
    print(sep)
    # print(type(sep))
    print(header)
    # print(type(str(header)))
    file_name_lookup = filegroup[0:filegroup.index('_')].lower()
    print(file_name_lookup)




