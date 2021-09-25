# Overview 

The project( Challenge Option Two ) consists of two parts: `run-data-pull` for extracting data from multiple sources and `run-db-query` for console querying the data. The data pull has been modelled in a ETL pipeline fashion, with the source data specifications and the data handling provided in the [pipeline](https://github.com/sijojosem2/data-engineer-code-challenge-sijo-completed/blob/main/pipeline.py) file. Once the data pull has been completed, the data can be interacted with using the `run-db-query` command

## Pre Run Setup - Project Variable Configuration 

The initial setup consists of deploying the python packages required for execution and the environment variable configuration. A working python 3.9 environment is suggested. 

The working assumptions for execution:

* A python 3.9 environment has already been setup  
* The main branch with the file/folder structure has already been deployed in the target running instance in the python environment.
* A working instance of PostgreSQL is accessible from the environment with DDL privileges.
* AWS credentials. *not entirely sure why, but the the specified public S3 bucket needs credentials from a valid AWS account*.
* The generated API key for the endpoints in the [pipeline](https://github.com/sijojosem2/data-engineer-code-challenge-sijo-completed/blob/main/pipeline.py) file is available.

Below are the files that should be setup before the initial setup run

### -------  env file -------

The [scripts]https://github.com/sijojosem2/data-engineer-code-challenge-sijo-completed/tree/main/scripts file exports the necessary environmental variables used for the project execution

`FOOTBALL_API_KEY` is an example key that I had obtained from [football stats](https://www.football-data.org/) to fetch football data (I know this is not part of the challenge, but I was tinkering with some ideas). Down the line if a new data source is added and keys are to be exported, it should be placed here. Any secure key or credentials *must be added to this file* since the subsequent configurations and script run depend on these parameters. Ideally to maintain key confidentiality when deploying between instances this file should be added to `--- gitignore ---` to avoid overwrite, but I have added this as part of the initial configuration.

The `DATABASE_URI` is a mandatory string connection parameter that should be supplied. I chose Postgres because of its psycopg2 package versatility which can cursor write huge chunks of data in a relatively short amount of time. The tradeoff is the memory usage which is a bit on the higher side for this kind of operation. Since I chose a generic approach with a process that can handle request JSON responses, S3 pulls and request CSV responses, I finalised on pandas psycopg2 alongside cursor write operation.

`AWS_ACCESS_KEY_ID` and the `AWS_SECRET_ACCESS_KEYS` had to be supplied to access the [dataset of Amazon product reviews](https://s3.amazonaws.com/amazon-reviews-pds/readme.html). I am not sure why a public S3 bucket needs one's private keys, but hey, I dont make the rules! Since I keep getting 403:Forbidden errors while trying without the keys, I gave this a go and voila this works.


```shell
export FOOTBALL_API_KEY=apikey123
export DATABASE_URI=postgresql://pg_host/pg_database?user=pg_user&password=pg_password
export AWS_ACCESS_KEY_ID=awskey123
export AWS_SECRET_ACCESS_KEYS=awssecretkey123

```

### -------  config.py -------

This `---folder--` file get the environmental variables from the above and into the python environment. 

Ensure that the `env file`  are available here. Apart from then the directories are pretty straight forward in specifying where you would like to save log, csv or SQL execution files(used in ETL [pipeline](https://github.com/sijojosem2/data-engineer-code-challenge-sijo-completed/blob/main/pipeline.py) file). Keep in mind that the paths are relative to the execution script

```python

LOG_DIR      = 'logs/'
SQL_DIR      = 'sql/'
CSV_DIR      = 'csv/'

```

### -------  pipeline.py   *OPTIONAL*  -------

The [pipeline](https://github.com/sijojosem2/data-engineer-code-challenge-sijo-completed/blob/main/pipeline.py) file has the following quick reference guide:


```python
"""
    ------------------  Quick Reference  ------------------

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
    "pd_dataframe"  : << pandas data frame parameters, for JSON responses, provide the column that needs to be extracted in 'record_path' ;
                        for non JSON responses provide either the column delimiter (variable) or colspecs (fixed length) other parameters like delimiter,
                        column separators or column names are derived from the pandas documentation:
                        https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html >>
    "target_table"  : <<target table parameters with reference to the pandas to_sql is given here>>
"""
```


Any additional SQLs can also be added in between the pipeline in the 'etl' list, apart from the already configured pre/post execution SQL, as such:


```python 
        
        {
            "dataset_name": "pre_execution",
            "description": "file execution pre etl",
            "exec_sql": {"name": "pre_exec.sql"}
        },

```
However please ensure that the sql file is available in the `sql folder`. The pipeline *will not fail if sql file is unavailable* and the error will be handled in logs, but if there is a dependency on the missing SQL the pipeline may halt execution


## Pre Run Setup - Package Deployment

Once all the keys and environment is setup, from the folder where `Makefile` is available run the following:

`make install-packages`

This will ensure that all the necessary packages for the execution is installed. The packages are picked up from the `requirements.txt`. I have kept this the latest versions as of now. Should any updated package is required, set the version in the `requirements.txt` and run `make install-packages` again.

Once the packages are deployed, the project is now ready to run 

## Data Pull

From the folder where `Makefile` is available run the following:

`make run-data-pull`

This will fetch data from the sources provided in the [pipeline](https://github.com/sijojosem2/data-engineer-code-challenge-sijo-completed/blob/main/pipeline.py) file and the logs/csv will be written to the locations specified in `config.py`

## Query Data

If all goes well with the Data pull, the query data utility can be run using :

`make run-query`

Running through the options, an SQL query can be supplied to retrieve the data that has been pulled. The limitation here is that if there are numerous columns in the data set, the query will return an irregular set. Ideally the query can be used for retrieving the columns as lengthy as the size of the console




