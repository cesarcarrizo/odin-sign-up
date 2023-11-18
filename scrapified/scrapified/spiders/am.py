import scrapy
from playwright.async_api import async_playwright

class AmSpider(scrapy.Spider):
    name = "am"
    allowed_domains = ["automercado.cr"]
    start_urls = ["https://automercado.cr"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    async def parse(self, response):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(response.url)

            title = await page.title()

            await browser.close()

            yield {
                'url': response.url, 'title': title
            }