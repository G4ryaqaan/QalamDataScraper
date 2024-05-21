import requests
from abc import ABC, abstractmethod
from colorama import Fore

class Scraping(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_page_content(self, url: str) -> str:
        """Fetch the content of a web page."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            print(Fore.RED + f"Error fetching URL {url}: {e}")
            return None

    @abstractmethod
    def parse_page_content(self, content: str):
        """Parse the content of a web page and extract required information."""
        pass

    @abstractmethod
    def scrape_data(self, start: int, end: int):
        """Scrape data from a range of pages and return structured data."""
        pass
