import sys
import time
from pydrive.auth import GoogleAuth 
from pydrive.drive import GoogleDrive
from PIL import Image, ImageTk
#import ImageTk
from Tkinter import Tk, Label

"""
Upload changes to Github:
git commit PyGooglePhotos.py
git push origin master
Update from Github
git pull

apt-get install python-imaging-tk
pip2 install pillow
"""

def keyinput():
	if key.upper() == 'Q':
		print "Exit"
		sys.exit()
	
def main():
	settings_file = "settings.yaml"
	photos=[]
	gauth = GoogleAuth(settings_file=settings_file)
	gauth.CommandLineAuth()
	drive = GoogleDrive(gauth)

	print "All files in root:"
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
	folder_id="1efl45Zs9_cFLEXzRERqqxIQp3Q" # 
	print "List files in folder 2016"

	_q = {'q': "'{}' in parents and trashed=false".format(folder_id)}
	photolist = drive.ListFile(_q).GetList()
	for file1 in photolist:
		#print 'title: %s, id: %s' % (file1['title'], file1['id'])
		#print 'mime: %s' % (file1['mimeType'])
		if file1['mimeType'] == "image/jpeg":
			imageurl = file1['title']
			imageid =  file1['id']
			#print 'title: %s' % (file1['title'])
	print "Open " + str(imageurl) + " id: " + str(imageid)

	# Download and show an image
	myFile = drive.CreateFile({'id': imageid})
	myFile.GetContentFile(imageurl)
	print '%s downloaded ' %(imageurl) + " and it looks like this:"
	# Create fullscreen window
	root = Tk() 
	root.overrideredirect(True)
	root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
	# Keyboard input
        root.bind('<Key>', keyinput)
	# Screen size?
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	#print str(screen_width) + "-" + str(screen_height)

	image = Image.open(imageurl)
	width, height = image.size
	#print str(width) + "-" + str(height)
	image = image.resize((screen_width, screen_height), Image.ANTIALIAS) 
	img = ImageTk.PhotoImage(image)
	
	panel = Label(root, image = img)
	panel.pack(side = "bottom", fill = "both", expand = "yes")
	root.mainloop()
	time.sleep(10)
if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      # Exit
      sys.exit()
