# AES Bit Flipping attack
Purpose of this script is the proof of concept for the revalidation of a forged expired ticket in order to get authenticated and perfornm an action as the original user. In this scenario, the ticket that gives the authorization for a change or a confirmation to a request is a url which has three fields: username, email and validity period. 
We perform a bit flip attack to change the validity period field of the url parameter.
This demo is done for educational purposes only.
---
