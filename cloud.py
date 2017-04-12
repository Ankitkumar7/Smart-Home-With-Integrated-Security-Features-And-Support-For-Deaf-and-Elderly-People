import dropbox
import serial
# Get your app key and secret from the Dropbox developer website
def dropboxConnection(app_key, app_secret):
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    authorize_url = flow.start()
    # Have the user sign in and authorize this token
    authorize_url = flow.start()
    print '1. Go to: ' + authorize_url
    print '2. Click "Allow" (you might have to log in first)'
    print '3. Copy the authorization code.'
    code = raw_input("Enter the authorization code here: ").strip()
    # This will fail if the user enters an invalid authorization code
    access_token, user_id = flow.finish(code)
    client = dropbox.client.DropboxClient(access_token)
    return 'linked account: ', client.account_info()

def uploadFile(filename):
    f = open(filename, 'rb')
    response = client.put_file(filename, f)
    print "uploaded:", response

    
#call this function
dropboxConnection('6fx149gb0lwt2md', '8ea9779uv3d7fd4')

arduinoSerialData = serial.Serial('com10',9600)

if __name__ == '__main__':
    print 'Welcome To Modulo Smart Home System | Door Alert System For Deaf "DAD"'
    initateProgram = int(raw_input("Enter 1 to initate the program: "))
    if initateProgram == 1:
        print 'Checking device status'
        try:
            if (arduinoSerialData.inWaiting() > 0):
                myData = arduinoSerialData.readline()
                print 'Device is ready'
        except SerialException:
            print 'Device not ready'
        
            



        
