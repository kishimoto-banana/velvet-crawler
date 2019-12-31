import re
from datetime import datetime
from urllib.parse import urlparse
from readability.readability import Document
import html2text

from dateutil import parser
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import Article

URL_FILE_PATH = "../urls.txt"


def normalize_url(url):
    return re.sub(r'\?.*', '', url)


class HatenaCrawlerSpider(CrawlSpider):
    name = 'hatena_crawler'
    allowed_domains = []
    start_urls = []
    rules = []

    custom_settings = {
        'DOWNLOAD_DELAY': 1,
    }

    def __init__(self, *args, **kwargs):
        with open(URL_FILE_PATH) as f:
            urls = [s.strip() for s in f.readlines()]
        start_urls = []
        allowed_urls = []
        rules = []
        domains = []
        for url in urls:
            domain = urlparse(url).netloc
            domains.append(domain)
            start_urls.append(url)
            allowed_urls.append(domain)
            rules.append(
                Rule(LinkExtractor(allow=rf'^http(s)?://{domain}/entry/.*',
                                   process_value=normalize_url),
                     callback=self.parse_page,
                     follow=True))
            self.domains = domains
            self.start_urls = start_urls
            self.allowed_domains = allowed_urls
            self.rules = rules
        super().__init__(*args, **kwargs)

    def parse_page(self, response):
        published_at = None
        published_at_timestamp = response.css(
            'meta[property="article:published_time"]::attr(content)'
        ).extract_first()
        if published_at_timestamp:
            try:
                # unixtime がセットされている場合
                published_at = datetime.fromtimestamp(
                    int(published_at_timestamp))
            except Exception:
                # タイムスタンプ文字列がセットされている場合
                published_at = parser.parse(published_at_timestamp)

        article = Document(response.text).summary()
        main_text = html2text.html2text(article)

        yield Article(
            domain=urlparse(response.url).netloc,
            url=response.url,
            title=response.css('title::text').extract_first(),
            # title=title,
            main_text=main_text,
            published_at=published_at,
        )
