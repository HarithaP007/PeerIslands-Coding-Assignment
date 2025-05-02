from pyspark.sql.functions import col

def select_columns(df, params):
    return df.select(*params['columns'])

def with_column(df, params):
    return df.withColumn(params['name'], eval(params['expr']))

def drop_columns(df, params):
    return df.drop(*params['columns'])

def filter_rows(df, params):
    return df.filter(params['condition'])

def join_df(df, params):
    other_df = params['other_df']
    return df.join(other_df, on=params['on'], how=params['how'])

def groupby_agg(df, params):
    return df.groupBy(*params['group_by']).agg(*params['aggregations'])

def cache_df(df, params=None):
    return df.cache()

def repartition_df(df, params):
    return df.repartition(params['num_partitions'], *params['columns'])

TRANSFORMATIONS = {
    "select": select_columns,
    "withColumn": with_column,
    "drop": drop_columns,
    "filter": filter_rows,
    "join": join_df,
    "groupByAgg": groupby_agg,
    "cache": cache_df,
    "repartition": repartition_df,
}
