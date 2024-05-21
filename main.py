from Scraping.islamqa_scraper import IslamQAScraping
import os

def main(start_id, end_id):
    scraper = IslamQAScraping()
    data_df = scraper.scrape_data(start_id, end_id)

    output_dir = 'Output/IslamQA'
    os.makedirs(output_dir, exist_ok=True)

    output_file = f'{output_dir}/IslamQA-{start_id}-{end_id}.csv'
    data_df.to_csv(output_file, index=False)
    print(f"\nData scraped and saved to {output_file}")

if __name__ == "__main__":
    per_iteration = 100

    loop_iteration = 1000
    for i in range(500, loop_iteration):
        start_id = ((i-1) * per_iteration) + 1
        end_id = i * per_iteration
        main(start_id, end_id)
        print(str(f"{start_id} {end_id}"))