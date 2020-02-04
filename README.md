 ____                                          
/ ___|  ___ __ _ _ __ ___  _ __ ___   ___ _ __ 
\___ \ / __/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 ___) | (_| (_| | | | | | | | | | | |  __/ |   
|____/ \___\__,_|_| |_| |_|_| |_| |_|\___|_|   
                                               
 ____                                            
/ ___| _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
\___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
 ___) | |_) | (_| | | | | | | | | | | |  __/ |   
|____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
      |_| 
      

The Python-scammer-spammer is originally forked from Engineering Man and then modified as I generally use it, to spam people who try to phish me in my inbox. 

It gives you some options on what to do, as it can send either fake usernames, emails or social security numbers, depending on, what the phishing sites you want to spam, is out to get. 

In the stout Scammer Spammer posts what usernames and data is send. 

How to:

Open up the developer tools in your browser, on the phishing website, and go to the Network tab and tick on Persist Log (in firefox, anyways). Now type in some easy identifiable text in the form, and click submit. Go through the lines that generates after you click the submit button, and find the file we rech with the POST method, and see what params it is expecing. Right click that line and pick "Copy -> Copy URL", and supply it in the script, when asked.
Having the POST method line marked click the Params in the right side window, and youshow you the id and the dummy data we just input. 