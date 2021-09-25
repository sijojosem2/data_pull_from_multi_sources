import boto3
import config


boto3_session = boto3.Session(
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEYS,
)


API_KEY = config.API_KEY

""" 
    ------------------  Quick Referenece  ------------------

    Common Key Attributes:
    ---------------------------------------
    "dataset_name"  : << used to designate the dataset and name the csv make sure to use no spaces so that when writing csv the dataset can be identified >>
    "description"   : << a simple description of the dataset and/or its source>>
    
    
    Other Key Attributes:
    ---------------------------------------
    "write_to_csv"  : << Flag enables or disables csv creation from the pandas dataframe>> 
    "exec_sql"      : << Designates an SQL file to be executed in the pipeline sequence>> 
    "aws_s3_boto"   : << Created for handling S3 datasets, this uses boto3 for session and aws profile handling>> 
    "request"       : << url and headers to be provided here, any additional parameters, body also should be given >>
    "pd_dataframe"  : << pandas dataframe parameters, for JSON responses, provide the column that needs to be extracted in 'record_path' ;
                        for non JSON responses provide either the column delimiter (variable) or colspecs (fixed length) other parameters like delimiter,
                        column separators or column names are derived from the pandas documentation:
                        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html >>
    "target_table"  : <<target table parameters with reference to the pandas to_sql is given here>>
    

"""

input = {
    "desctiption": "etl_pipeline",
    "etl": [
        {
            "dataset_name": "pre_execution",
            "description": "file execution pre etl",
            "exec_sql": {"name": "pre_exec.sql"}
        },
        {
            "dataset_name": "variable_length_json_request_example",
            "description": "premier_league_teams competition data from public api with a JSON response",
            "request": {"url": "https://api.football-data.org/v2/competitions/PL/matches",
                        "headers": {"X-Auth-Token": API_KEY}, "params": {}},
            "pd_dataframe": {"norm": {"record_path": ["matches"], "sep": "_"}, "drop_cols": ["referees"]},
            "write_to_csv": True,
            "target_table": {"name": "request_json_retrieval_example", "if_exists": "append", "index": False}
        },
        # Since the S3 data set was too big for my local machine, i took only one parquet set as shown below
        {
            "dataset_name": "aws_large_s3_parquet_retreival_example",
            "description": "aws reviews from the publicly available s3 instance",
            "aws_s3_boto": {"path": "s3://amazon-reviews-pds/parquet/product_category=Digital_Music_Purchase", 'boto3_session': boto3_session},
            "write_to_csv": True,
            "target_table": {"name": "parquet_data_example", "if_exists": "append", "index": False}
        },
        {
            "dataset_name": "fixed_request_type_example",
            "description": "weather station information with fixed length csv data but not a JSON response",
            "request": {"url": "http://noaa-ghcn-pds.s3.amazonaws.com/ghcnd-stations.txt", "params": {}},
            "write_to_csv": True,
            "fixed_length": True,
            "pd_dataframe": {
                "params": {
                    "colspecs": [[0, 11], [12, 21], [22, 31], [32, 38], [39, 40], [41, 72], [73, 76], [77, 80],
                                 [81, 85]],
                    "names": ["id", "latitude", "longitude", "elevation", "state", "name", "gsn flag", "hcn_crn_flag",
                              "wmo_id"]
                },
                "drop_cols": []
            },
            "target_table": {"name": "fixed_width_data_example", "if_exists": "append", "index": False}
        },
        {
            "dataset_name": "variable_request_type_example",
            "description": "NYC grade scores obtained from 'https://catalog.data.gov/dataset?res_format=CSV' csv data but not a JSON response",
            "request": {"url": "https://data.cityofnewyork.us/api/views/825b-niea/rows.csv", "params": {}},
            "write_to_csv": True,
            "var_length": True,
            "pd_dataframe": {
                "params": {
                    "sep": ",", "header": "infer"},
                "drop_cols": []
            },
            "target_table": {"name": "variable_length_data_example", "if_exists": "append", "index": False}
        },
        {
            "dataset_name": "post_execution_sql_script_example",
            "description": "file execution post etl",
            "exec_sql": {"name": "post_exec.sql"}
        },

    ]
}
