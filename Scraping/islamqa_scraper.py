from bs4 import BeautifulSoup
from .base_scraper import Scraping
import pandas as pd
from typing import Dict, Any
from utils.helpers import load_env_variables, setup_logging, validate_url

class IslamQAScraping(Scraping):
    def __init__(self):
        env_vars = load_env_variables()
        base_url = env_vars['ISLAMQA_BASE_URL']
        super().__init__(base_url)
        self.logger = setup_logging()

    def parse_page_content(self, content: str) -> Dict[str, Any]:
        """Parse the content of a web page and extract required information."""
        soup = BeautifulSoup(content, 'html.parser')

        title = soup.find(class_='title is-4 is-size-5-touch')
        title_text = title.text.strip() if title else ''

        qno = soup.find(class_='subtitle has-text-weight-bold has-title-case cursor-pointer tooltip')
        qno_text = int(qno.text.strip()) if qno else None

        ques = soup.find(class_='single_fatwa__question text-justified')
        ques_text = ques.text.replace('Question', '').strip() if ques else ''

        summary = soup.find(class_='single_fatwa__summary__body')
        summary_text = summary.text.strip() if summary else ''

        points = soup.find(class_='single_fatwa__answer__head layout-section')
        points_text = points.text.replace('Contents', '').replace('Related', '').replace('Answer', '').strip() if points else ''

        ans = soup.find(class_='content')
        ans_text = ans.text.strip() if ans else ''

        source = soup.find(class_='subtitle is-6 has-text-weight-bold is-capitalized')
        source_text = source.text.replace('Source:', '').strip() if source else ''

        return {
            'Qno': qno_text,
            'Title': title_text,
            'Ques': ques_text,
            'Summary': summary_text,
            'Points': points_text,
            'Ans': ans_text,
            'Source': source_text
        }

    def scrape_data(self, start: int, end: int) -> pd.DataFrame:
        """Scrape data from a range of pages and return a DataFrame."""
        data = []
        for i in range(start, end):
            url = f"{self.base_url}{i}"
            if not validate_url(url):
                self.logger.error(f"Invalid URL: {url}")
                continue

            content = self.fetch_page_content(url)
            if content:
                try:
                    page_data = self.parse_page_content(content)
                    page_data['URL'] = url
                    data.append(page_data)
                    self.logger.info(f"Data fetched successfully for URL: {url}")
                except Exception as e:
                    self.logger.error(f"Error processing URL {url}: {e}")
        df = pd.DataFrame(data, columns=['Qno', 'URL', 'Title', 'Ques', 'Summary', 'Points', 'Ans', 'Source'])
        return df
