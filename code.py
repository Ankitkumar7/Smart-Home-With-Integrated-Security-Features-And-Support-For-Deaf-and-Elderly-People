import serial
from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio
client = TwilioRestClient(account_sid, auth_token)

def sms():
	my_msg = "someone at door"
	message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)   


#database connection
from peewee import *

db = SqliteDatabase('visitorLog.db')

class Person(Model):
    image = CharField()
    date =  DateTimeField()
    time = DateTimeField()

   
    class Meta:
        database = db # This model uses the "people.db" database.



arduinoSerialData = serial.Serial('com10',9600)
database = []
try:
        if (arduinoSerialData.inWaiting() > 0):
                myData = arduinoSerialData.readline()
                print 
