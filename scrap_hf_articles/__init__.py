# filepath: /home/achapin/Documents/scrap_hf_articles/scrap_hf_articles/scrap_hf_articles/__init__.py
"""
Scrap Hugging Face Articles

This package provides functionality to scrape articles from Hugging Face user profiles
and convert them into Markdown format.

Available functions:
- get_user_articles: Retrieve articles from a specified Hugging Face user.
- scrape_huggingface_article_as_markdown: Convert a Hugging Face article to Markdown format.
"""

from .core import get_user_articles, scrape_huggingface_article_as_markdown