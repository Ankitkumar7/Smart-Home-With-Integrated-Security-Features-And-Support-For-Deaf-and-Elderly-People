####################################################
# Author: Keerthana T, Ann Martin, Ankit kumar
# Script: trackingVisitor.py
from peewee import *
import serial
import sys
from dateTime import timeFormat, dateFormat
import pyscreenshot as ImageGrab
db = SqliteDatabase('people.db')

class Visitor(Model):
    image = CharField()
    date = CharField()
    time = CharField()

    class Meta:
        database = db

class login(Model):
	username = CharField()
	password = CharField()
	class Meta:
		database = db
def screenShot():
    im=ImageGrab.grab()
    im.save('d:\\ankit.jpg')

print "*"*70
print "\t\t\tWelcome To Door Alert System"
print "*"*70
try:
    db.create_tables([Visitor, login])
except OperationalError:
    print 'Table already exists'
db.connect()
try:
    arduinoSerialData = serial.Serial('com11',9600)
except serial.serialutil.SerialException:
    print "Please connect device"

while True:
    print("\t\t\t1. Register")
    print("\t\t\t2. Login")
    choices = raw_input("\t\tEnter your choice (1 or 2): ")
    choices = int(choices)
    if choices == 1:
        usr = raw_input("\t\tEnter username: ")
        pwd = raw_input("\t\tEnter password: ")
        newUser = login(username=usr, password=pwd.encode('base64','strict'))
        newUser.save()
        print "--> Message: Registration completed"
    if choices == 2:
        getUsername = raw_input("\t\tEnter your username: ").strip()
        getPassword = raw_input("\t\tEnter your password: ").strip()
        for user in login.select():
            if user.username == getUsername and user.password.decode('base64','strict') == getPassword:
                print "--> Message: Login successfull"
                print "\t\t\tFunction"
                print "\t\t\t1. Initate Program"
                print "\t\t\t2. Terminate Program"
                programChoice = raw_input("\t\tEnter your choice: ")
                programChoice = int(programChoice)
                if programChoice == 1:
                    try:
                        while True:
                            if (arduinoSerialData.inWaiting() > 0):
                                myData = arduinoSerialData.readline()
                                print "Movement at the door"
                                
                    except (NameError, serial.serialutil.SerialException):
                        print "--> Message: Device offline"
                if programChoice == 2:
                    sys.exit()
                print "--> Message: Program Terminated"
        else:
            print '--> Message: Access denied'
                
