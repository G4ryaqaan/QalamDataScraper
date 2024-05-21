import logging
import os
from dotenv import load_dotenv
from colorama import Fore, Style, init

init(autoreset=True)

class ColorFormatter(logging.Formatter):
    """Custom formatter to add color to logs."""
    def format(self, record):
        if record.levelno == logging.INFO:
            record.msg = Fore.GREEN + record.msg + Style.RESET_ALL
        elif record.levelno == logging.ERROR:
            record.msg = Fore.RED + record.msg + Style.RESET_ALL
        return super().format(record)

def setup_logging(level=logging.INFO):
    """Setup logging configuration with color."""
    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    formatter = ColorFormatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger

def load_env_variables():
    """Load environment variables from a .env file."""
    load_dotenv()
    env_vars = {
        'ISLAMQA_BASE_URL': os.getenv('ISLAMQA_BASE_URL')
    }
    return env_vars

def validate_url(url: str) -> bool:
    """Validate the structure of a URL."""
    from urllib.parse import urlparse

    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
