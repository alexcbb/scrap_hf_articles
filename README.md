# Scrap Hugging Face Articles

## Goal
The Scrap Hugging Face Articles project is designed to scrap articles from Hugging Face user profiles and convert them into Markdown format. This allows users to easily access and share content from Hugging Face blogs in a more portable format or reuse this in their own blogs. 

## Features
- Retrieve articles from a specified Hugging Face user.
- Convert the articles into Markdown format.
- Extract authors' names from the articles.

## Installation
To install the project, you can use the following command:

```bash
pip install .
```

Make sure you have Python and pip installed on your system.

## Usage
To use the library, you can import the functions from the `scrap_hf_articles` package in your Python code:

```python
from scrap_hf_articles.core import get_user_articles, scrape_huggingface_article_as_markdown

# Example usage
username = "<Hugging Face Username>"
articles = get_user_articles(username)
for article in articles:
    markdown_output, authors = scrape_huggingface_article_as_markdown(article)
    print(authors)
    print(markdown_output)
```

Replace `<Hugging Face Username>` with the actual username of the Hugging Face user whose articles you want to scrape.

## Example
```python
from scrap_hf_articles.core import get_user_articles, scrape_huggingface_article_as_markdown

username = "Beegbrain"
articles = get_user_articles(username)
for article in articles:
    markdown_output, authors = scrape_huggingface_article_as_markdown(article)
    print(authors)
    print(markdown_output)
```

This example will fetch all articles from the user "achapin" and print the Markdown output along with the authors' names.

## Requirements
- Python 3.x
- requests
- beautifulsoup4
- markdownify

## License
This project is licensed under the MIT License.