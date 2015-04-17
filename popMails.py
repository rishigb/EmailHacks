import poplib
import configVal
pop3_host = 'pop.gmail.com'
pop3_user = configVal.details["username"]
pop3_pass = configVal.details["password"]

## connect to host using SSL
pop3_mail = poplib.POP3_SSL(pop3_host)

## print the response message from server
print pop3_mail.getwelcome()

## send user
pop3_mail.user(pop3_user)

## send password
pop3_mail.pass_(pop3_pass)

## get mail box stats; returns an array
pop3_stat = pop3_mail.stat()

print "Total New Mails : %s (%s bytes)" % pop3_stat

## let's fetch one latest mail
print "\n\n===\nLatest Mail\n===\n\n"

## fetch the top mail
latest_email = pop3_mail.retr(1)

## print the message
print latest_email[3]
#        print mail
#pop3_mail.dele(1)


