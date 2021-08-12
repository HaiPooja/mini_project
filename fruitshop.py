#create a small fruit shop software

fruit={}
cart=[]
while True:
	print("1 add fruit details ")
	print("2 delete fruit  ")
	print("3 search  fruit details ")
	print("4 change  fruit name and rate")
	print("5 display fruit details")
	print("6 add to cart")
	print("7 display cart")
	print("8 exit ")        
	choice =int(input("Enter your choice"))
	if choice ==1:
	##add fruit
		fruit_id = int(input("\tEnter Fruit_id "))
		if fruit_id not in fruit.keys():
			fruit_name = input("\tEnter name ")
			rate= int(input("\tEnter rate "))
			imported_from = input("\tEnter the imported from ")
			import_date = input("\tEnter import_date ")
			buying_price = int(input("\tEnter buying_price "))
			temp ={
				"fruit_name":fruit_name,
				"rate":rate,
				"imported_from":imported_from,
				"import_date":import_date,
				"buying_price":buying_price,
			}
			fruit[fruit_id] = temp
		else:
			print("\tfruit id  already Taken")

	elif choice == 2:
		#delete fruits by name
		fid = input("\tEnter fruit id") 
		if fid not in fruit.keys():
				print("\tWrong fruit id")
		else:
				del fruit[fid]
	elif choice ==3:
		#search fruit details
		name=input("enter the fruit name you want to search")
		rate=input("enter the fruit rate you want to search")
		found = False
		for i in fruit.values():
			if i["fruit_name"] == name and i["rate"] == rate:
				print("found!!")
				found = True
				break
		if(found == False):
				print("Not found")
	elif choice ==4:
                #change fruit  details
                print(fruit)
                c = int(input("Enter fruit id :"))
                if c not in fruit.keys():
                	print('Please provide right fruit id ')
                else:
                	print("modify fruit data")
                	fruit[c]['fruit_name'] = input('Enter new fruit name :')
                	fruit[c]['rate'] =input('Enter new rate : ')
	elif choice==5:
	#display
		print(fruit)
	elif choice==6:
	#add to cart
		for i in fruit.keys():
			print(f"press {i} for add to cart")
		cart.append(fruit[int(input('enter fruit id to add on cart : '))])
	elif choice==7:
	#display cart
		print(cart)
	elif choice==8:
		break;
	else:
		print("invalid")



