# in this file we used functions that uses in diffrent python  files

import yaml
import os


def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content



def create_directory(dirs=list):  # we use list here because maybe we have to create multiple folder so we can pass list
    for dir_path in dirs:  # this loop iterate over all list and make directory 
        os.makedirs(dir_path, exist_ok = True)
        print(f"directory is create at {dir_path}") 


def save_local_df(data, data_path, index_status=False):
    data.to_csv(data_path, index=index_status)
    print(f"data is saved at {data_path}")