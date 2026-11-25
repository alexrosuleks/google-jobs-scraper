"""Google Jobs Scraper with the Scrapely Python SDK (scrapely-client-python).

Install: pip install scrapely-client-python
Run:     SCRAPELY_TOKEN=your_token python example.py
"""
import json
import os

from scrapely_client import ScrapelyClient


def main() -> None:
    client = ScrapelyClient(os.environ['SCRAPELY_TOKEN'])

    run_input = {
        "query": "Software Engineer",
        "location": "San Francisco, CA",
        "maxResults": 10,
        "country": "us",
        "googleDomain": "google.com",
        "postedWithin": "any",
        "proxyConfiguration": {
            "useScrapelyProxy": True,
            "scrapelyProxyGroups": [
                "DATACENTER"
            ]
        }
    }

    # Start the scraper on Scrapely and wait for it to finish.
    run = client.actor('openrole/google-jobs-scraper').call(run_input=run_input)
    if run is None:
        raise RuntimeError('Run was not found')

    # Read the scraped results from the run's dataset.
    items = list(client.dataset(run.default_dataset_id).iterate_items())
    print(f'Scraped {len(items)} results')
    print(json.dumps(items, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
