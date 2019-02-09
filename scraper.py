import requests
from bs4 import BeautifulSoup
from csv import writer

def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

response = requests.get('https://weather.com/')
soup = BeautifulSoup(response.text, 'html.parser')


articles = soup.find_all(class_='wx-media-object')
print(len(articles))

with open('articles.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Image']
    csv_writer.writerow(headers)

    for article in articles:

        title = article.find('h3') or article.find('h1')
        img = article.img.extract()['src']

        print(title.get_text(), '\n', img, '\n\n')
        csv_writer.writerow([title.get_text(), img])
