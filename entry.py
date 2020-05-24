from utils.data_extractor import BigQueryDataExtractor
import timeit
from config.conf import logger


def run():

    """ Wrapper function that runs the scripts and returns tables in csv format in the outputs directory. """

    start = timeit.default_timer()

    bq_runner = BigQueryDataExtractor(project="ace-digit-277918")
    bq_runner.wrapper_query_to_df(dataset="world_bank_wdi")

    end = timeit.default_timer()

    logger.info(f"Program taken: {(end-start)/60} to execute")

if __name__=='__main__':
    run()
