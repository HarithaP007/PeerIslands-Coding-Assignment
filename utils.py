from pyspark.sql.functions import upper, col

def transform_df(df, logic_name: str):
    if logic_name == "custom_capitalize":
        return df.withColumn("name", upper(col("name")))
    else:
        raise ValueError(f"Unknown custom logic: {logic_name}")
