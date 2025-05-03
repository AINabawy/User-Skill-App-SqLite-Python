import sqlite3

user_message = """
What do you want to do?
's' ->Show all skills
'a' ->Add new skill
'u' ->Update skill progress
'd' ->Delete a skill
'q' ->Quit the append
Choose an option:"""

#CREATE DATABASE AND CONNECT
db = sqlite3.connect("app.db")

#SETTING UP THE CURSOR
cr = db.cursor()

#CREATE TABLE
cr.execute("CREATE TABLE IF NOT EXISTS skills(skill TEXT,progress TEXT,user_id KEY)")
cr.execute("CREATE TABLE IF NOT EXISTS names(name TEXT,user_id KEY)")



#USERS DATA DICT
data = {'Ali':{'PHP':'70%','CSS':'80%','JAVA SCRIPT':'90%'},
'Nabawy':{'PYTHON':'70%','C++':'80%','C':'90%'}}

#DEFINE THE METHODES 

def addData():
	for i,name in enumerate(data):
		#print(f"INSERT into names Values('{name}',{i+1})")
		cr.execute(f"INSERT into names Values('{name}',{i+1})")
		for skill in data[name]:
			#print(f"INSERT into skills Values('{skill}',{data[name][skill]},{i+1})")
			cr.execute(f"INSERT into skills Values('{skill}','{data[name][skill]}',{i+1})")

def show_skills(user_id):
	#SHOW SKILLS
	cr.execute(f"SELECT *FROM skills WHERE user_id ='{user_id}'")
	results=cr.fetchall()
	print(f"You have {len(results)} skills.")
	for row in results:
		print(f"Skill ->{row[0]}",end="\t")
		print(f"Progress ->{row[1]}")
	
	
def add_skill(user_id,skill,progress):
	cr.execute(f"INSERT into skills Values('{skill}','{progress}',{user_id})")
	print("Skill has been added.")
	
def update_progress(user_id,skill,progress):
	cr.execute(f"UPDATE skills SET progress='{progress}' WHERE user_id={user_id} AND skill='{skill}' ")
	print("Skill has been updated.")
	
	
def	delete_skill(user_id,skill):
	cr.execute(f"DELETE FROM skills WHERE user_id={user_id} AND skill='{skill}'")
	print("Skill has been deleted.")
	
def close_db():
	#SAVE
	db.commit()
	#CLOSE DATABASE
	db.close()
	print("Database closed")
	


options=['s','a','u','d','q']

counter=0


while counter <= 5:
	user_input = input(user_message).strip().lower()

	if user_input in options:
		print("Your command \'%c\' is found."%user_input)
		user_id = input("Please Enter your Id: ")
		
		if user_input == options[0]:
			show_skills(user_id)
		elif user_input == options[1]:
			sk=input("Please enter the skill name: ").strip().capitalize()
			prog=input("Please enter the progress: ")
			add_skill(user_id,sk,prog)
		elif user_input == options[2]:
			sk=input("Please enter the skill name: ").strip().capitalize()
			prog=input("Please enter the progress: ")
			update_progress(user_id,sk,prog)
		elif user_input == options[3]:
			sk=input("Please enter the skill name: ").strip().capitalize()
			delete_skill(user_id,sk)
		else:
			print("App is closed.")
			
		close_db()
		break
	else:
		if counter==5:
			print("You have no tries")
		else:
			print(f"This command \"{user_input}\" not found.Try again")
		counter+=1


		
