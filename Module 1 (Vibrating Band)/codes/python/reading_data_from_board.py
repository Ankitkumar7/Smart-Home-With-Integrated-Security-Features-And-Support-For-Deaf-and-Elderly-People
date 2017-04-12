import serial #Import Serial Library
import datetime

from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = TwilioRestClient(account_sid, auth_token)

my_msg = "Movement at door, please check"

                

from time import gmtime, strftime	
#import database
import sqlite3
from twilio.rest import TwilioRestClient
client = TwilioRestClient('ACb33e2dc45cee6b88612c9aa53338c5ba', 'a440d31e6a6082bf93c8e3f5a1dbfced')

# conn = sqlite3.connect('visitor.db')
# c = conn.cursor()
def smsService():
    message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg) 
	


# c.execute('''CREATE TABLE IF NOT EXISTS guestbook
#              (Visitor  text, Date text,  Time text)''')

get_date = strftime("%a, %d %b %Y ", gmtime())
get_time = strftime("%H:%M:%S", gmtime())
try:
	arduinoSerialData = serial.Serial('com11',9600)
except serial.serialutil.SerialException:
	print "Please connect device"

database = []
try:
	while True:
		if (arduinoSerialData.inWaiting() > 0):
			myData = arduinoSerialData.readline()
			print myData
except (NameError, serial.serialutil.SerialException):
	print "Device offline"
