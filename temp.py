import asyncio
import random
from pyppeteer import launch
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ScraperPayload:
    url: str
    job_list_selector: str
    title_selector: str
    description_selector: str
    location_selector: str
    link_selector: str


async def scrape_jobs(payload: ScraperPayload) -> List[Dict[str, str]]:
    """Scrapes jobs based on the given payload."""
    browser = None
    try:
        # Add random delay for rate limiting
        await asyncio.sleep(random.uniform(1, 3))

        browser = await launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
        )
        page = await browser.newPage()

        # Set longer default timeout
        page.setDefaultNavigationTimeout(90000)

        # Wait for network to be idle
        await page.goto(payload.url, {
            'waitUntil': 'networkidle0',
            'timeout': 90000
        })

        # Wait for the job listings container to load
        await page.waitForSelector(payload.job_list_selector)

        jobs = await page.evaluate('''(args) => {
            try {
                const {
                    job_list_selector, 
                    title_selector, 
                    description_selector, 
                    location_selector, 
                    link_selector
                } = args;

                const jobs = Array.from(document.querySelectorAll(job_list_selector))
                    .map(job => {
                        try {
                            return {
                                title: job.querySelector(title_selector)?.innerText?.trim() || '',
                                description: job.querySelector(description_selector)?.innerText?.trim() || '',
                                location: job.querySelector(location_selector)?.innerText?.trim() || '',
                                link: job.querySelector(link_selector)?.href || ''
                            };
                        } catch (err) {
                            console.error('Error processing job:', err);
                            return null;
                        }
                    })
                    .filter(job => job !== null);

                return jobs;
            } catch (err) {
                console.error('Error in evaluate:', err);
                return [];
            }
        }''', {
            "job_list_selector": payload.job_list_selector,
            "title_selector": payload.title_selector,
            "description_selector": payload.description_selector,
            "location_selector": payload.location_selector,
            "link_selector": payload.link_selector
        })

        return jobs
    except Exception as e:
        print(f"Error scraping {payload.url}: {str(e)}")
        return []
    finally:
        if browser:
            await browser.close()


async def worker(queue: List[ScraperPayload]):
    """Worker to process the scraping jobs."""
    while queue:
        payload = queue.pop(0)
        print(f"Processing: {payload.url}")
        try:
            jobs = await scrape_jobs(payload)
            print(f"Jobs scraped from {payload.url}:\n", jobs)
        except Exception as e:
            print(f"Failed to scrape {payload.url}: {e}")


async def main():
    queue = [
        ScraperPayload(
            url="https://jobs.careers.microsoft.com/global/en/search?l=en_us&pg=1&pgSz=20",
            job_list_selector=".ms-List-cell",
            title_selector="h2",
            description_selector="div[role='group'] div:nth-child(3)",
            location_selector="div[role='group'] div:nth-child(2)",
            link_selector="a"
        ),
    ]

    # Create tasks for concurrent execution
    tasks = [worker([payload]) for payload in queue]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())