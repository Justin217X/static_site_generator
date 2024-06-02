import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello world!",
            None,
            {"class": "greeting", "href": "http://example.com"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="http://example.com"'
        )


if __name__ == "__main__":
    unittest.main()
