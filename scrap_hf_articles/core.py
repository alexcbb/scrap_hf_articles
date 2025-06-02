import requests
from bs4 import BeautifulSoup
import markdownify
import argparse


def get_user_articles(username):
    url = f"https://huggingface.co/{username}/activity/articles"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for a in soup.find_all("a", href=True):
        href = a['href']
        if href.startswith(f"/blog/"):
            articles.append("https://huggingface.co" + href)

    return list(set(articles))  # remove duplicates if any

def scrape_huggingface_article_as_markdown(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the article. Status code: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the main content
    content_div = soup.find('div', class_='blog-content')
    if content_div:
        authors = []
        divs = soup.find_all('div', class_='not-prose')
        for div in divs:
            images = div.find_all('img', alt=True)
            for img in images:
                if img['alt'].strip():  # non-empty alt
                    authors.append(img['alt'].strip().replace("'s avatar", ""))

        for a in content_div.find_all('a', href=True):
            if "Back to Articles" in a.text:
                a.decompose()
            if "Update on GitHub" in a.text:
                a.decompose()
            if "Edit article" in a.text:
                a.decompose()
        for div in content_div.find_all('div', class_='not-prose'):
            div.decompose()
    if not content_div:
        raise Exception("Main content not found in the article.")

    # Convert HTML content to Markdown
    html_content = str(content_div)
    markdown_content = markdownify.markdownify(html_content, heading_style="ATX")

    return f"{markdown_content.strip()}", list(set(authors))