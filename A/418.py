import requests, bs4, csv

def super_strip(text):
    text = text.strip()
    text = text.replace('\n', ' ')
    return text

def get_title(dom):
    titles = dom.select('title')
    if titles:   # truthy because if there is a title, titles has len > 0
        return super_strip(titles[0].getText())



url = 'https://augusta.edu'
resp = requests.get(url)
html_text = resp.text

#print(html_text[:5000])
dom = bs4.BeautifulSoup(html_text, features="html.parser")

print(get_title(dom))
print('------------------')


with open('links.csv', 'wt', newline='') as fi:

    links = dom.select('a')
    for link in links:
        href = link.get('href')
        if not href:    # truthy
            continue
        
        href = href.strip()
        is_ext = '//' in href[:8]
        if not is_ext:
            continue

        href_text = super_strip(link.getText())

        if not href_text:   # truthy
            images = link.select('img')
            if images:    # truthy
                alt_text = images[0].get('alt')
                if not alt_text:
                    href_text = "IMAGE HERE"
                else:
                    href_text = super_strip(alt_text)

        if not href_text:
            href_text = "NO TEXT"

        print(f"getting {href}")
        resp = requests.get(href)
        html_text = resp.text
        inner_dom = bs4.BeautifulSoup(html_text, features="html.parser")
        title = get_title(inner_dom)

        #print(href_text, href)
        writer = csv.writer(fi)
        row = (href_text, href, title)
        writer.writerow(row)

