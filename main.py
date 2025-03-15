import os
from pathlib import Path

# Correct directory path
project_root = Path(r"C:\Users\ayshr\OneDrive\Desktop\Replit\Text-Summarizer")

# Change to project root
os.chdir(project_root)

from textSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

# STAGE_NAME = "Data Ingestion stage"
# try:
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#    data_ingestion = DataIngestionTrainingPipeline()
#    data_ingestion.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e


# STAGE_NAME = "Data Validation stage"
STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

