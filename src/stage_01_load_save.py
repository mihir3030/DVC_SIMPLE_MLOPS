from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os

# this function save data to our local directory

def get_data(config_path):
    config = read_yaml(config_path) # read config file to download data and save data to local 
    
    remote_data_path = config['data_source']  # we have path of data
    df = pd.read_csv(remote_data_path, sep=";")  # load data into dataframe. and this data seperate by ;

    # now we have to save this data in local using our artifacts directory
    # create path to directory = "artifacts/raw_local_dir/data.csv"
    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']

    raw_local_file = config['artifacts']['raw_local_file']

    # we have got all informations. 
    # create path of directory
    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)

    create_directory(dirs = [raw_local_dir_path])

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    
    df.to_csv(raw_local_file_path, sep=",", index=False)





# this entry calling point for this file
# start exceution from here
if __name__ == '__main__':

    # command line agrument
    args = argparse.ArgumentParser() # calling method

    args.add_argument("--config", "-c", default="config/config.yaml")  # pass argument when program runs

    parsed_args =  args.parse_args()

    get_data(config_path = parsed_args.config) # calling uper function