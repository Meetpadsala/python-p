import os
import logging

logging.basicConfig(
    filename="srcipt.log",
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
path = "test"

if os.path.exists(path):
    logging.info("folder found")
else:
    logging.error("folder not found")
    


