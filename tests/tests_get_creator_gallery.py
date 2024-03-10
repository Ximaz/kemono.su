import sys
import unittest
import unittest.mock

sys.path.append("..")

import kemono
import response_mocker


class TestGetGallery(unittest.TestCase):
    def test_page_parser(self):
        links = kemono.parse_gallery_page(page=response_mocker.mock_gallery_response("", {"o": 0}).text)
        self.assertTrue(50 == len(links))
        for link in links:
            self.assertEqual(link, f"https://kemono.su/{response_mocker.IMAGINARY_CREATOR['service']}/user/{response_mocker.IMAGINARY_CREATOR['id']}/post/post_id")

    def test_validate_page_value(self):
        self.assertListEqual(kemono.get_creator_gallery(response_mocker.IMAGINARY_CREATOR, 0), [])

    @unittest.mock.patch("requests.get")
    def test_get_creator_gallery(self, mock: unittest.mock.MagicMock):
        mock.side_effect = lambda url, **kwargs: response_mocker.mock_gallery_response(url, **kwargs)
        links = kemono.get_creator_gallery(response_mocker.IMAGINARY_CREATOR)
        self.assertTrue(50 == len(links))
        for link in links:
            self.assertTrue(link.startswith(f"https://kemono.su/{response_mocker.IMAGINARY_CREATOR['service']}/user/{response_mocker.IMAGINARY_CREATOR['id']}/post/"))

    @unittest.mock.patch("requests.get")
    def test_get_creator_entire_gallery(self, mock: unittest.mock.MagicMock):
        mock.side_effect = lambda url, **kwargs: response_mocker.mock_gallery_response(url, **kwargs)
        links = kemono.get_creator_entire_gallery(response_mocker.IMAGINARY_CREATOR)
        self.assertTrue(60 == len(links))
        for link in links:
            self.assertTrue(link.startswith(f"https://kemono.su/{response_mocker.IMAGINARY_CREATOR['service']}/user/{response_mocker.IMAGINARY_CREATOR['id']}/post/"))

if __name__ == "__main__":
    unittest.main()
