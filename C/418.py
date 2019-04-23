import requests, bs4, csv

def super_strip(text):
    text = text.strip()
    text = text.replace('\n', ' ')
    return text

def get_title(dom):
    title_elems = dom.select('title')
    if title_elems:    # truthy
        return super_strip(title_elems[0].getText())
    else:
        return "NO TITLE"

with open('links.csv', 'wt', newline='') as fi:
    writer = csv.writer(fi)

    resp = requests.get('https://augusta.edu')
    html_text = resp.text
    #print(html_text[:500])

    au_dom = bs4.BeautifulSoup(html_text, features="html.parser")

    print(get_title(au_dom))
    print('--------------------')

    links = au_dom.select('a')
    for link in links:
        href = link.get('href')

        if not href:    # truthy
            continue

        if '//' not in href[:8]:
            continue
        
        link_text = super_strip(link.getText())

        if not link_text:   # truthy
            images = link.select('img')
            if images:   # truthy
                link_text = images[0].get('alt')

        if not link_text:
            link_text = "NO TEXT"

        print(f"Getting {href}...")
        resp = requests.get(href)
        html_text = resp.text
        link_dom = bs4.BeautifulSoup(html_text, features="html.parser")
        title = get_title(link_dom)

        #print(link_text, href)
        row = (link_text, href, title)
        writer.writerow(row)

