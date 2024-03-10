import os
import sys
import unittest

sys.path.append("..")

import kemono

COUNTER = 0

def update(fname: str):
    global COUNTER
    COUNTER += 1
    message = "updated " + str(COUNTER)
    file_handle = open(fname, "w+")
    file_handle.write(message)
    file_handle.close()
    return message

class TestCacheManager(unittest.TestCase):
    def test_implementation(self):
        fname = "tests_cache_manager.txt"
        delay = 1 / 3600 * 2
        message = kemono.read_from_cache(update=update, fname=fname, delay=delay)
        self.assertEqual(message, "updated 1")
        self.assertEqual(COUNTER, 1)
        message = kemono.read_from_cache(update=update, fname=fname, delay=delay)
        self.assertEqual(message, "updated 1")
        self.assertEqual(COUNTER, 1)
        message = kemono.read_from_cache(update=update, fname=fname, delay=0)
        self.assertEqual(message, "updated 2")
        self.assertEqual(COUNTER, 2)
        os.unlink(fname)

if __name__ == "__main__":
    unittest.main()
