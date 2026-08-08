
from framework.config.settings import settings
from framework.utils.logger import get_logger

logger = get_logger(__name__)

def test_launch_chrome(page):#page is dependent on context and context on browser
    # So browser-> context-> Page
    
    logger.info(f"Navigating to the Homepage: {settings.base_url}")
    page.goto(settings.base_url)


