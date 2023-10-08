def filemeta_collector(full_file_path):
    import pandas as pd
    import csv

    with open(full_file_path) as fp:
        reader = csv.reader(fp)
        headers = next(reader)

    
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(str(headers))
    detect_delimiter = dialect.delimiter
    generic_df = pd.read_csv(full_file_path, sep=detect_delimiter)
    column_datatype_dict = generic_df.dtypes.apply(lambda x: x.name).to_dict()
    return column_datatype_dict ,  detect_delimiter , headers






# full_file_path =r'C:\programs\pyprojects\FileIngestion\dir_source\organizations_1.csv'
# columndatatype , sep , header = filemeta_collector(full_file_path)

# print(columndatatype)
# print(type(str(columndatatype)))
# print(sep)
# print(type(sep))
# print(header)
# print(type(str(header)))

