#start a mini project console ERP system.
employees={}
while True:
	print("Press 1 for add employee")
	print("Press 2 for delete employee ")
	print("Press 3 for search employee")
	print("Press 4 for display  employee")
	print("Press 5 for change employee details")
	print("Press 6 for Quit")
	ch = int(input("Enter choice"))
	if ch == 1:
	#adding employee
		employee_id = input("\tenter Employee id ")
		if employee_id not in employees.keys():
			name = input("\tenter name ")
			age = int(input("\tenter age "))
			gender = input("\tenter the gender ")
			place = input("\tenter place ")
			salary = int(input("\tenter salary "))
			previous_company = input("\tenter your previous company ")
			joining_date = input("\tenter joining date ")
			temp ={
				"name":name,
				"age":age,
				"genter":gender,
				"place":place,
				"salary":salary,
				"previous_company":previous_company,
				"joining_date":joining_date,
				}
			employees[employee_id] = temp
		else:
			 print("\tEmployee id  already Taken")
	elif ch == 2:
	#delete
		eid = input("\tEnter employee id") 
		if eid not in employees.keys():
			print("\tWrong Employee id")
		else:
			del employees[employee_id]
	elif ch == 3:
	#search
		name = input("\tEnter name")
		found = False
		for i in employees.values():
				if i["name"] == name: 
					print(f"\t{i['name']} | {i['age']} | {i['place']} | {i['gender']} | {i['previous_company']} | {i['salary']} ")
					found = True
					break
		if found==False:
			print("\tnot in the list")
	elif ch == 4:
		for id,employee in employees.items():
			print(f"\t{id} | {employee['name']} | {employee['age']} | {employee['place']} | {employee['gender']} | {employee['previous_company']} | {employee['salary']} ")
	elif ch== 5:
		print("Enter 1 for change name")
		print("Enter 2 for change age")
		print("Enter 3 for change gender")
		print("Enter 4 for change salary")
		cho =int(input("\tEnter your choice."))
		employee_id = input("\tEnter employee id.")
		if cho == 1:
			employees[employee_id]['name'] = input("\tEnter new name") 
		elif cho == 2:
			employees[employee_id]['age'] = int(input("\tEnter new age"))
		elif cho == 3:
			employees[employee_id]['gender'] = input("\tEnter gender")
		elif cho == 4:
                        employees[employee_id]['salary'] = int(input("\tEnter new salary"))
		else:
			print("invalid choice!!")
	elif ch == 6:
		break;
	else:
		print("Invalid Choice")



