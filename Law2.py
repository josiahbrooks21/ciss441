from bs4 import BeautifulSoup
import requests

fname, purl = 'slk_law','https://en.wikipedia.org/wiki/Rich_Wilkerson_Jr.'
res = requests.get(purl)
webcontent = res.text
with open(fname + '.txt', encoding='utf-8', mode='w') as fo:
	fo.write(webcontent)
	
soup = BeautifulSoup(webcontent, "html.parser")
print('\n\n', purl, res.status_code)

ptitle = soup.title
if ptitle:
	print(ptitle.string)