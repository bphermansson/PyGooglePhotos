import sys
from pydrive.auth import GoogleAuth 
from pydrive.drive import GoogleDrive
from PIL import Image

#settings_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.yaml')
settings_file = "settings.yaml"

photos=[]

gauth = GoogleAuth(settings_file=settings_file)
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

# Auto-iterate through all files that matches this query
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

print "List folders"
for file1 in file_list:
  #print 'title: %s, id: %s' % (file1['title'], file1['id'])
  #print 'mime: %s' % (file1['mimeType'])	
  if file1['mimeType'] == "application/vnd.google-apps.folder":
	if file1['title'] == "Google Photos":
		print "Found your photos:"
		print 'Folder: %s, Id: %s' % (file1['title'],file1['id'])
		found = True

if found == False:
	print "Error, no Google Photos folder found"
	sys.exit()

# Google Photos folder id =1Q4Xk107tDLn4SdoHOqZwy5AGyvIm2bNO1uubxlMqx34
# (found above)
#folder_id="1Q4Xk107tDLn4SdoHOqZwy5AGyvIm2bNO1uubxlMqx34"
#title: 2016, id: 1efl45Zs9_cFLEXzRERqqxIQp3Q
folder_id="1efl45Zs9_cFLEXzRERqqxIQp3Q" # List files in folder 2016

_q = {'q': "'{}' in parents and trashed=false".format(folder_id)}
photolist = drive.ListFile(_q).GetList()
for file1 in photolist:
	#print 'title: %s, id: %s' % (file1['title'], file1['id'])
	#print 'mime: %s' % (file1['mimeType'])
	if file1['mimeType'] == "image/jpeg":
		imageurl = file1['title']
		imageid =  file1['id']
		print 'title: %s' % (file1['title'])
print "Open " + str(imageurl) + " id: " + str(imageid)

# Download and show an image
myFile = drive.CreateFile({'id': imageid})
myFile.GetContentFile(imageurl)
print '%s downloaded ' %(imageurl) + " and it looks like this:"
image = Image.open(imageurl)
image.show()