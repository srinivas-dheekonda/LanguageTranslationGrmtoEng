from LanguageTranslation.logging import logger
from LanguageTranslation.pipeline.Stage_01_data_ingestion import DataIngestionPipeline

stage_name = "Data Ingestion pipeline"

try:
    logger.info(f">>>>>>>>> started {stage_name} stage <<<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> completed {stage_name} stage <<<<<<<<<<<\n\nX================================X")
except Exception as e:
    raise e

