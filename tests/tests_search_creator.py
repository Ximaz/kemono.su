import os
import sys
import unittest

sys.path.append("..")

import kemono

CREATORS_FILE = "creators.txt"

class TestSearchCreator(unittest.TestCase):
    def test_valid_account(self):
        name = "Miyukitty"
        creator = kemono.get_creator(name=name)
        self.assertTrue(isinstance(creator, (dict, type(None),)), "Return value should either be int or None")
        self.assertEqual(creator["id"], "70394974", f"It seems that the account of {name} has been deleted. Please, take another account as a reference")

    def test_unknowned_account(self):
        name = "this account definitely doesn't exist"
        creator = kemono.get_creator(name=name)
        self.assertTrue(isinstance(creator, (dict, type(None),)), "Return value should either be int or None")
        self.assertEqual(creator, None, f"Somehow the unknowned account reference actually exists now, please change to another odd thing")

    def test_check_creators_file(self):
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
    unittest.main()
