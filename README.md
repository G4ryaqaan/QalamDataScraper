
# QalamDataScraper

**QalamDataScraper** is a Python-based tool designed to efficiently scrape and store data from various sources. It collects and organizes textual data, ensuring it's ready for further processing and analysis in AI applications.

## Features

- **Data Collection**: Scrapes a wide range of text data from specified URLs.
- **Storage**: Organizes and stores data in a structured format using Pandas.
- **Logging**: Provides detailed logging with color-coded messages.
- **Scalability**: Handles large volumes of data efficiently.

## Installation

### Setting Up a Virtual Environment

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Installing Dependencies Manually

If you don't have a `requirements.txt` file, you can install the dependencies manually:

```bash
pip install beautifulsoup4 abc pandas typing requests colorama logging python-dotenv
```

## Setting Up Environment Variables

1. **Create a `.env` file** in the root directory of your project.
2. **Add the following environment variables** to the `.env` file:
   ```env
   ISLAMQA_BASE_URL=https://example.com/base_url/
   ```

## Usage

### Example Code

Here's an example of how to use the scraper:

```python
from qalam_data_scraper.islamqa_scraping import IslamQAScraping

scraper = IslamQAScraping()
data = scraper.scrape_data(start=1, end=100)
data.to_csv('output.csv', index=False)
print('Data scraping completed successfully!')
```

### Detailed Class Descriptions

#### `IslamQAScraping`

A class that inherits from the `Scraping` base class, designed to scrape data from the IslamQA website.

- **Methods**:
  - `parse_page_content(content: str) -> Dict[str, Any]`: Parses the content of a web page and extracts required information.
  - `scrape_data(start: int, end: int) -> pd.DataFrame`: Scrapes data from a range of pages and returns a DataFrame.

#### `Scraping`

An abstract base class for web scraping.

- **Methods**:
  - `fetch_page_content(url: str) -> str`: Fetches the content of a web page.
  - `parse_page_content(content: str)`: Abstract method to parse the content of a web page.
  - `scrape_data(start: int, end: int)`: Abstract method to scrape data from a range of pages.

#### Utility Functions

- `setup_logging(level=logging.INFO)`: Sets up logging configuration with color.
- `load_env_variables()`: Loads environment variables from a `.env` file.
- `validate_url(url: str) -> bool`: Validates the structure of a URL.
- `combine_csv_files(folder_path: str, output_file_path: str)`: Combines multiple CSV files into a single CSV file.

## Running the Scraper

To run the scraper, execute the following command:

```bash
python -m qalam_data_scraper.islamqa_scraping
```

Ensure you have configured the environment variables correctly and installed all dependencies.