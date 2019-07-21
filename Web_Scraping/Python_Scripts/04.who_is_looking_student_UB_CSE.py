import requests as re
import webbrowser as wb
import sys
import pyperclip
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse


def get_soup(url):
    try:
        res = re.get(url, timeout=1)
        
        res.raise_for_status()
        return bs(res.text,'html.parser')
    
    except re.Timeout as err:
        print(err)
        return 0
    
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        return 0


def has_specific_attribute(tag):
    return tag.has_attr('target') and not tag.has_attr('class')



# url = 'https://engineering.buffalo.edu/computer-science-engineering/people/faculty-directory.html'


if len(sys.argv) > 1:
    url = ' '.join(sys.argv[1:])
else:
    url = pyperclip.paste()


all_faculty_links = []

soup = get_soup(url)

if soup==0:
    print("Error in URL loading")

span_tags = soup.select('.staff_name_bolded')

print("Total Faculty : ", len(span_tags))

for span_tag in span_tags:
    anchor_tag = span_tag.select('a')
    link = anchor_tag[0].get('href')
    
    # If there is no url in href. Ex: < a href=""> Something </a>
    if link is None:
        print("No Link")
        continue
    
    # Need to check whether the link is an absolute link or relative link
    elif link.startswith('http'):
        all_faculty_links.append(link)
    else:
        o = urlparse(url)
        full_link = 'https://' + o.netloc + link
        all_faculty_links.append(full_link)


faculty_personal_websites = []

flag = True

for link in all_faculty_links:
    
    soup = get_soup(link)
    
    anchor_tags = soup.find_all(has_specific_attribute)
    
    for tag in anchor_tags:
        
        innerText = ''
        
        '''
            # First I use thd below approach but later I find a easy way for the same task - `tag.text`
            
            # Skip the tag elements if it hase text in depth 1 or depth 2 in the descendent tree
            if tag.string is not None or tag.contents[-2].string is not None :
            continue
            
            innerText = str(tag.contents[-2].contents[-2].string).lower()  # Depth 3
            
            '''
        
        innerText = tag.text.strip().lower()
        
        if flag is True:
            print(tag.prettify())
            flag = False
    
        if "website" in innerText:
            link = tag.get('href')
            if link is None:
                continue
        else:
            faculty_personal_websites.append(link)


for link in faculty_personal_websites:
    
    soup = get_soup(link)
    
    if soup==0:
        print("Error")
        continue
    text = str(soup.get_text()).lower()

    if "looking for" in text:
        wb.open(link)
