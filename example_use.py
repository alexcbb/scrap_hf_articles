from scrap_hf_articles.core import get_user_articles, scrape_huggingface_article_as_markdown

# Example usage
username = "Beegbrain"
articles = get_user_articles(username)
print(f"Found {len(articles)} articles for user '{username}':")
if not articles:
    print("No articles found.")
for article in articles:
    markdown_output, authors = scrape_huggingface_article_as_markdown(article)
    print(authors)
    print(markdown_output)