import os
import sys
import unittest

sys.path.append("..")

import kemono

IMAGINARY_CREATOR = {
    "id": "creator_id",
    "name": "The Creator",
    "service": "service",
    "indexed": -1,
    "updated": -1,
    "favorited": -1
}
CREATOR = "Miyukitty"
CREATORS_FILE = "creators.txt"

HTML_PAGE = """
<div class="card-list card-list--legacy">
  <div class="card-list__layout"></div>
  <div class="card-list__items">
    <article
      class="post-card post-card--preview"
      data-id="INVALID"
      data-service="INVALID"
      data-user="INVALID"
    >
      <a href="/service/user/creator_id/post/post_id">
        <header class="post-card__header">LOREM IPSUM</header>
        <div class="post-card__image-container">
          <img
            class="post-card__image"
            src="//img.kemono.su/thumbnail/data/SOME/INVALID/IMAGE.jpg"
          />
        </div>
        <footer class="post-card__footer">
          <time class="timestamp" datetime="INVALID TIME">INVALID TIME</time>
          <div>ATTACHMENTS NUMBER OR NONE</div>
        </footer>
      </a>
    </article>
    <article
      class="post-card post-card--preview"
      data-id="INVALID"
      data-service="INVALID"
      data-user="INVALID"
    >
      <a href="/service/user/creator_id/post/post_id">
        <header class="post-card__header">LOREM IPSUM</header>
        <div class="post-card__image-container">
          <img
            class="post-card__image"
            src="//img.kemono.su/thumbnail/data/SOME/INVALID/IMAGE.jpg"
          />
        </div>
        <footer class="post-card__footer">
          <time class="timestamp" datetime="INVALID TIME">INVALID TIME</time>
          <div>ATTACHMENTS NUMBER OR NONE</div>
        </footer>
      </a>
    </article>
  </div>
</div>
"""

class TestGetGallery(unittest.TestCase):
    def test_page_parser(self):
        links = kemono.parse_page(page=HTML_PAGE)
        self.assertTrue(2 == len(links))
        for link in links:
            self.assertEqual(link, f"https://kemono.su/{IMAGINARY_CREATOR['service']}/user/{IMAGINARY_CREATOR['id']}/post/post_id")

    def test_validate_page_value(self):
        self.assertListEqual(kemono.get_creator_gallery(IMAGINARY_CREATOR, 0), [])

    def test_real_creator(self):
        creator = kemono.get_creator(name=CREATOR)
        links = kemono.get_creator_gallery(creator)
        error = f"The content of the creator {creator['name']} might have been deleted. Please, pick another reference"
        self.assertTrue(50 == len(links), error)
        for link in links:
            self.assertTrue(link.startswith(f"https://kemono.su/{creator['service']}/user/{creator['id']}/post/"), error)

    def test_real_creator_entire_gallery(self):
        creator = kemono.get_creator(name=CREATOR)
        links = kemono.get_creator_entire_gallery(creator)
        error = f"The content of the creator {creator['name']} might have been deleted. Please, pick another reference"
        self.assertTrue(176 <= len(links), error)
        for link in links:
            self.assertTrue(link.startswith(f"https://kemono.su/{creator['service']}/user/{creator['id']}/post/"), error)

if __name__ == "__main__":
    if os.path.exists(CREATORS_FILE):
        os.unlink(CREATORS_FILE)
    unittest.main()
    if os.path.exists(CREATORS_FILE):
        os.unlink(CREATORS_FILE)
