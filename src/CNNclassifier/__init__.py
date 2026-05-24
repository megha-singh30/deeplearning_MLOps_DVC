import logging
import os, sys

log_dir = "logs"
format = "%(asctime)s - %(name)s - %(levelname)s - %(name)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s"

os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(level=logging.INFO, 
                    format=format, 
                    handlers=[
                        logging.FileHandler(os.path.join(log_dir, "app.log")),
                        logging.StreamHandler(sys.stdout)
            ])

logger = logging.getLogger("CNNclassifier_logger")