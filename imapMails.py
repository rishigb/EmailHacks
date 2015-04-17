#!/usr/bin/env python

from imapclient import IMAPClient
import time
import configVal
#import RPi.GPIO as GPIO

DEBUG = True

HOSTNAME = 'imap.gmail.com'
USERNAME = configVal.details["username"]
PASSWORD = configVal.details["password"]
MAILBOX = 'Inbox'

NEWMAIL_OFFSET = 1   # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 60 # check mail every 60 seconds

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GREEN_LED = 18
#RED_LED = 23
#GPIO.setup(GREEN_LED, GPIO.OUT)
#GPIO.setup(RED_LED, GPIO.OUT)

def loop():
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)

    if DEBUG:
        print('Logging in as ' + USERNAME)
        select_info = server.select_folder(MAILBOX)
        print('%d messages in INBOX' % select_info['EXISTS'])

    folder_status = server.folder_status(MAILBOX, 'UNSEEN')
    newmails = int(folder_status['UNSEEN'])

    if DEBUG:
        print "You have", newmails, "new emails!"

    if newmails > NEWMAIL_OFFSET:
	print "emails undread here"
    time.sleep(MAIL_CHECK_FREQ)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        #GPIO.cleanup()
	print "end here"
