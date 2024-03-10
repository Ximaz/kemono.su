import re
import sys
import unittest
import unittest.mock

sys.path.append("..")

import kemono
import response_mocker

IMAGE_REGEX = re.compile(r"^https:\/\/.*\.kemono\.su\/data\/.+\/.+\/[a-f0-9]{64}\.(?:png|jpg|jpeg)\?f=.+$")

class TestGetPosts(unittest.TestCase):
    def test_page_parser(self):
        posts = kemono.parse_posts_page(page=response_mocker.mock_posts_response("", {"o": 0}).text)
        self.assertTrue(68 == len(posts))
        for post in posts:
            self.assertNotEqual(IMAGE_REGEX.match(post), None)

    @unittest.mock.patch("requests.get")
    def test_get_creator_posts(self, mock: unittest.mock.MagicMock):
        mock.side_effect = lambda url, **kwargs: response_mocker.mock_posts_response(url, **kwargs)
        posts = kemono.get_creator_posts(response_mocker.IMAGINARY_GALLERY_URL)
        self.assertTrue(68 == len(posts))
        for post in posts:
            self.assertNotEqual(IMAGE_REGEX.match(post), None)

    @unittest.mock.patch("requests.get")
    def test_get_creator_entire_posts(self, mock: unittest.mock.MagicMock):
        mock.side_effect = lambda url, **kwargs: response_mocker.mock_posts_response(url, **kwargs)
        posts = kemono.get_creator_entire_posts([response_mocker.IMAGINARY_GALLERY_URL])
        self.assertTrue(68 == len(posts))
        for post in posts:
            self.assertNotEqual(IMAGE_REGEX.match(post), None)

if __name__ == "__main__":
    unittest.main()
