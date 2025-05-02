def show_df(df, params):
    df.show(params.get('n', 20), truncate=params.get('truncate', True))

def write_df(df, params):
    df.write.mode(params.get("mode", "overwrite")).format(params["format"]).save(params["path"])

def collect_df(df, params):
    return df.collect()

ACTIONS = {
    "show": show_df,
    "write": write_df,
    "collect": collect_df,
}
