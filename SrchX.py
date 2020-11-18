#import modules

from googlesearch import search
from colorama import Fore, init
init()
print(Fore.GREEN)

import time
time.sleep(1)

banner = """
000000000000000000000000000
0   ----  SrchX ----      0
0           by            0
0      Blacksterhack      0
000000000000000000000000000
"""
print(banner)

Disclaimer = "This program was created for purposes only"
print(Disclaimer)

time.sleep(1)

Menu = """
1- Users and admins passwords(Web pages).
2- Pages with login forms.
3- Files with user names or error messages that reveal the username.
4- Detection of the web server version or vulnerable product.
5- Hardware devices online(cameras, prints, etc).
6- Sensitive directories on a server.
7- Information to support access.
"""
print(Menu)

#Variables.
user_admins = "ext:pwd inurl:(service | authors | administrators | users) “# -FrontPage-“"
L_forms = "inurl:/admin/login.asp"
f_use_names = "“access denied for user” “using password” “general error” -inurl:phpbb “sql error”"
dec_web_server = "“SquirrelMail version 1.4.4” inurl:src ext:php"
hard_dev = "camera linksys inurl:main.cgi"
sen_fic = "“phone  * * *” “address *” “e-mail” intitle:”curriculum vitae”"
Inf_SA = "inurl:”:8080″ -intext:8080"

option = int(input("Choose an option: "))
#searching with the googlesearch module.
if option==1:
	for i in search(user_admins, start = 0, num = 30 , pause = 2):
		print(i)

if option==2:
	for i in search(L_forms, start = 0, num = 30, pause = 2):
		print(i)

if option==3:
	for i in search(f_use_names, start = 0, num = 30, pause = 2):
		print(i)

if option==4:
	for i in search(dec_web_server, start = 0, num = 30, pause = 2):
		print(i)

if option==5:
	for i in search(hard_dev, start = 0, num = 30, pause = 2):
		print(i)


if option==6:
	for i in search(sen_fic, start = 0, num = 30, pause = 2):
		print(i)
		

if option==7:
	for i in search(Inf_SA, start = 0, num = 30, pause = 2):
		print(i)
