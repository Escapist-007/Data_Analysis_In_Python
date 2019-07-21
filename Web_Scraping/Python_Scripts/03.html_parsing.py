import requests as re,bs4

# Step 01: Creating a BeautifulSoup Object from HTML

response = re.get('https://nostarch.com/automatestuff/')

try:
    response.raise_for_status()
    
    data = response.text
    
    soup = bs4.BeautifulSoup(data,'html.parser')
    
#     print(soup.prettify())
except Exception as exc:
    print('There was a problem: %s' % (exc))



# Step 02: Finding an Element with the select() Method

elems = soup.select('div .field-items')

print("Total Number of 'div' elements",len(elems))

for i in elems:
    if "by Al Sweigart" in str(i.getText()):
        print("             -----         ")
        print()
        print(i.getText())
        print(i.attrs)
        print()
