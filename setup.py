from setuptools import setup, find_packages

setup(
    name='scrap_hf_articles',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'markdownify',
    ],
    entry_points={
        'console_scripts': [
            'scrap_hf_articles=scrap_hf_articles.core:main',
        ],
    },
    author='Alexandre Chapin',
    author_email='alexandre.chapin@ec-lyon.fr',
    description='A tool to scrape articles from Hugging Face user profiles and convert them to Markdown.',
    license='MIT',
    keywords='huggingface scraping markdown',
    url='https://github.com/yourusername/scrap_hf_articles',
)