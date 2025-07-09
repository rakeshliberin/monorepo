import logging
import os
import sys
from datetime import datetime

# Create logs directory if it doesn't exist
log_dir = "logs"

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

class ColoredFormatter(logging.Formatter):
    """Custom formatter with colors for terminal output"""
    
    grey = "\x1b[38;21m"
    blue = "\x1b[38;5;39m"
    yellow = "\x1b[38;5;226m"
    red = "\x1b[38;5;196m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def get_logger(name: str = "voice_agent") -> logging.Logger:
    """
    Get a configured logger that can be used across all modules.

    Args:
        name: Name of the logger, defaults to "voice_agent"

    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Only configure the logger if it hasn't been configured already
    if not logger.handlers:
        # Create handlers
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # File handler - plain text
        file_handler = logging.FileHandler(f"{log_dir}/voice_agent_{current_time}.log")
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler - colored output
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)

        # Create formatters
        file_format = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_format = ColoredFormatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s'
        )

        # Set formatters
        file_handler.setFormatter(file_format)
        console_handler.setFormatter(console_format)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        # Prevent propagation to root logger
        logger.propagate = False

    return logger

# Create a default logger for import
logger = get_logger()
