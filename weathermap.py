#! python3
#mapit.py - launches map
import webbrowser, sys, pyperclip

#sys.argv # ['mapit.py', '870', 'Valencia', 'St.']
#check if arguements are passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
	
else:
    address = pyperclip.paste()


webbrowser.open('https://www.wunderground.com/forecast/us/ca/' + address)
