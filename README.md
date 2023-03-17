# HS_scraper
These piece of code is used to fetch contents for a Helsingin Sanomat (HS) -paper for a particular date. The result (see (example result)[https://www.hs.fi/api/editions/3831/toc]) is a well-organized json, including paper sections, article titles, urls and IDs. Note, that the articles themselves cannot be scraped with this code.

Feel free to use the code however you want.

## How does it work
A hidden API is used, which requires the paper's ID. The ID is found at the regular website of the paper. The paper contents are a bit difficult to scrape from the regular website, so the hidden API simplifies things. 

## About the paper ID
The paper ID is *almost* always systematically incremented daily. The correct IDs can be found at the regular website of the paper. This method is applied in the code.
