import unittest

from query import Query

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def testSearch(self):
        print("Testing Search Functionality")
        self.Query.phrase_query()
        self.assertEqual(self.Query.phrase_query, "roshan")

if __name__ == '__main__':
    unittest.main()
