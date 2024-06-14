import unittest
from prefix import Trie  # Change PrefixTree to Trie

class PrefixTreeTest(unittest.TestCase):
    def test_insert(self):
        tree = Trie()  # Change PrefixTree to Trie
        tree.insert("apple")
        tree.insert("banana")
        tree.insert("cherry")
        self.assertTrue(tree.search("apple"))
        self.assertTrue(tree.search("banana"))
        self.assertTrue(tree.search("cherry"))
        self.assertFalse(tree.search("grape"))

    def test_search(self):
        tree = Trie()  # Change PrefixTree to Trie
        tree.insert("apple")
        tree.insert("banana")
        tree.insert("cherry")
        self.assertTrue(tree.search("apple"))
        self.assertTrue(tree.search("banana"))
        self.assertTrue(tree.search("cherry"))
        self.assertFalse(tree.search("grape"))

    def test_starts_with(self):
        tree = Trie()  # Change PrefixTree to Trie
        tree.insert("apple")
        tree.insert("banana")
        tree.insert("cherry")
        self.assertTrue(tree.starts_with("app"))
        self.assertTrue(tree.starts_with("ban"))
        self.assertTrue(tree.starts_with("che"))
        self.assertFalse(tree.starts_with("gra"))

if __name__ == '__main__':
    unittest.main()
