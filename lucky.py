'''11-2
this program reads the argument and opens the first 4 google research results in the browser'''

#!/usr/bin/env python
import sys
import requests
import bs4
import webbrowser

def luckyme():
	#check for argument length
	if len(sys.argv)>1:
		ser='+'.join(sys.argv[1:])
		url="https://www.google.com/search?q="+ser
		res=requests.get(url)
		try:
			res.raise_for_status()
		except Exception as exc:
			print "There is a problem: %s "%exc
			sys.exit()
		f=open('search.html','wb')
		for c in res.iter_content(10000):
			f.write(c)
		#use beautifulsoup module to search for links
		soup=bs4.BeautifulSoup(open('search.html').read(),"html.parser")
		links=soup.select('.r a')
		f.close()
		#open browser tabs
		for i in range (min(4,len(links))):
			webbrowser.open('https://google.com'+links[i].get('href'))
	else:
		print "no search requests received!"
		sys.exit()

luckyme()

'''Study points:
1. modules.
 requests module can grab html file of the specifies url. Note when save the files, open it with 'wb' mode to store using unicode
 beautifulsoup module is similar to regex but works much better for html context. Use CSS selector to search for wanted content
2. code style
 It's ok to write the html into a file and then search on it but you can directly search on res.Text()
3. future usage
 It could be the first step to search for the wanted information from most related search results '''