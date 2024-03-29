import scrapy
from scrapy.linkextractors import LinkExtractor


class UfcEventsSpider(scrapy.Spider):
    name = "ufc_events"
    allowed_domains = ["ufcstats.com"]
    start_urls = ["http://ufcstats.com/statistics/events/completed?page=all"]

    def parse(self, response):
       events_links = response.xpath("//i//a/@href")
    #    events_links = [link.url for link in LinkExtractor().extract_links(response)]
       yield from response.follow_all(events_links, self.parse_event)

    #    pagination_links = response.xpath('(//ul[@class="b-statistics__paginate"]//li//a)[2]')
    #    yield from response.follow_all(pagination_links, self.parse)

    def parse_event(self, response):
        def extract_with_xpath(expression):
            return response.xpath(expression).get(default="").strip()

        # Very susceptible to website changes. Not stable.
        yield {
            "event_name": extract_with_xpath("//div//h2//span/text()"),
            "event_date": extract_with_xpath("(//li[contains(@class, 'b-list__box-list-item')]/text())[2]"),
            "event_location": extract_with_xpath("(//li[contains(@class, 'b-list__box-list-item')]/text())[4]"),
        }