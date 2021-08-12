#create a small fruit shop software

fruit=[]
while True:
	print("1 add fruit ")
	print("2 delete fruit by name ")
	print("3 search  fruit by name and rate ")
	print("4 change  fruit name ")
	print("5 display ")
	print("6 exit ")        
	choice =int(input("enter your choice"))
	if choice == 1:
	#add fruit
		name=input("enter the fruit name")
		rate=int(input("enter the rate"))
		if name!=None and rate !=None:
			fruit.append([name,rate])
	elif choice == 2:
		#delete fruits by name
		name=input("enter the fruit name you want to delete ")
		for i in fruit:
			if i[0]==name:
				fruit.remove(i)
	elif choice ==3:
		#search fruit by name and rate
		name=input("enter the fruit name you want to search")
		rate=input("enter the fruit rate you want to search")
		for i in fruit:
			if i[0]== name and i[1]==rate:
				print("found")
			else:
				print("not found")
	elif choice ==4:
                #change fruit  name and rate
                name=input("enter the fruit name you want to change")
                rate=int(input("enter the fruit rate you want to change"))
                new_name=input("enter the new name ")
                new_rate=int(input("enter new rate"))
                for i in fruit:
                	if i[0]==name and i[1]==rate:
                		fruit.remove(i)
                		fruit.append([new_name,new_rate])
                		print(fruit)
	elif choice==5:
	#display
		print(fruit)
	elif choice==6:
		break;
	else:
		print("invalid")



