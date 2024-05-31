from sensor.exception import SensorException
from sensor.logger import logging
import sys, os 
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.utils2 import dump_csv_file_to_mongodb_collection

if __name__ == "__main__":

    # file_path="aps_failure_training_set1.csv"
    # database_name="ineuron"
    # collection_name ="sensor"
    # dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
