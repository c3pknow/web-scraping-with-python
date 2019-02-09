try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    from BeautifulSoup import BeautifulSoup as bs



with open('nordstrom.html', 'r', encoding='utf-8') as myfile:
    html = myfile.read()

#print(html)

soup = bs(html, 'html.parser')


# Direct
#
# print(soup.body.encode('utf-8'))
# print(soup.head.encode('utf-8'))
# print(soup.head.title.encode('utf-8'))


# Find()  // Finds first
el = soup.find('div').encode('utf-8')
#print(el)


# Find All: find_all() or findall()  // Finds all, returns list
el = soup.find_all('div')
print(len(el))
print('\n')

# Find by ID 
el = soup.find(id='GlobalDesktopNavFlyout2')
print(el)
print('\n')

# Find by Class (class is a reserved word, need to append '_')
el = soup.find(class_='shopping-bag-links')
print(el)
print('\n')

# Find by (data) attributes
el = soup.find(attrs={"data-element":"touch-target"})
print(el)
print('\n')


# Select  // Always returns as a list, even if only one
el = soup.select('#product-results-query-anchor')
print(el)
print('\n')



# Get Text: get_text()
el = soup.find(class_='tile-link_G92ai').get_text()
print(el)
print('\n')


for item in soup.select('.tile-link_G92ai'):
    print(item.get_text())
print('\n')



# DOM Navigation
el = soup.body.contents[5]
sibling = el.find_next_sibling()
print(sibling.encode('utf-8'))
print('\n')

sibling = el.find_previous_sibling()
print(sibling.encode('utf-8'))
print('\n')

el = soup.find(class_='tile-link_G92ai')
print(el.find_parent().find_child())

# Pass in a element type to find specific next/previous sibling
# sibling = el.find_previous_sibling('li')

# for item in el:
#    print(item.encode('utf-8'))