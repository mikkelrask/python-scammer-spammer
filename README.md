# Scammer Spammer

The Python-scammer-spammer is originally forked from Engineering Man and then modified as I generally use it, to spam people who try to phish me in my inbox. 

It gives you some options on what to do, as it can send either fake usernames, emails or social security numbers, depending on, what the phishing sites you want to spam, is out to get. 

In the stout Scammer Spammer posts what usernames and data is send. 

## How to:

'''
git clone https://github.com/mikkelrask/python-scammer-spammer.git
cd python-scammer-spammer
pip install -r requirements
python scammer.py
'''

Open up the developer tools in your browser, on the phishing website, and go to the Network tab and tick on Persist Log (in firefox, anyways). Now type in some easy identifiable text in the form, and click submit. Go through the lines that generates after you click the submit button, and find the file we rech with the POST method, and see what params it is expecing. Right click that line and pick "Copy -> Copy URL", and supply it in the script, when asked.
Having the POST method line marked click the Params in the right side window, and youshow you the id and the dummy data we just input. 