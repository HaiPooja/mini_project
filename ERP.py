#start a mini project console ERP system.
employee=[]
while True:
	print("1 add employee ")
	print("2 delete employee ")
	print("3 search  employee ")
	print("4 change  employee data ")
	print("5 display ")
	print("6 exit ")
	choice=int(input("enter your choice"))
	if choice ==1:
		#add employee
		name=input("enter name ")
		if name != None:
			employee.append(name)
	if choice ==2:
		#delete
		print(employee)
		print("choose name from this ")
		name=input("enter name to delete ")
		employee.remove(name)
	elif choice==3:
		#search
		name=input("enter the name to search ")
		if name in employee:
			print(str(name)+" is in the lise")
		else:
			print(str(name)+" is not in the list")
	elif choice==4:
		#change employee
		name=input("enter the name to be change ")
		index=employee.index(name)
		new_name=input("enter new name ")
		employee[index]=new_name
	elif choice==5:
		#display
		print(employee)
	elif choice==6:
		break;
	


