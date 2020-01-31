The Python-scammer-spammer is originally forked from Engineering Man and then modified as I generally use it, to spam people who try to phish me in my inbox. 
What it does is loop through the names.json file, and generate either random usernames or emails and passwords, to send as fake data to the scammer, and hopefully make their data pool unusable. 

In the stout it posts what usernames and data is send. 

How to:

Open up the developer tools in your browser, on the phishing website, and go to the Network tab and tick on Persist Log (in firefox, anyways). Now type in some easy identifiable text in the form, and click submit. Go through the lines that generates after you click the submit button, and find the file we rech with the POST method, and see what params it is expecing. Right click that line and pick "Copy -> Copy URL", and paste it in the URL variable.
Having the POST method line marked click the Params in the right side window, and youshow you the id and the dummy data we just input. 

The field ID that holds our userID should replace 'userid' on line 22
The field ID that holds our password should replace 'password' on line 23

Now the script should be primed, and ready to spam our scammer.
