from CNNclassifier import logger
from CNNclassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNclassifier.pipeline.stage_02_preparebasemodel import PrepareBaseModelTrainingPipeline

## This shows how the workflow of the project will happen
'''
1. Update config.yaml
2. Update secrets.yaml (if we want to hide something in Github then we have login/password)
3. Update params.yaml
4. Update entity
5. Update configuration manager in src config
6. Update components
7. Update pipeline
8. Update main.py
9. Update dvc.yaml

'''

from CNNclassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n X==============X")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Base model preparation Stage"

try:
    logger.info(f"**************")
    logger.info(f">>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    logger.error(e)
    raise e