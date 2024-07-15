import os
os.chdir("/storage/emulated/0/WOW")
account = input("Name of account to delete:")
exist = os.access("/storage/emulated/0/WOW/"+account, 1)
if exist:
	os.chdir("/storage/emulated/0/WOW/"+account)
	files = os.listdir()
	for file in files:
		os.remove(file)
	os.chdir("/storage/emulated/0/WOW")
	os.rmdir(account)
	print("Done")
else:
	exit("Error with error code 001")
