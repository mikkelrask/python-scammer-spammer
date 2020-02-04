import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

#url = 'https://innoique.icu/prv/3f5c944e6d930973cedf945fa1c3bdad647/loginerror.php'
#url = 'https://mediation-de.com/prv/12f6009a33bccd92c33a9369248ff983866/loadlogin.php'
url  = 'http://jacobderusha.com/prv/97fd1ae641100c6994d55e4121aaa5dd189/loadlogin.php'

names = json.loads(open('names.json').read())

for name in names:
	#name_extra = ''.join(random.choice(string.digits))

	#username = name.lower() + name_extra

	DD = random.randint(1,30) # Max 30  
	MM = random.randint(1,12) # Max 12
	YYYY = random.randint(1940,2002) # Max 2002
	EXTRA = random.randint(1000,9999)

	if(DD<10):
		DD = str("0") + str(DD)

	if(MM<10):
		MM = str("0")+ str(MM)
	
	username = str(DD) + str(MM) + str(YYYY) + str(EXTRA)
	password = ''.join(random.choice(chars) for i in range(10))

	requests.post(url, allow_redirects=False, data={
		'userid': username,
		'password': password,
		'submit': 'submit'
	})
	print("sending social security number " + username + " and password " + password)
