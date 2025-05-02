import json
import logging
from pyspark.sql import SparkSession
from transformations import TRANSFORMATIONS
from actions import ACTIONS
from utils import transform_df

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(path="config.json"):
    with open(path) as f:
        return json.load(f)

def apply_transformations(df, config):
    for step in config.get("transformations", []):
        op = step["operation"]
        params = step.get("params", {})
        logger.info(f"Applying transformation: {op} with params: {params}")
        if op in TRANSFORMATIONS:
            df = TRANSFORMATIONS[op](df, params)
        elif op == "custom":
            df = transform_df(df, params["logic_name"])
        else:
            raise ValueError(f"Unknown transformation operation: {op}")
    return df

def apply_actions(df, config):
    for step in config.get("actions", []):
        op = step["operation"]
        params = step.get("params", {})
        logger.info(f"Performing action: {op} with params: {params}")
        if op in ACTIONS:
            ACTIONS[op](df, params)
        else:
            raise ValueError(f"Unknown action operation: {op}")

def main():
    spark = SparkSession.builder.appName("DynamicTransformationFramework").getOrCreate()

    data = [(1, "Haritha", 29), (2, "Renuka", 22), (3, "Indu", 33)]
    df = spark.createDataFrame(data, ["id", "name", "age"])

    config = load_config()
    df = apply_transformations(df, config)
    apply_actions(df, config)

    spark.stop()

if __name__ == "__main__":
    main()
