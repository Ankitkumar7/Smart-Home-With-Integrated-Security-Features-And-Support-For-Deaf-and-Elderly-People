
import time
def configured():
	print "Configuring  Devices", 
	for i in range(5):
		print ".",
		time.sleep(2)
	print '\nDevice is Online'
print configured()
