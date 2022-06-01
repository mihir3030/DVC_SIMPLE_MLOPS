from src.utils.all_utils import read_yaml, create_directory, save_local_df
import pandas as pd
import os
import argparse
from sklearn.linear_model import ElasticNet
import joblib



def split_and_save(config_path, params_path):
    config = read_yaml(config_path)  # read config from yaml file
    params = read_yaml(params_path)

    # getting path     
    artifact_dir = config['artifacts']['artifacts_dir']  
    split_data_dir = config['artifacts']['split_data_dir']

    train_data_filename = config['artifacts']['train']

    train_data_path = os.path.join(artifact_dir, split_data_dir, train_data_filename)
 

    # load csv file into dataframe
    train_data = pd.read_csv(train_data_path)

    train_x = train_data.drop('quality', axis=1)
    train_y = train_data['quality']
    
    alpha = params['model_params']['ElasticNet']['alpha']
    l1_ration = params['model_params']['ElasticNet']['l1_ratio']
    random_state = params['base']['random_state']
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ration, random_state=random_state)
    lr.fit(train_x, train_y)

    model_dir = config['artifacts']['model_dir']
    model_filename = config['artifacts']['model_file']

    model_dir = os.path.join(artifact_dir, model_dir)
    
    create_directory([model_dir])

    model_path = os.path.join(model_dir,model_filename)

    joblib.dump(lr, model_path)
    
 


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()
   
    split_and_save(config_path=parsed_args.config, params_path=parsed_args.params)