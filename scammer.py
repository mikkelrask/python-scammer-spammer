import requests
import os
import random
import string
import json

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

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# What are we going to send?
print('What do we wish to send today?')
print('1: Usernames and password')
print('2: Email-address and passwords')
print('3: Social security numbers and passwords')
print('')
userformat = int(input('Please pick: '))
print('')
url  		= input('Please inset POST URL that requests data: ')
print('')
userinput 	= input('Name of the username input: ')
print('')
passwinput 	= input('Name of the password input: ')
print('')
datanumbers = int(input('How many logins do you wish to send: '))
print('')

names = json.loads(open('names.json').read())


i = 1
while(i<datanumbers):
	#Username / Email generation
	for name in names:
		name_extra = ''.join(random.choice(string.digits))
		username = name.lower() + name_extra
		username = name.lower() + name_extra
		email = username + '@live.dk'

	#Danish SSN generator
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
	password = ''.join(random.choice(chars) for i in range(10))

	if(userformat == 1):
		choice = username
	elif(userformat == 2):
		choice = email
		username = email
	elif(userformat == 3):
		username = ssn

	requests.post(url, allow_redirects=False, data={
		userinput: username,
		passwinput: password,
		'submit': ''
	})
	print("sending login " + username + " and password " + password)

print('')
print('Successfully sent ' + str(datanumbers) + ' fake random logins to the POST url ' + url)
print('*****************************************************************************')
print("Please consider reporting this URL to the google report phishing form found ")
print("here to help warn others that aren/'t as techsavvy as you - thanks!")
print('')
print('https://safebrowsing.google.com/safebrowsing/report_phish/')