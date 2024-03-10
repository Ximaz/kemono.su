import json


IMAGINARY_CREATOR = {
    "id": "012345678",
    "name": "The Creator",
    "service": "service",
    "indexed": -1,
    "updated": -1,
    "favorited": -1
}

IMAGINARY_GALLERY_URL = f"https://kemono.su/{IMAGINARY_CREATOR['service']}/user/{IMAGINARY_CREATOR['id']}/post/VALID_GALLERY_ID"

GALLERY_ARTICLE = f"""
<article class="post-card post-card--preview" data-id="INVALID" data-service="INVALID" data-user="INVALID">
  <a href="/service/user/{IMAGINARY_CREATOR['id']}/post/post_id">
    <header class="post-card__header">LOREM IPSUM</header>
    <div class="post-card__image-container">
      <img class="post-card__image" src="//img.kemono.su/thumbnail/data/SOME/INVALID/IMAGE.jpg"/>
    </div>
    <footer class="post-card__footer">
      <time class="timestamp" datetime="INVALID TIME">INVALID TIME</time>
      <div>ATTACHMENTS NUMBER OR NONE</div>
    </footer>
  </a>
</article>
"""

POSTS_ARTICLE = """
<div class="post__thumbnail">
    <figure>
      <a
        class="fileThumb"
        href="https://c5.kemono.su/data/0e/0e/0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e.png?f=40.jpeg"
        download="filename.jpg"
      >
        <img
          data-src="https://img.kemono.su/thumbnail/data/0e/0e/0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e.png"
          src="https://img.kemono.su/thumbnail/data/0e/0e/0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e.png"
          loading="lazy"
        >
      </a>
    </figure>
  </div>
"""

class RequestMockResponse:
    def __init__(self, text: str):
        self.text = text


def mock_creators_response(url: str, params: dict = None):
    return RequestMockResponse(json.dumps([IMAGINARY_CREATOR]))

def mock_gallery_response(url: str, params: dict = None):
    if None is not params and params.get("o", 0) == 0:
        return RequestMockResponse(f"""
            <div class="card-list card-list--legacy">
            <div class="card-list__layout"></div>
            <div class="card-list__items">
                {GALLERY_ARTICLE * 50}
            </div>
            </div>""")
    return RequestMockResponse(f"""
        <div class="card-list card-list--legacy">
        <div class="card-list__layout"></div>
        <div class="card-list__items">
            {GALLERY_ARTICLE * 10}
        </div>
        </div>""")

def mock_posts_response(url: str, params: dict = None):
    return RequestMockResponse(f"<div class=\"post__files\">{POSTS_ARTICLE * 68}</div>")
