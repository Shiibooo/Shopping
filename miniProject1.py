#define the list of items
dairy = {"Milk": 2.30,"Butter": 4.50, "Eggs": 3.40, "Cheese Slices": 3.15,
         "Evaporated Milk Creamer": 1.40, "Milo": 12.50, "Biscuits": 5.30, "Yogurt": 0.95}
packaged_goods = {"Bread": 2.70, "Cereal ": 7.00, "Crackers": 3.10, "Chips": 2.60,
                  "Raisin": 2.10, "Nuts": 2.00, "Green Bean": 1.05, "Barley": 1.05}
canned_goods = {"Tomato": 1.45, "Button Mushroom": 1.15, "Baking Bean": 1.35, "Tuna Fish": 1.45,
                "Kernel Corn": 1.25, "Sardine Fish": 1.10, "Chicken Luncheon Meat": 1.95, "Pickled Lettuce": 0.95}
condiments_sauces = {"Fine Salt": 0.80, "Sea Salt Flakes": 1.30, "Chicken Stock": 3.15, "Chili Sauce": 2.65,
                     "Oyster Sauce": 4.50, "Sweet Soy Sauce": 3.75, "Tomato Ketchup": 3.20, "Sesame Oil": 4.95}
drinks_and_beverages = {"Green Tea Canned 330ML": 15.00, "Blackcurrent Ribena 330ML": 31.00, "100 Plus 24 Cans": 15.00,
                        "Orange Cordial 2 Litre": 3.90, "Mineral Water 24 x 600ML": 7.00, "Pineapple Juice": 0.80, "Nescafe Coffee": 9.90, "Coke 24 cans": 12.40}
shopping_menu= dairy|packaged_goods|canned_goods|condiments_sauces|drinks_and_beverages

#list to show the user data
user_shopping_list_dict={}
#boolean to check for discount
discount = False

print("#########################")
print("##### SHOPPING LIST #####")
print("#########################")

#main
def main():
    print("\nPlease input the number of the action that you would like to do.")
    print("1. View shopping list" '\n' 
          "2. Add item to shopping cart" '\n' 
          "3. Remove item from shopping cart" '\n' 
          "4. View your shopping cart" '\n' 
          "5. Go to checkout" '\n' 
          "6. Exit\n")
    #get input
    action = int(input("Please input the action number: "))

    #check input and runs corresponding functions
    while True:
        #view the shopping list
        if action == 1:
            action1()
        #add items to the cart
        elif action == 2:
            action2()
        #remove items from the shopping cart
        elif action == 3:
            action3()
        #view cart
        elif action == 4:
            action4()
        #checkout
        elif action == 5:
            action5()
        #exit from the code if 6 is pressed
        elif action == 6:
            break
        #ask for an input when the numebr is pressed wrongly
        else:
            print('Invalid number, please try again')
            main()

#ask for user input for how the data is shown
def action1():
    print("Do you want to display shopping list according to category, alphabetical order or in ascending price?")
    displayOption =input("Please input C for category, A for alphabetical order and P for ascending price:")
    if displayOption == 'c':
        action1_category()
        main()
    else:
        main()

#print out items based on category
def action1_category():
    i = 1
    print("***DAIRY***")
    for key in dairy:
        print(i,'%s - $%.2f' % (key, dairy[key]))
        i= i+1
    print()

    print("***PACKAGED GOODS***")
    for key in packaged_goods:
        print(i, '%s - $%.2f' % (key, packaged_goods[key]))
        i= i+1

    print()

    print("***CANNED GOODS***")
    for key in canned_goods:
        print(i, '%s - $%.2f' % (key, canned_goods[key]))
        i= i+1

    print()

    print("***CONDIMENTS/SAUCES***")
    for key in condiments_sauces:
        print(i, '%s - $%.2f' % (key, condiments_sauces[key]))
        i= i+1

    print()

    print("***DRINKS AND BEVERAGES***")
    for key in drinks_and_beverages:
        print(i, '%s - $%.2f' % (key, drinks_and_beverages[key]))
        i= i+1

    print()

#Add items
def action2():

    #prints all of the items in the store
    action1_category()

    global qlist
    qlist=[]
    while True:
        num=input('Key the number of the item you would like to get [item (no.)]: ')
        global q
        q=int(input('Key the number of the items you would like: '))
        user_shopping_list_dict.append('{} x {}'.format(q,num))
        total_price.append(q*shopping_menu.get(num))
        choice=input('Would you like to add more things to your cart?(y/n) ')
        if choice == 'y':
            action4()
            continue
        elif choice == 'n':
            main()
            #break

#Remove items
def action3():

    #uses action4 function to print the list of items that are in the cart of the user
    action4()

    while True:
        print('\nBe warned that all quantities of the item would be removed\n')
        delete=int(input('Key in the number that you would like to remove'
                         '(1 being the first item in the list)  : '))
        user_shopping_list_dict.remove(user_shopping_list_dict[delete-1])
        total_price.remove(total_price[delete-1])
        choice=input('Would you like to delete more things from your cart?(y/n) ')
        if choice == 'y':
            action4()
            #print(user_shopping_list_dict)
            continue
        else:
            main()
            #break

#View Shopping cart
def action4():
    print("Price without GST\n")
    #print(user_shopping_list_dict)
    for key, value in user_shopping_list_dict.items():
        print(key, "price: "+ str(value) )
    main()

#Go to checkout
def action5():

    discountCheck = input("Do you have a discount y/n")

    if(discountCheck == "y"):
        discount = True
    else:
        discount = False
    totalCost = 0

    #calculate total cost before GST and discount
    for key, value in user_shopping_list_dict.items():
        totalCost = totalCost + value

    #cost of item with GST
    print("\nprice with GST")
    for key, value in user_shopping_list_dict.items():
        print(key, " price:"+ str(value *1.07) )

    #print total cost
    print("\ntotal cost including GST:" + str(totalCost*1.07))

    #total discount
    if (discount == True):
        print("\nDiscount amount:" + str(totalCost*.1))

    #total GST
    print("\nGST amount:" + str(totalCost * 0.07))

    main()

#function to return back to main screen
def exitToMain():
    print("exited to main")
    main()

#call main in order to access the rest of the codes
main()