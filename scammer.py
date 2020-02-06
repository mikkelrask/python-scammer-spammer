import requests
import os
import random
import string
import json
import socket
import whois

from querycontacts import ContactFinder

passwordrange = 12

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def menu():
	print(bcolors.BOLD + 'What do want to do?' + bcolors.ENDC)
	print('1: Spam Usernames and password')
	print('2: Spam Email-address and passwords')
	print('3: Spam Social security numbers and passwords')
	print('4: Find abuse contacts for domain and host')
	print('5. Report website')
	print('6. Set password lenght (Default 12 - resets each session')
	print('q: Quit')
	print('')

	userformat = input('Please pick: ')
	if(userformat == 'q'):
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
	
	domain = input(bcolors.BOLD + "What domain do you wish to look up: " + bcolors.ENDC)
	domainwhois = "whois " + domain + " | grep @"
	print("Searching for abuse contacts for " + bcolors.UNDERLINE + domain + bcolors.ENDC)
	print("")
	domainresult = os.popen(domainwhois)	
	ip = socket.gethostbyname(domain)
	IPabuse = qf.find(ip)
	print('Server hosting: (' + ip + ')')
	print(bcolors.OKGREEN + ". ".join(repr(e) for e in IPabuse) + bcolors.ENDC)
	print('')
	print('Domain host/registrar: ' + domain)
	print(bcolors.OKGREEN + domainresult.readline() + bcolors.ENDC) 
	
	
	input("Press Enter to continue...")
	menu()

def socialsecuritynumber():
	url  		= input('Please inset POST URL that requests data: ')
	print('')
	userinput 	= input('Name of the username input: ')
	print('username input: ' + userinput)
	passwinput 	= input('Name of the password input: ')
	print('password input: ' + passwinput)
	datanumbers = int(input('How many logins do you wish to send: '))
	print('Sending a total of ' + str(datanumbers) + ' logins.' )

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
		print("sending login " + bcolors.WARNING + ssn + bcolors.ENDC + " and password " + bcolors.WARNING + password + bcolors.ENDC)
		count+=1
	print('')
	print('Successfully sent ' + bcolors.BOLD + str(datanumbers) + bcolors.ENDC + ' fake random logins to the POST url ' + url)
	print('*****************************************************************************')
	print("Please consider reporting this URL to the google report phishing form found ")
	print("here to help warn others that aren't as techsavvy as you - thanks!")
	print('')
	print('Link: https://safebrowsing.google.com/safebrowsing/report_phish/')
	input("Press ENTER to continue...")
	menu()



chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))



def usernames():
	names = json.loads(open('names.json').read())
	name_extra = ''.join(random.choice(string.digits))
	name = names + name_extra

	url = input('Please inset POST URL that requests data: ')
	print('')
	userinput = input('Name of the username input: ')
	print('username input: ' + userinput)
	passwinput = input('Name of the password input: ')
	print('password input: ' + passwinput)
	datanumbers = int(input('How many logins do you wish to send: '))
	print('Sending a total of ' + str(datanumbers) + ' logins.' )
	password = ''.join(random.choice(chars) for i in range(passwordrange))

	
	for name in names:
		name_extra = ''.join(random.choice(string.digits))

		username = name.lower() + name_extra + '@yahoo.com'
		password = ''.join(random.choice(chars) for i in range(8))

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
	print('Successfully sent ' + bcolors.BOLD + str(datanumbers) + bcolors.ENDC + ' fake random logins to the POST url ' + url)
	print('*****************************************************************************')
	print("Please consider reporting this URL to the google report phishing form found ")
	print("here to help warn others that aren't as techsavvy as you - thanks!")
	print('')
	print('Link: https://safebrowsing.google.com/safebrowsing/report_phish/')
	input("Press ENTER to continue...")
	menu()

def emails():
	print('Emails')
	menu()



#i = 1
#for name in range(datanumbers):
	#Username / Email generation
	#name_extra = ''.join(random.choice(string.digits))
	#username = name.lower() + name_extra
	#username = name.lower() + name_extra
	#email = username + '@live.dk'

	#Danish SSN generator
#	

print('mmmmmmm #                     mmmm                                           ')
print('   #    # mm    mmm          #"   " mmmm    mmm   mmmmm  mmmmm   mmm    m mm ')
print('   #    #"  #  #"  #         "#mmm  #" "#  "   #  # # #  # # #  #"  #   #"  "')
print('   #    #   #  #""""             "# #   #  m"""#  # # #  # # #  #""""   #    ')
print('   #    #   #  "#mm"         "mmm#" ##m#"  "mm"#  # # #  # # #  "#mm"   #    ')
print('                                    #                                        ')
print('                                    "                                        ')
print('')
print('*****************************************************************************')
print('')
print('Please use with care. Do not spam websites, that arent phishing for data.')
print('You will need to find the POST URL, username input and password input ')
print('before continuing.')
print('See https://github.com/mikkelrask/python-scammer-spammer for details.')
print('')
print('*****************************************************************************')
print('')
print('What do want to do?')
print('1: Spam Usernames and password')
print('2: Spam Email-address and passwords')
print('3: Spam Social security numbers and passwords')
print('4: Find abuse contacts for domain and host')
print('5. Report website')
print('q: Quit')
print('')
userformat = input('Please pick: ')
if(userformat == 'q'):
	exit()
elif(userformat == "1"):
	usernames()
elif(userformat == "2"):
	emails()
elif(userformat == "3"):
	socialsecuritynumber()
elif(userformat == "4"):
	abusecontact()