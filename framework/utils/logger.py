import logging
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "automation.log"


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name) #creates/retreives a logger with a name
    #later we have to call : logger = get_logger(__name__)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )
    '''
                    Logger
                       │
                 Log message
                       │
              ┌────────┴────────┐
              ▼                 ▼
       Console Handler      File Handler
              │                 │
              ▼                 ▼
          Terminal       automation.log 
    '''
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger