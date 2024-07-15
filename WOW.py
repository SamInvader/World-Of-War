"""WOW
World Of War"""

import os

os.chdir("/storage/emulated/0/WOW")

import time,random

def UPGRADE(method,team_list,percentage,host):
	
	if host in team_list.keys():
		
		team_list[host]=(team_list.get(host)+((percentage/100)*(team_list.get(host))))
		print(f"Successfully upgraded {host} by {percentage}%")
		
	else:
		
		print("{host} not in your squad")
		
	return team_list
	
def STRATEGY(method, team_list):
	
	if method=='WTS':
		
		s_team_list=sorted(team_list.items(), key=lambda x:x[1], reverse=False)
		team_list=dict(s_team_list)
		
	if method=='STW':
		
		s_team_list=sorted(team_list.items(),key=lambda x:x[1],reverse=True)
		team_list=dict(s_team_list)
		
	if method=='MXD':
		
		import random
		MXD=list(team_list.items())
		random.shuffle(MXD)
		team_list=dict(MXD)
		
	return team_list
	
def SPY(team_list,host,opp_team):
	
	team_list[host]=(team_list.get(host)-((20/100)*(team_list.get(host))))
	print("*****OPPOSITION*TEAM*****")
	
	for i,j in opp_team.items():
		
		print(f"Soldier: {i} ** Strength percentage: {j}")
		
	return team_list
	
def CREATE(team_list,host):
	
	if host in team_list.keys():
		
		print(f"Soldier {host} already exists")
		
	else:
		
		import random
		team_list[host]=random.randint(100,125)
		print(f"Soldier {host} created")
		
	return team_list
	
def FILEOPEN(file,value=0,mode='R_F'):
	
	if mode=='R_F':
		
		File=open(file,'r')
		
		return File.read()
		
	elif mode=='W_F':
		
		File=open(file,'a')
		File.write(value)
		File.close()
		
def OPP_UPGRADE(percentage,host,team):
	
	team[host]=(team.get(host)+(percentage/100 *(team.get(host))))
	
	return team
	
def COMMAND(commander_name,opp_list,opp_no,team_list,team,team_name,amount):
	
	print(f"{commander_name}: Shit what's all this")
	
	import time
	
	time.sleep(0.5)
	life=150
	print(f"BMr: Welcome to the battle commander. \nBMr: All soldiers are currently in the recuperation centre. We needed backup urgently")
	time.sleep(0.5)
	print(f"""BMr: All the best ,co~m~ma~n...,aargh f**k, lay...(line broken)
{commander_name}: BMr, d**n, line broken, s**t they're coming, how many are they PCC
PCC: There are a total of ...{opp_no} people here
{commander_name}: Thanks
PCC: Anytime(PCC shuts down)
{commander_name}: Okay let's start""")
	a=0
	attacks=['punch','kick','shoot']
	d=True
	
	while d:
		
		print(attacks)
		opp_list=OPP_DEL(opp_list)
		
		if life<=0 and len(list(opp_list))>0:
			
			print("PCC: Bad luck boss")
			print(f"""PCC: Seems like were re-establishing connection with BMr
BMr: commander,com~ come in commander
{commander_name}: (with a thick voice) Yes BMr
BMr: Commander we just defeated the coup that happened here, wait why do you sound like that
{commander_name}:We... LOST
BMr: WHAT! NO, WH...WHY""")
			time.sleep(0.5)
			print("Game Over")
			pos="lost"
			break
			
		elif life>0 and len(list(opp_list))<=0:
			
			print("PCC: That's a new territory conquered. Congratulations Boss")
			print(f"""BMr:Commander, com~~ come in commander
{commander_name}: Yeah
BMr:Good, commander we also eliminated the attempted siege
{commander_name}:Great, we also have a new territory, take care of all casualties
(Breathes in) VICTORY IS OURS""")
			pos="won"
			break
			
		elif life<=0 and len(opp_list)<=0:
			
			print("Fight again")
			life=150
			
		att=input("Which attack:")
		
		if att.lower() in attacks:
			
			if att.lower()=='punch':
				
				import random
				
				aa=random.randint(0,35)
				b=random.choice(list(opp_list.keys()))
				opp_list[b]-=aa
			elif att.lower()=='kick':
				
				import random
				
				aa=random.randint(0,35)
				b=random.choice(list(opp_list.keys()))
				opp_list[b]-=aa
				
			elif att.lower()=='shoot':
				
				import random
				
				aa=random.randint(10,70)
				b=random.choice(list(opp_list.keys()))
				opp_list[b]-=aa
				
			print("Life:",life)
			print("{} people left to handle".format(len(opp_list.keys())))
			
		elif att.lower()=='exp':
			
			import random
			
			aa=random.randint(90,100)
			b=random.choice(list(opp_list.keys()))
			opp_list[b]-=aa
			a+=1
			print("Life:",life)
			print("{} people left to handle".format(len(opp_list.keys())))
			
		else:
			
			print(f"{att.upper()} not possible")
			
		opp_no=len(opp_list)
		c=random.randint(0,5)
		impact=c*opp_no
		life-=impact
		print("Life:",life)
		
	SAVE_FILE(pos,team,commander_name,team_name,amount)
	FILEOPEN("gamefile.dat",'W_F')
def OPP_DEL(opplist):
	for key in opplist.keys():
		if opplist[key]<=0:
			opplist.pop(key)
			break
	return opplist
def SAVE_FILE(pos, team_list,commander,team, amount):
	file=open("gamefile.dat","a")
	import time,random,json
	date=time.asctime()
	if pos=='won':
		Input="\n"+date+"\n 1 border added "+'gluiwygl'
	else:
		Input="\n"+date+"\n 1 border removed "+"gluiwygl."
	file.write(Input)
	file.write("\nSQUAD\n")
	json.dump(team_list, file)
	file.write("\nCommander Name:"+commander+"\nTeam Name:"+team+"\n")
	file.write("You "+pos)
	file.close()
	players = open("players.dat", "w")
	json.dump (team_list, players)
	players.close ()
	money_file = open("money.dat", "w")
	json.dump(amount, money_file)
def SEP(content):
	nos='1234567890'
	nos=list(nos)
	content=list(content)
	numeric,alpha=[],[]
	for no in content:
		if no in nos:
			numeric.append(no)
		else:
			alpha.append(no)
	return alpha,numeric
def DEL(team_list):
	for key in team_list.keys():
		if team_list[key]<=0:
			del team_list[key]
			break
	return team_list
def WELCOME(commander_name,team_name):
	print(f"""Hello commander
{commander_name}:Yeah PCC, why was I summoned
PCC:We're in desperate need of a territory to keep our population under control,and naturally other commander's cant do this so we need you
{commander_name}:Well then, I'll try my best, contact the federation I need troops
PCC:Yes, that has been settled there are close to 15 soldiers ready to fight
{commander_name}:Good
""")
	print("PCC: The teams squad name is {}".format(team_name))
def GET_TEAM():
	import random,json
	sol_list={}
	soldiers=['Tom', 'Cruise', 'Jayden', 'Harry', 'Peterson', 'Parker', 'Peter', 'Jace', 'Andrew', 'Peter', 'Samuel', 'Stone', 'Lingfeng', 'JP', 'BMr']
	players = open ("players.dat","r")
	t = players.read()
	if t == "":
		for names in soldiers:
			sol_list[names]=random.randint(20,100)
	else:
		players.close()
		players = open("players.dat")
		sol_list = json.load(players)
	return sol_list
def GET_MONEY():
	import json
	money_file = open("money.dat")
	amount = json.load(money_file)
	return amount
def OPP_GET_TEAM(team_list):
	import random
	sol_list={}
	soldiers=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',"W",'X','Y','Z']
	try:
		for sol in soldiers:
			sol_list[sol]=random.randint(0,round(max(team_list.values())))
	except ValueError:
		sol_list.clear()
		for sol in soldiers:
			sol_list[sol]=random.randint(0,100)
	return sol_list
def MAIN():
	Commander = input("Commander account name:")
	import time, os, json
	exist = os.access("/storage/emulated/0/WOW/"+Commander, 1)
	if exist:
		os.chdir("/storage/emulated/0/WOW/"+Commander)
	else:
		exit("Exit with error code 001")
	print('**W**O**W***')
	time.sleep(0.5)
	print("World Of War")
	time.sleep(1)
	print("Data")
	time.sleep(0.5)
	print("KEEP CONFIDENTIAL...")
	time.sleep(0.5)
	Data=FILEOPEN('gamefile.dat',None,'R_F')
	print(Data)
	time.sleep(0.5)
	print("Click Enter to start, Press 'E' to End")
	Input=input()
	money = GET_MONEY()
	if Input.lower()=='e':
		exit()
	if Input.lower() != 'e' and Input.lower() != '':
		print("Wrong Input")
	team=GET_TEAM()
	opp_team=OPP_GET_TEAM(team)
	Team_file = open("team_name.txt")
	Team = Team_file.read()
	WELCOME(Commander,Team)
	time.sleep(0.7)
	print('Team:',team)
	while True:
		print(f"You have ${money} left")
		upgrade_option=input("LIST\n[1].Upgrade team($20)\n[2].Pick strategy\n[3]Spy on opponent($50)\n[4]Recruit soldiers($30).\n[end] to End.\nInput the things in bracket in front of it to use it\n")
		if upgrade_option=="1" and money>=20:
			money -= 20
			method=input("""Method:
[M]orale
[F]ood and Water
[C]arnal pleasures
[Mi]ndset
""")
			if method.upper()=='M':
				host=input("Which soldier:")
				team=UPGRADE('supply',team,30,host)
				print(team)
			elif method.upper()=='F':
				host=input("Which soldier:")
				team=UPGRADE('food and water',team,50,host)
				print(team)
			elif method.upper()=='C':
				host=input("Which soldier:")
				team=UPGRADE('carnal pleasures',team,-10,host)
				print(team)
			elif method.upper()=='MI':
				host=input("Which soldier:")
				team=UPGRADE('mindset',team,20,host)
				print(team)
			else:
				print("Wrong Method Input")
				print(team)
		elif upgrade_option=='2':
			print("""Which Method:
1:[WTS]Weak To Strong
2:[STW]Strong To Weak
3:[MXD]Mixed""")
			choice=input()
			if choice.upper()=='WTS':
				team=STRATEGY('WTS',team)
			elif choice.upper()=='STW':
				team=STRATEGY('STW',team)
			elif choice.upper()=='MXD':
				team=STRATEGY('MXD',team)
			else:
				print("Wrong Strategy\n")
			print('Team code:',team)
		elif upgrade_option=='3' and money>=50:
			money -= 50
			print("""Please note this will reduce the energy points from the host
Press Enter to continue or press another key to terminate""")
			Input=input()
			if Input.lower()=='':
				host=input("Which soldier:")
				if host not in team:
					print(f'{host} not in team')
					print('Team code:',team)
				else:
					team=SPY(team,host,opp_team)
			else:
				pass
			print('Team code:',team)
		elif upgrade_option=='4' and money>=30:
			money-=30
			host=input('Soldier Name:')
			team=CREATE(team,host)
			print('Team code:',team)
		elif upgrade_option.lower()=='full':
			for soldiers,prowess in team.items():
				team[soldiers]=100
			print("Team code:",team)
		elif upgrade_option.lower()=="end":
			break
		else:
			print('Wrong Input')
	m=0
	while m<5:
		opp_team=OPP_UPGRADE(random.randint(0,15),random.choice(list(opp_team.keys())),opp_team)
		m+=1
	print('All troops sent out to war')
	time.sleep(2)
	print("MESSAGE FROM BMr:Commander we have started the war")
	done=False
	while not done:
		try:
			pp=iter(team.items())
			p=next(pp)
			i=list(p)
			p=i[0]
		except:
			COMMAND(Commander,opp_team,len(opp_team.keys()),team,team,Team,money+100)
			break
		o=random.choice(list(opp_team.keys()))
		if team.get(p)>opp_team.get(o):
			time.sleep(1)
			print('Soldier {} from opponents withdraws'.format(o))
			sub=opp_team[o]//4
			opp_team[o]=0
			team[p]-=sub
			time.sleep(1)
		elif team.get(p)<opp_team.get(o):
			time.sleep(1.5)
			print("Soldier {} from your team withdraws".format(p))
			time.sleep(1)
			print("MESSAGE FROM {}: I'm sorry commander".format(p))
			sub=team[p]//4
			opp_team[o]-=sub
			team[p]=0
		else:
			team[p]-=1
			opp_team[o]-=sub
		team=DEL(team)
		opp_team=OPP_DEL(opp_team)
		if len(list(team.items()))==0 or len(list(opp_team.items()))==0:
			if len(list(team.items()))==0 and len(opp_team.keys())>0:
				print("You lost in the war")
				time.sleep(1)
				print("\n BMr: Attention commander, I...I'm sorry but we lost\n{}: I know. PCC told me\n BMr: Oh...Uhmmm Commander, pls protect the border\n{}: Sure (mutters) Useless bunch of people".format(Commander,Commander))
				COMMAND(Commander,opp_team,len(opp_team.keys()),team,team,Team,money+100)
			elif len(list(team.items()))>0 and len(opp_team.keys())==0:
				print("We won let's proceed")
				time.sleep(1)
				print("BMr: We're proceeding boss\n{}: GO".format(Commander))
				time.sleep(5)
				print("We won {} \n BMr:VICTORY IS OURS\nGame Over".format(Commander))
				SAVE_FILE('won',team,Commander,Team,money+300)
			else:
				print("Both sides suffered losses")
				time.sleep(1)
				print("PCC: All soldiers in recuperation centre no borders won")
				time.sleep(1)
				print('A truce was created')
				date=time.asctime()
				file=open("gamefile.dat",'a')
				file.write(date)
				file.write("Draw\nTruce created")
				file.close()
			break


MAIN()
while True:
	print('To continue game: Click Enter, To end click Z')
	Input=input()
	if Input=='':
		MAIN()
	elif Input.lower()=='z':
		exit()
	else:
		print('WRONG INPUT')