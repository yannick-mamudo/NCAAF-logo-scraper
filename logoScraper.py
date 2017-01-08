from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib

# adapted from https://github.com/nateberman/Python-WebImageScraper

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "html.parser")

def get_colleges(url):
    soup = make_soup(url)
    colleges = [coll for coll in soup.findAll("a", "bi")]
    college_names = [each.get_text().replace(" ", "_") for each in colleges]
    college_links = [each.get('href') for each in colleges]
    return college_names, college_links

def get_logos(url):
    c_names, c_links = get_colleges(url)
    for i in range(len(c_names)):
        get_logo(c_names[i], c_links[i])

def get_logo(name, link):
    soup = make_soup(link)
    parent = [p for p in soup.findAll(True, {'class':['brand-logo']})]
    img_url = (parent[0].findAll("img")[0].get("src"))
    filename = 'logos/'+name+'.png'
    urllib.urlretrieve(img_url, filename)


get_logos('http://www.espn.com/college-football/teams')