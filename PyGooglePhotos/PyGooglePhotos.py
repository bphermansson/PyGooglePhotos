import sys
from pydrive.auth import GoogleAuth 
from pydrive.drive import GoogleDrive

#settings_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.yaml')
settings_file = "settings.yaml"

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
	  print 'Folder: %s' % (file1['title'])
