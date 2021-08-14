#create a small fruit shop software

fruit={}
cart=[]

def main_menu():
	print("1 add fruit details ")
	print("2 delete fruit  ")
	print("3 search  fruit details ")
	print("4 change  fruit name and rate")
	print("5 display fruit details")
	print("6 add to cart")
	print("7 display cart")
	print("8 exit ")
    
def add_fruit():
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
def delete_fruit():
	fid = int(input("\tEnter fruit id"))
	if fid not in fruit.keys():
		print("\tWrong fruit id")
	else:
		del fruit[fid]
def search_fruit():
	name=input("enter the fruit name you want to search")
	rate=input("enter the fruit rate you want to search")
	found = False
	for i in fruit.values():
		if i["fruit_name"] == name and i["rate"] == rate:
			print("We found!!")
			found = True
			break
		if(found == False):
			print("Not Found!!!!")
def display_fruit_details():
	print(fruit)
	#for fruit_id,f in fruit.item():
		#print("\n\tfruit id:\t{}".format(fruit_id))
		#for key,value in fruit.item():
			#print("\t{}:\t{}".format(key,value))
def add_to_cart():
	print(fruit)
	#for fruit_id,f in fruit.item():
	
		#print("\t{}\t{}\t{}\t{}\t{}".format(fruit_id,f['name'],fruit['rate']))
	fruit_id=int(input("Enter the fruit id to add the item to cart:"))
	if fruit_id in fruit.keys():
		cart.append(fruit[fruit_id])
def display_cart():
	print(cart)
	#for fruit in cart:
	#	print("\n")
	#	for key,value in fruit.item():
	#		print("\t{}:\t{}".format(key,value))

#def change_fruit_menu():
#	print("\t1. Change fruit id")    
#	print("\t2. Change fruit name")
#	print("\t3. Change fruit rate")
#	print("\t4. Change imported from")
#	print("\t5. Change import date")
#	print("\t6. Change bought price")
#	print("\t7. exit")
	
#def change_fruit_id():
#	fruit_id=int(input("\t Enter the fruit id "))
#	if fruit_id in fruit.keys():
#		new_id=int(input("\t Enter the new fruit id "))
		#new_id=int(input("\t Enter new fruit id for {}: ".format(fruit[fruit_id][fruit_name])))
#		fruit[new_id]=fruit[fruit_id]
#		del fruit[fruit_id]
#	else:
#		print("\t Wrong fruit id")
#def change_fruit_name():
#	fruit_id=int(input("\tEnter the fruit id "))
#	if fruit_id in fruit.keys():
#		new_name=input("\t Enter the new_name ")
#		fruit[fruit_id]["name"]=new_name
#	else:
#		print("\t invalid")
#def change_import_from():
#	fruit_id=int(input("\t Enter the fruit_id "))
#	if fruit_id in fruit.keys():
#		new_imp_frm=input("\tEnter the new value for import_from ")
#		fruit[fruit_id]["imported_from" ]=new_imp_frm
#	else:
#		print("\t Invalid")
#def change_import_date():
#	fruit_id=int(input("\t Enter the fruit_id "))
#	if fruit_id in fruit.keys():
#		new_imp_date=input("\tEnter the new value for import_date ")
#		fruit[fruit_id]["imported_date" ]=new_imp_date
#	else:
#		print("\t Invalid")
#def change_buy_price():
#	fruit_id=int(input("\t Enter the fruit_id "))
#	if fruit_id in fruit.keys():
#		new_price=input("\tEnter the new value for buy price  ")
#		fruit[fruit_id]["buy_price" ]=new_price
#	else:
#		print("\t Invalid")


def change_fruit_details():
	print(fruit)
	c = int(input('Enter fruit id : '))
	if c not in fruit.keys():
		print('Please provide right fruit id ')
	else:
		print('modify fruit data')
		fruit[c]['fruit_name'] = input('Enter new fruit name :')
		fruit[c]['rate'] =input('Enter new rate : ')
#while True:
#	change_fruit_menu()
#		
#	ch = int(input("Enter your choice: "))
#	if ch == 1:
        #change fruit id
#		change_fruit_id()
#	elif ch == 2:
#       #fruit_name
#		change_fruit_name() 

#	elif ch == 3:
        #change fruit rate
#		change_fruit_rate()
#	elif ch==4:
	#change imported from
#		change_imported_from()
#	elif ch==5:
	#change import date
#		change_import_date()
#	elif ch==6:
	#change buy price
#		change_buy_price()
#	elif ch==7:
	#exit
#		break;
#	else:
#		print("invalid")	

while True:
	main_menu()   
	choice =int(input("Enter your choice"))
	if choice ==1:
	##add fruit
		add_fruit()

	elif choice == 2:
		#delete fruits by name
		delete_fruit()
	elif choice ==3:
		#search fruit details
		search_fruit()
	elif choice ==4:
                #change fruit  details
		change_fruit_details()
	elif choice==5:
	#display
		display_fruit_details()
	elif choice==6:
	#add to cart

		add_to_cart()
	elif choice==7:
	#display cart
		display_cart()
	elif choice==8:
		break;
	else:
		print("invalid")



