import os
import sys
import unittest
import unittest.mock

sys.path.append("..")

import kemono
import response_mocker

CREATORS_FILE = "creators.txt"

class TestSearchCreator(unittest.TestCase):
    @unittest.mock.patch("requests.get")
    def test_valid_account(self, mock: unittest.mock.MagicMock):
        mock.side_effect = lambda url, **kwargs: response_mocker.mock_creators_response(url, **kwargs)
        creator = kemono.get_creator(name=response_mocker.IMAGINARY_CREATOR["name"])
        self.assertTrue(isinstance(creator, (dict, type(None),)), "Return value should either be int or None")
        self.assertEqual(creator["id"], response_mocker.IMAGINARY_CREATOR["id"])

    @unittest.mock.patch("requests.get")
    def test_unknowned_account(self, mock: unittest.mock.MagicMock):
        mock.side_effect = lambda url, **kwargs: response_mocker.mock_creators_response(url, **kwargs)
        name = "this account definitely doesn't exist"
        creator = kemono.get_creator(name=name)
        self.assertTrue(isinstance(creator, (dict, type(None),)), "Return value should either be int or None")
        self.assertEqual(creator, None)

    @unittest.mock.patch("requests.get")
    def test_check_creators_file(self, mock: unittest.mock.MagicMock):
        mock.side_effect = lambda url, **kwargs: response_mocker.mock_creators_response(url, **kwargs)
        if os.path.exists(CREATORS_FILE):
            os.unlink(CREATORS_FILE)
        creators = kemono.get_creators()
        self.assertTrue(os.path.exists(CREATORS_FILE))
        os.unlink(CREATORS_FILE)
        expected_keys = { "id", "name", "service", "indexed", "updated", "favorited" }
        expected_value_types = (str, str, str, int, int, int,)
        error = "The kemono.su creators API might have change, some keys are not the same as expected by now."
        for e in creators:
            self.assertTrue(e.keys() == expected_keys, error)
            self.assertTupleEqual(tuple(map(lambda v: type(v), e.values())), expected_value_types, error)

if __name__ == "__main__":
    if os.path.exists(CREATORS_FILE):
        os.unlink(CREATORS_FILE)
    unittest.main()
    if os.path.exists(CREATORS_FILE):
        os.unlink(CREATORS_FILE)
