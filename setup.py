from pathlib import Path
import time,json
begin_time=time.time()
pathname=r"/storage/emulated/0/WOW"
user = input("Commander account to create or reset:")
team_name = input("Team name:")
pathnam=Path(pathname)
import os
if pathnam.exists():
	os.chdir(r"/storage/emulated/0/WOW")
	try:
		os.mkdir(user)
	except FileExistsError:
		os.chdir("/storage/emulated/0/WOW/"+user)
		listoffiles = os.listdir()
		for files in listoffiles:
			os.unlink(files)
	os.chdir(r"/storage/emulated/0/WOW/"+user)
	filename="gamefile.dat"
	path=pathname+filename
	p=Path(path)
	if p.exists():
		new_file=open(filename, 'w')
		new_file.write('')
		new_file.close()
		print(f"Successfully reseted '{filename}'")
		players = open("players.dat", 'w')
		players.write ('')
		players.close ()
		money = open ("money.dat","w")
		money.write ("200")
		money.close ()
		team = open ("team_name.txt", "w")
		json.dump(team_name, team)
		team.close ()
	else:
		new_file=open(filename, 'w')
		new_file.close()
		print(f"Successfully created '{filename}'")
		players = open("players.dat", 'w')
		players.write ('')
		players.close ()
		money = open("money.dat","w")
		money.write("200")
		money.close()
		team = open ("team_name.txt", "w")
		team.write (team_name)
		team.close ()
else:
	os.chdir(r"/storage/emulated/0")
	os.mkdir(r'/WOW')
	os.chdir(r"/storage/emulated/0/WOW")
	os.mkdir(user)
	os.chdir("/storage/emulated/0/WOW"+user)
	new_file=open('gamefile.dat','w')
	print("Successfully initialized 'gamefile.dat'")
	new_file.close()
	players = open("players.dat", 'w')
	players.write ('')
	players.close ()
	money = open("money.dat","w")
	money.write("200")
	money.close()
	team = open ("team_name.txt", "w")
	team.write (team_name)
	team.close ()
end_time=time.time()
time_taken=round(end_time-begin_time, 2)
print("Process Completed\nTime taken>>>"+str(time_taken),"secs")
