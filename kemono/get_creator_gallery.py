import bs4
import requests


PAGE_SIZE = 50


def parse_gallery_page(page: str) -> list[str]:
    parser = bs4.BeautifulSoup(page, "html.parser")
    references = parser.select("div.card-list.card-list--legacy>div.card-list__items>article.post-card>a")
    return ["https://kemono.su" + ref.get("href") for ref in references]


def get_creator_gallery(creator: dict, page: int = 1) -> list[str]:
    if 1 > page:
        return []
    cursor = (page - 1) * PAGE_SIZE
    html = requests.get(f"https://kemono.su/{creator['service']}/user/{creator['id']}", params={"o": cursor}).text
    return parse_gallery_page(html)


def get_creator_entire_gallery(creator: dict) -> list[str]:
    page = 1
    total = []
    gallery = get_creator_gallery(creator=creator, page=page)
    while len(gallery) > 0:
        total.extend(gallery)
        page += 1
        gallery = get_creator_gallery(creator=creator, page=page)
    return total
