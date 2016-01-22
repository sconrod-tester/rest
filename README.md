# rest
Requirements:

Python 2.7 

Instructions:

git clone repository
change to repo directory

#python rest-new.py

This starts the REST API which is using the itty python micro-framework

It imports the get_n.py which is a small caculation to get fibonacci number based on a numberical input and throw an error if input is a negative value

You will be prompted to enter in a positive numerical value 

Press enter

The result will return the number you entered and below the fibonacci value


#Please note the original itty.py python micro-framework was simply copied then edited to import get_n.py which was written by myself.

In Progress.

Status:

The rest api when started returns a welcome message and it also prompts at thattime to enter in a numerical value - however, I need remove this prompt from the rest api startup and just make a curl query to the rest api return the prompt- this is in progress.


ubuntu@ubuntu:~/rest$ python rest-new.py
Enter a positive numerical value: 6
6
8
itty starting up (using wsgiref)...
Listening on http://:8080...
Use Ctrl-C to quit.





Thank You,

Sherri Conrod
