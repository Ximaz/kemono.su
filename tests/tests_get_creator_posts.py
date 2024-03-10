import os
import re
import sys
import unittest

sys.path.append("..")

import kemono

CREATOR = "Miyukitty"
CREATORS_FILE = "creators.txt"

HTML_PAGE = """
<div class="post__files">
  <div class="post__thumbnail">
    <figure>
      <a
        class="fileThumb"
        href="IMAGE_URL_HERE"
        download="filename.jpg"
      >
        <img
          data-src="IMAGE_THUMBNAIL_URL_HERE"
          src="IMAGE_THUMBNAIL_URL_HERE"
          loading="lazy"
        >
      </a>
    </figure>
  </div>
  <div class="post__thumbnail">
    <figure>
      <a
        class="fileThumb"
        href="IMAGE_URL_HERE"
        download="filename.jpeg"
      >
        <img
          data-src="IMAGE_THUMBNAIL_URL_HERE"
          src="IMAGE_THUMBNAIL_URL_HERE"
          loading="lazy"
        />
      </a>
    </figure>
  </div>
</div>
"""

IMAGE_REGEX = re.compile(r"^https:\/\/.*\.kemono\.su\/data\/.+\/.+\/[a-f0-9]{64}\.(?:png|jpg|jpeg)\?f=.+$")

class TestGetGallery(unittest.TestCase):
    def test_page_parser(self):
        links = kemono.parse_posts_page(page=HTML_PAGE)
        self.assertTrue(2 == len(links))
        for link in links:
            self.assertEqual(link, f"IMAGE_URL_HERE")

    def test_real_creator(self):
        creator = kemono.get_creator(name=CREATOR)
        links = kemono.get_creator_gallery(creator)
        error = f"The content of the creator {creator['name']} might have been deleted. Please, pick another reference"
        self.assertTrue(1 <= len(links), error)
        link = links[0]
        posts = kemono.get_creator_posts(link)
        self.assertTrue(1 <= len(posts), error)

    def test_real_creator_entire_posts(self):
        creator = kemono.get_creator(name=CREATOR)
        page = 1
        gallery = kemono.get_creator_gallery(creator=creator, page=page)
        while len(gallery) > 0:
          for g in gallery:
            posts = kemono.get_creator_entire_posts([g])
            for post in posts:
              self.assertNotEqual(IMAGE_REGEX.match(post), None, f"The URL format doesn't match the regex, it might have change. (see at {gallery}) (posts: {posts})")
          page += 1
          gallery = kemono.get_creator_gallery(creator=creator, page=page)

if __name__ == "__main__":
    if os.path.exists(CREATORS_FILE):
        os.unlink(CREATORS_FILE)
    unittest.main()
    if os.path.exists(CREATORS_FILE):
        os.unlink(CREATORS_FILE)
