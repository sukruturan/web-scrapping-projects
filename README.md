# Collection of upcoming Web Scraping & Automation projects.
# Airbnb NYC Price / Review / Score Analysis

This project scrapes Airbnb listings, cleans the data, calculates a price-performance score and outputs a ranked list of the best stays.

### Features
- Automated data scraping (Selenium + BeautifulSoup)
- Data cleanup & normalization (Pandas)
- Price-per-night calculation
- Score formula → (rating * review_count) / price_per_night
- Final ranked & customer-ready output table

### Output Example

| Title | Location | Price/Night | Rating | Reviews | Score |
|-------|----------|-------------|--------|---------|-------|
| Midtown Cozy Room | Manhattan, NY | 3100 | 4.93 | 280 | 0.45 |

### Run
```bash
python airbnb_scrapper.py
python airbnb_scrapper_clean.py