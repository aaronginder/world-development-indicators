from google.cloud import bigquery
import pandas as pd
from config.conf import logger

class BigQueryDataExtractor:

    def __init__(self, project: str):
        self.project = project
        self.client = bigquery.Client(self.project)
        self.public_client = bigquery.Client("bigquery-public-data")

    def get_table_list(self, dataset: bigquery.DatasetReference) -> list:

        """ Function that takes a dataset and returns a list of the tables within that dataset.

        :type dataset: bigquery.DatasetReference
        :param dataset: the dataset reference object that you want to return a list of tables

        :rtype: list """

        tables_list = self.public_client.list_tables(dataset=dataset)
        logger.info(f"Retrieved tables in {dataset}")

        return list(tables_list)

    def bq_query_to_dataframe(self, sql: str) -> pd.core.frame.DataFrame:

        """ Function that takes a SQL (Structured Query Language) str input which is executed and returns a pandas Dataframe object

        :type sql: str
        :param sql: the SQL code that is to be executed on a table

        :raises: Exception if syntax error

        :rtype: pd.Dataframe """

        try:
            df = self.client.query(sql).to_dataframe()

        except Exception as e:
            logger.error(f"Cannot execute query to a dataframe due to: {e}")

        return df

    def wrapper_query_to_df(self, dataset: bigquery.DatasetReference) -> None:

        """ Wrapper function that takes as dataset input and loops through the tables within the dataset and coverts the BigQuery table to a dataframe and exports as a CSV.

        :type dataset: bigquery.DatasetReference
        :param dataset: the dataset reference object

        :rtype: None """

        table_names = self.get_table_list(dataset=dataset)

        for table in table_names:
            sql = f"""SELECT * FROM `{table.project}.{table.dataset_id}.{table.table_id}`"""

            logger.info(f"Starting to collect data for {table.table_id}")
            response = self.bq_query_to_dataframe(sql)
            logger.info(f"Collected data for {table.table_id}")

            output = f"output/{table.table_id}.csv"
            response.to_csv(path_or_buf=output, index=True)
            logger.info(f"Exported data to {output}")
