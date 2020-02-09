import requests
import os
import random
import string
import json
import socket
import whois

from querycontacts import ContactFinder

passwordrange = 12
extra_char_range = 4

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def waitforinput():
	input(bcolors.BOLD + "Press Enter to continue ..." + bcolors.ENDC)
	print('')

def banner():
	print('mmmmmmm #                     mmmm                                           ')
	print('   #    # mm    mmm          #"   " mmmm    mmm   mmmmm  mmmmm   mmm    m mm ')
	print('   #    #"  #  #"  #         "#mmm  #" "#  "   #  # # #  # # #  #"  #   #"  "')
	print('   #    #   #  #""""             "# #   #  m"""#  # # #  # # #  #""""   #    ')
	print('   #    #   #  "#mm"         "mmm#" ##m#"  "mm"#  # # #  # # #  "#mm"   #    ')
	print('                                    #                                        ')
	print('                                    "                                        ')
	print('*****************************************************************************')
	print('v. 0.1')
	print('Please use with care. Do not spam websites, that arent phishing for data.')
	print('You will need to find the POST URL, username input and password input ')
	print('before continuing.')
	print('See https://github.com/mikkelrask/python-scammer-spammer for details/issues.')
	print('')
	print('*****************************************************************************')

def finishbanner():
	print('*****************************************************************************')
	print("Please consider reporting this URL to the google report phishing form found ")
	print("here to help warn others that aren't as techsavvy as you - thanks!")
	print('')
	print('[ ' + bcolors.OKGREEN + 'x' + bcolors.ENDC + ' ] Link:' + bcolors.OKGREEN + bcolors.UNDERLINE + 'https://safebrowsing.google.com/safebrowsing/report_phish/' + bcolors.ENDC)
	waitforinput()
	
def menu():
	print(bcolors.BOLD + 'What do want to do?' + bcolors.ENDC)
	print('[ 1 ] ' + bcolors.OKGREEN + 'Spam Usernames and password' + bcolors.ENDC)
	print('[ 2 ] ' + bcolors.OKGREEN + 'Spam Email-address and passwords' + bcolors.ENDC)
	print('[ 3 ] ' + bcolors.OKGREEN + 'Spam Social security numbers and passwords' + bcolors.ENDC)
	print('[ 4 ] ' + bcolors.OKGREEN + 'Find abuse contacts for domain and host' + bcolors.ENDC)
	print('[ x ] ' + bcolors.OKGREEN + 'Exit' + bcolors.ENDC)
	print('')

	userformat = input('Please pick: ')
	if(userformat == 'q'):
		exit()
	elif(userformat == 'x'):
		exit()
	elif(userformat == 'X'):
		exit()
	elif(userformat == "1"):
		usernames()
	elif(userformat == "2"):
		emails()
	elif(userformat == "3"):
		socialsecuritynumber()
	elif(userformat == "4"):
		abusecontact()
	print('')

def abusecontact():
	qf = ContactFinder()
	
	domain = input(bcolors.BOLD + "[ * ] What domain do you wish to look up: " + bcolors.ENDC)
	domainwhois = "whois " + domain + " | grep @"
	print("[ " + bcolors.OKGREEN + "+" + bcolors.ENDC + " ] Searching for abuse contacts for " + bcolors.UNDERLINE + domain + bcolors.ENDC)
	domainresult = os.popen(domainwhois)	
	ip = socket.gethostbyname(domain)
	print('[ ' + bcolors.OKGREEN + '+' + bcolors.ENDC + ' ] Pinging ' + domain + ' ...  ... ' + bcolors.OKGREEN + ip + bcolors.ENDC)
	IPabuse = qf.find(ip)
	print('')
	print('Abuse contact for the hosting server:')
	print(bcolors.FAIL + ". ".join(repr(e) for e in IPabuse) + bcolors.ENDC)
	print('')
	print('Abuse contact for the domain host/registrar for: ' + domain)
	print(bcolors.FAIL + domainresult.readline() + bcolors.ENDC) 
	
	waitforinput()
	menu()

def userinput():
	url  		= input('[ * ] Please inset POST URL that requests data: ')
	print('')
	userinput 	= input('[ * ] Name of the username input: ')
	passwinput 	= input('[ * ] Name of the password input: ')
	datanumbers = int(input('[ + ] How many logins do you wish to send: '))
	print('')
	print(bcolors.BOLD + 'Sending a total of ' + str(datanumbers) + ' logins.' + bcolors.ENDC)
	print('')
	print('*****************************************************************************')
	print('')

def socialsecuritynumber():
	userinput()
	count=0
	while count <= datanumbers:
		DD = random.randint(1,30) # Max 30  
		MM = random.randint(1,12) # Max 12
		YYYY = random.randint(1940,2002) # Max 2002
		EXTRA = random.randint(1000,9999)

		if(DD<10):
			DD = str("0") + str(DD)

		if(MM<10):
			MM = str("0")+ str(MM)
		
		ssn = str(DD) + str(MM) + str(YYYY) + str(EXTRA)

		# Password generator
		password = ''.join(random.choice(chars) for i in range(passwordrange))
		requests.post(url, allow_redirects=False, data={
			userinput: ssn,
			passwinput: password,
			'submit': ''
		})
		print("[ " + bcolors.OKGREEN + "+" + bcolors.ENDC + " ] sending login " + bcolors.WARNING + ssn + bcolors.ENDC + " and password " + bcolors.WARNING + password + bcolors.ENDC)
		count+=1
	print('')
	print('[ ' + bcolors.OKGREEN + 'x ] ' + bcolors.ENDC + ' Successfully sent ' + bcolors.BOLD + str(datanumbers) + bcolors.ENDC + ' fake random logins to the POST url ' + url)
	finishedbanner()
	menu()

def usernames():
	userinput()

	names = json.loads(open('names.json').read())
	name_extra = ''.join(random.choice(string.digits))
	name = names + name_extra

	password = ''.join(random.choice(chars) for i in range(passwordrange))

	count = 0
	while count < datanumbers:
		name_extra = ''.join(random.choice(string.digits))

		username = random.choice().lower() + name_extra
		password = ''.join(random.choice(chars) for i in range(4))

		requests.post(url, allow_redirects=False, data={
			userinput: username,
			passwinput: password,
			'submit': ''
		})
		print("sending login " + bcolors.WARNING + username + bcolors.ENDC + " and password " + bcolors.WARNING + password + bcolors.ENDC)
		
	
	#count = 0
	#while count < datanumbers:
	#	username = name.lower() + name_extra
	#	username = name.lower() + name_extra
	#	print("sending login " + bcolors.WARNING + username + bcolors.ENDC + " and password " + bcolors.WARNING + password + bcolors.ENDC)

	#	count += 1

	
	print('')
	print('[ ' + bcolors.OKGREEN + 'x' + bcolors.ENDC + ' ] Successfully sent ' + bcolors.BOLD + str(datanumbers) + bcolors.ENDC + ' fake random logins to the POST url ' + url)
	print('*****************************************************************************')
	print("Please consider reporting this URL to the google report phishing form found ")
	print("here to help warn others that aren't as techsavvy as you - thanks!")
	print('')
	print('Link: https://safebrowsing.google.com/safebrowsing/report_phish/')
	waitforinput()
	menu()

def emails():
	userinput()
	s
	chars = string.ascii_letters + string.digits + '!@#$%^&*()'
	random.seed = (os.urandom(1024))	
	for name in names:
		name_extra = ''.join(random.choice(string.digits))

		username = name.lower() + name_extra + '@yahoo.com'
		password = ''.join(random.choice(chars) for i in range(passwordrange))

		requests.post(url, allow_redirects=False, data={
			'auid2yjauysd2uasdasdasd': username,
			'kjauysd6sAJSDhyui2yasd': password
		})


	menu()

banner()
menu()