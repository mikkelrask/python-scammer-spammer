import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

#url = 'https://innoique.icu/prv/3f5c944e6d930973cedf945fa1c3bdad647/loginerror.php'
url = 'https://mediation-de.com/prv/12f6009a33bccd92c33a9369248ff983866/loadlogin.php'

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra
	password = ''.join(random.choice(chars) for i in range(10))

	requests.post(url, allow_redirects=False, data={
		'userid': username,
		'password': password,
		'submit': 'submit'
	})
	print("sending username " + username + " and password " + password)
