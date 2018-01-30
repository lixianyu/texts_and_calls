import time
import urllib
import re
import bs4
import requests

open_log = False
start_url = "https://en.wikipedia.org/wiki/Special:Random"
#start_url = "https://en.wikipedia.org/wiki/Physics"
#start_url = "https://en.wikipedia.org/wiki/Logic"
#start_url = "https://en.wikipedia.org/wiki/Non-fiction"
#start_url = "https://en.wikipedia.org/wiki/Counting"
#start_url = "https://en.wikipedia.org/wiki/Ferguson_Township,_Centre_County,_Pennsylvania"
#start_url = "https://en.wikipedia.org/wiki/Science"
#start_url = "https://en.wikipedia.org/wiki/Biological_classification"
#start_url = "https://en.wikipedia.org/wiki/Geometry"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    # This div contains the article's body
    # (June 2017 Note: Body nested in two div tags)
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None
    a1 = re.compile(r'\s\(.*?\)+?[\,\s,\<]+')
    #a2 = re.compile(r'href\={1}\".+?\"{1}')
    a2 = re.compile(r'\/wiki\/.+?\"')
    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if open_log:
            print('element = \n{}'.format(element))
            print('...............................................................................')
        str_element = str(element)
        #idx = str_element.find(')')
        #print('idx = {}'.format(idx))
        #print('idx = {}'.format(idx))
        #print(type(idx))
        str_element = a1.sub('', str_element)
        if open_log:
            print('str_element = {}'.format(str_element))
            print('...............................................................................')
        alla = a2.findall(str_element)
        if open_log:
            print('alla = {}'.format(alla))
            print('-------------------------------------------------------------------------------')
        if len(alla) != 0:
            article_link = alla[0][:-1]
            if open_log:
                print('article_link = {}'.format(article_link))
            break

        '''
        if element.find("a", recursive=False):
        #if new_tag.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            #article_link = new_tag.find("a", recursive=False).get('href')
            # print('element = {}'.format(element))
            #print(type(article_link))
            break
        '''
    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

def continue_crawl(search_history, target_url, max_steps=30):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        print("> {}".format(target_url))
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        print("--- {}".format(search_history[-1]))
        return False
    else:
        return True

article_chain = [start_url]
counts = 1
while continue_crawl(article_chain, target_url):
    print('{}: {}'.format(counts, article_chain[-1]))
    counts += 1

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)

    time.sleep(2) # Slow things down so as to not hammer Wikipedia's servers
