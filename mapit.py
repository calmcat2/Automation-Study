'''Ch11-1
This program reads argument from the user and opens up a browser tab to search the argument in google map.
If there is no argument passed, it will use the last text in clipboard'''


#!/usr/bin/env python

import pyperclip
import webbrowser
import sys

def mapit():
	if len(sys.argv)>1:
		addr='+'.join(sys.argv[1:])		
	else:
		addr=(pyperclip.paste()).replace(' ','+')
	url="https://www.google.com/maps/place/"+addr
	#print url
	webbrowser.open(url)

mapit()

'''Learning points:
1. modules.
 pyperclip is used to get text from clipboard. paste() returns unicode string which should be treated carefully
 webbrowser is used to open up a webpage (needs 'http(s)://' in the url)
2. future usage.
 Can I have give an address and it returns the weather for the next few hours?

