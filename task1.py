name = input("Enter your Name: ")
ph_no = int(input("Enter phone number: "))
customer = (name,ph_no)

menu = {
  "Meat Roll" : 35,
  "Burger" : 90,
  "Mango Shake" : 75,
  "Chocolate Falooda" : 100,
  "Loaded Fries" : 80
}

print("\t\t Menu \t\t")
for i in menu:
  print(i," - ",menu[i],"₹")

print("Pick 2 items...........")
total_items  = {}
for i in range(2):
  item = input(f"Enter item {i+1}: ")
  qty = int(input("Quantity: "))
  total_items[item] = qty 

total=0
print("\t\t BILL \t\t")
print("Customer: ",customer)
for key in total_items:
  item_total = menu[key]*total_items[key]
  print(key,' x ',total_items[key],' = ',item_total," ₹ ")
  total+=item_total

print("Total: ",total,"₹")