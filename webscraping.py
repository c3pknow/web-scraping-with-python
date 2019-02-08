from bs4 import BeautifulSoup


with open('nordstrom.html', 'r') as myfile:
    html=myfile.read()

print(html)

#soup = BeautifulSoup()