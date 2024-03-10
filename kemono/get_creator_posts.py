import bs4
import requests


def parse_posts_page(page: str) -> list[str]:
    parser = bs4.BeautifulSoup(page, "html.parser")
    references = parser.select("div.post__files>div.post__thumbnail>figure>a.fileThumb")
    return [ref.get("href") for ref in references]


def get_creator_posts(gallery_url: str) -> list[str]:
    html = requests.get(gallery_url).text
    return parse_posts_page(html)


def get_creator_entire_posts(gallery_urls: list[str]) -> list[str]:
    total = []
    for gallery_url in gallery_urls:
        posts = get_creator_posts(gallery_url=gallery_url)
        total.extend(posts)
    return total
