import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode(
            "This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://example.com/image1.png) and ![another](https://example.com/image2.png)"
        expected_output = [("image", "https://example.com/image1.png"),
                           ("another", "https://example.com/image2.png")]
        assert extract_markdown_images(text) == expected_output

        text = "No images here!"
        expected_output = []
        assert extract_markdown_images(text) == expected_output

        text = "Single image ![single](https://example.com/single.png)"
        expected_output = [("single", "https://example.com/single.png")]
        assert extract_markdown_images(text) == expected_output

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://example.com/page) and [another](https://example.com/another)"
        expected_output = [("link", "https://example.com/page"),
                           ("another", "https://example.com/another")]
        assert extract_markdown_links(text) == expected_output

        text = "No links here!"
        expected_output = []
        assert extract_markdown_links(text) == expected_output

        text = "Single link [single](https://example.com/single)"
        expected_output = [("single", "https://example.com/single")]
        assert extract_markdown_links(text) == expected_output


if __name__ == "__main__":
    unittest.main()
