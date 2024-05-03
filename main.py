
from movieRecommender.config.configuration import ConfigHandler
from movieRecommender.pipeline import DataValidationPipeline, FetchDataPipeline
from movieRecommender.logging import logger

config = ConfigHandler()

STAGE_NAME = "Fetch the data stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_acquisition = FetchDataPipeline(config)
   data_acquisition.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Validate Data stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationPipeline(config)
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
