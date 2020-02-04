import random

DD = random.randint(1,30) # Max 30  
MM = random.randint(1,12) # Max 12
YYYY = random.randint(1940,2002) # Max 2002
EXTRA = random.randint(1000,9999)

if(DD<10):
    DD = str("0") + str(DD)

if(MM<10):
    MM = str("0")+ str(MM)

username = str(DD)+str(MM)+str(YYYY)+str(EXTRA)

print(username)