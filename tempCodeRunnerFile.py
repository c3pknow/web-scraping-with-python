    for article in articles:
        
        title = article.find('h3') or article.find('h1')
        img = article.img.extract()['src']
        
        print(title.get_text(), '\n', img, '\n\n')
        csv_writer.writerow([title.get_text(), img])
