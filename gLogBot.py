
#import all prewritten code modules to use
import colorama #for color
from colorama import Fore #for color
import os
import requests #for GET, POST, etc HTTP requests
from requests import Session
from bs4 import BeautifulSoup as bs #for parsing and reading web content
import time #for sleep
import files #for working with files
from pprint import pprint  #to make output easy on the eyes
import json #for working with JSON filesimport os #for working with the OS

#Definte login variables and Get username and password
#need input validation

print(Fore.CYAN + "\n\tThis program logs in to your Google account and stores the data output of HTTP requests made to Google servers into a directory. It is intended to\n be the beginning of a larger automated form login and data scraping bot. \n")
uName=input(Fore.GREEN + "\n Phone or Gmail: ")
uPass=input(Fore.GREEN + "Password: ")

#create directory variables

path=input(Fore.CYAN + "\n\nEnter path you would like the information stored in format /path/to/directory if unsure leave blank and the current directory will be used: ")

if not path:
   path=os.getcwd()
if path=="pey pey":
   print(Fore.MAGENTA +"What up Pedro!", Fore.RED +" <3 ", Fore.BLUE + " John")
if path=="brent":
   print(Fore.MAGENTA + "What up Brent!", Fore.RED +" <3", Fore.BLUE + " John")
if path=="jason":
   print(Fore.MAGENTA + "JAY SOHN!!!!", Fore.RED +" <3", Fore.BLUE + " John")
if path=="joanne":
   print(Fore.MAGENTA + "Hey MOM! I LOVE YOU!!!", Fore.RED +" <3", Fore.BLUE + "John")
if path=="amy":
   print(Fore.MAGENTA + "Hey Amy!", Fore.RED +" <3", Fore.BLUE + " John")

try: os.mkdir(path)
except OSError as error:
   print("Using previous directory.")
finally: os.chdir(path)

#Try to login

form_data={'Email': uName, 'Password': uPass}
post = "https://accounts.google.com/signin/challenge/sl/password"

with requests.Session() as s:

  soup = bs(s.get("https://mail.google.com").text, "html.parser")
  for inp in soup.select("#gaia_loginform input[name]"):
   if inp["name"] not in form_data:
    form_data[inp["name"]] = inp["value"]
  s.post(post, form_data)
  html = s.get("https://mail.google.com/mail/u/0/#inbox").content

my_mail=s.get("https://mail.google.com/mail/u/0/#inbox").text
True

#Print variables to screen and save results for further study

pprint("Data dump in 5, 4, 3, 2... ")
time.sleep(5)

pprint("::::::::::::::SOUP:::::::::::::::::")
pprint("-----------------------------------")
time.sleep(5)

with open('soup.html', 'w', encoding='utf-8') as f:
 f.write(str(soup))
 f.close()

print(soup.prettify)


time.sleep(5)
pprint("::::::::::::::YOUR_MAIL::::::::::::::")
time.sleep(5)


with open('myMail.txt', 'w') as f:
 f.write(my_mail)
 f.close()

time.sleep(5)
pprint(my_mail)
time.sleep(5)

time.sleep(5)
pprint(":::::::::::::HTML::::::::::::::")
time.sleep(5)


with open('html.html', 'w', encoding='utf-8') as f:
 f.write(str(html))
 f.close()

time.sleep(5)
pprint(html)
time.sleep(5)

time.sleep(5)
pprint("::::::::::::FORM_DATA:::::::::::")
time.sleep(5)


with open('formData.txt', 'w') as f:
 f.write(json.dumps(form_data))
 f.close()

pprint(form_data)
#
