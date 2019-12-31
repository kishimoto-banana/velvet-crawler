import scrapy


class Article(scrapy.Item):
    __table_name__ = 'articles'
    __uniq_fields__ = [
        'url',
    ]

    domain = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    main_text = scrapy.Field()
    published_at = scrapy.Field()
    hatena_bookmark_count = scrapy.Field()
