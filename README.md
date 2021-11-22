# 403bypazz
Automate the procedure of 403 response code bypass
# Description 

The tool uses three techniques to try to bypass 403 response code and give out the response code:

1- Use multiple request methods ( GET - POST- HEAD... etc)

2- Use multiple payloads at the end of URL (kudos to those who tweet these tips)

3- Add headers to the request (X-Forwarded-Host , X-Host ... etc )

# Installation :

1- git clone https://github.com/ShravanBhat/403bypazz.git

2- cd 403bypazz

3- pip3 install -r requirements.txt

# Usage 

the tool take two arguments : url - path 

python3 403bypasser.py url path

EX : python3 403bypasser.py https://www.example.com /index ( space between url and path )

