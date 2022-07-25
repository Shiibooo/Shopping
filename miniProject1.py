#define the list of items
dairy = {"Milk (1)": 2.30,"Butter (2)": 4.50, "Eggs (3)": 3.40, "Cheese Slices (4)": 3.15,
         "Evaporated Milk Creamer (5)": 1.40, "Milo (6)": 12.50, "Biscuits (7)": 5.30, "Yogurt (8)": 0.95}

packaged_goods = {"Bread (9)": 2.70, "Cereal (10)": 7.00, "Crackers (11)": 3.10, "Chips (12)": 2.60,
                  "Raisin (13)": 2.10, "Nuts (14)": 2.00, "Green Bean (15)": 1.05, "Barley (16)": 1.05}

canned_goods = {"Tomato (17)": 1.45, "Button Mushroom (18)": 1.15, "Baking Bean (19)": 1.35, "Tuna Fish (20)": 1.45,
                "Kernel Corn (21)": 1.25, "Sardine Fish (22)": 1.10, "Chicken Luncheon Meat (23)": 1.95, "Pickled Lettuce (24)": 0.95}

condiments_sauces = {"Fine Salt (25)": 0.80, "Sea Salt Flakes (26)": 1.30, "Chicken Stock (27)": 3.15, "Chili Sauce (28)": 2.65,
                     "Oyster Sauce (29)": 4.50, "Sweet Soy Sauce (30)": 3.75, "Tomato Ketchup (31)": 3.20, "Sesame Oil (32)": 4.95}

drinks_and_beverages = {"Green Tea Canned 330ML (33)": 15.00, "Blackcurrent Ribena 330ML (34)": 31.00, "100 Plus 24 Cans (35)": 15.00,
                        "Orange Cordial 2 Litre (36)": 3.90, "Mineral Water 24 x 600ML (37)": 7.00, "Pineapple Juice (38)": 0.80, "Nescafe Coffee (39)": 9.90, "Coke 24 cans (40)": 12.40}

shopping_menu= dairy|packaged_goods|canned_goods|condiments_sauces|drinks_and_beverages

#list to show the user data
total_price=[]
user_shopping_list=[]

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

    action = int(input("Please input the action number: "))

    while True:
        if action == 1:
            action1()
        elif action == 2:
            action2()
        elif action == 3:
            action3()
        elif action == 4:
            action4()
        elif action == 5:
            action5()
        elif action == 6:
            action6()
        else:
            print('Invalid number, please try again')




#ask for user input for how the data is shown
def action1():
    print("Do you want to display shopping list according to category, alphabetical order or in ascending price?")
    input("Please input C for category, A for alphabetical order and P for ascending price:")

#print out items based on category
def action1_category():
    print("***DAIRY***")
    for key in dairy:
        print('%s - $%.2f' % (key, dairy[key]))
    print()

    print("***PACKAGED GOODS***")
    for key in packaged_goods:
        print('%s - $%.2f' % (key, packaged_goods[key]))
    print()

    print("***CANNED GOODS***")
    for key in canned_goods:
        print('%s - $%.2f' % (key, canned_goods[key]))
    print()

    print("***CONDIMENTS/SAUCES***")
    for key in condiments_sauces:
        print('%s - $%.2f' % (key, condiments_sauces[key]))
    print()

    print("***DRINKS AND BEVERAGES***")
    for key in drinks_and_beverages:
        print('%s - $%.2f' % (key, drinks_and_beverages[key]))
    print()

#Add items
def action2():
    action1_category()
    global qlist
    qlist=[]
    while True:
        num=input('Key the number of the item you would like to get [item (no.)]: ')
        global q
        q=int(input('Key the number of the items you would like: '))
        user_shopping_list.append('{} x {}'.format(q,num))
        total_price.append(q*shopping_menu.get(num))
        choice=input('Would you like to add more things to your cart?(y/n) ')
        if choice == 'y':
            continue
        elif choice == 'n':
            main()
            #break

#Remove items
def action3():
    print(user_shopping_list)
    while True:
        print()
        print('Be warned that all quantities of the item would be removed')
        print()
        delete=int(input('Key in the number that you would like to remove'
                         '(1 being the first item in the list)  : '))
        user_shopping_list.remove(user_shopping_list[delete-1])
        total_price.remove(total_price[delete-1])
        choice=input('Would you like to delete more things from your cart?(y/n) ')
        if choice == 'y':
            print(user_shopping_list)
            continue
        else:
            main()
            #break

#View Shopping cart
def action4():
    print(user_shopping_list)

#Go to checkout
def action5():
    print("action 5")

#exit code
def action6():
    print("action 6")

#call main in order to access the rest of the codes
main()







#commented out
#
# main()
#
# dairy = {"Milk (1)": 2.30,"Butter (2)": 4.50, "Eggs (3)": 3.40, "Cheese Slices (4)": 3.15,
#          "Evaporated Milk Creamer (5)": 1.40, "Milo (6)": 12.50, "Biscuits (7)": 5.30, "Yogurt (8)": 0.95}
#
# packaged_goods = {"Bread (9)": 2.70, "Cereal (10)": 7.00, "Crackers (11)": 3.10, "Chips (12)": 2.60,
#                   "Raisin (13)": 2.10, "Nuts (14)": 2.00, "Green Bean (15)": 1.05, "Barley (16)": 1.05}
#
# canned_goods = {"Tomato (17)": 1.45, "Button Mushroom (18)": 1.15, "Baking Bean (19)": 1.35, "Tuna Fish (20)": 1.45,
#                 "Kernel Corn (21)": 1.25, "Sardine Fish (22)": 1.10, "Chicken Luncheon Meat (23)": 1.95, "Pickled Lettuce (24)": 0.95}
#
# condiments_sauces = {"Fine Salt (25)": 0.80, "Sea Salt Flakes (26)": 1.30, "Chicken Stock (27)": 3.15, "Chili Sauce (28)": 2.65,
#                      "Oyster Sauce (29)": 4.50, "Sweet Soy Sauce (30)": 3.75, "Tomato Ketchup (31)": 3.20, "Sesame Oil (32)": 4.95}
#
# drinks_and_beverages = {"Green Tea Canned 330ML (33)": 15.00, "Blackcurrent Ribena 330ML (34)": 31.00, "100 Plus 24 Cans (35)": 15.00,
#                         "Orange Cordial 2 Litre (36)": 3.90, "Mineral Water 24 x 600ML (37)": 7.00, "Pineapple Juice (38)": 0.80, "Nescafe Coffee (39)": 9.90, "Coke 24 cans (40)": 12.40}
#
# shopping_menu= dairy|packaged_goods|canned_goods|condiments_sauces|drinks_and_beverages

# print()
#
# print("#########################")
# print("##### SHOPPING LIST #####")
# print("#########################")




# def main():
#     print()
#     print("Please input the number of the action that you would like to do.")
#     print("1. View shopping list" '\n'
#           "2. Add item to shopping cart" '\n'
#           "3. Remove item from shopping cart" '\n'
#           "4. View your shopping cart" '\n'
#           "5. Go to checkout" '\n'
#           "6. Exit")
#     print()
#     action = int(input("Please input the action number: "))
#     print()
#     while True:
#         if action == 1:
#             action1()
#         elif action == 2:
#             action2()
#         elif action == 3:
#             action3()
#         elif action == 4:
#             action4()
#         elif action == 5:
#             action5()
#         elif action == 6:
#             action6()
#         else:
#             print('Invalid number, please try again')
#
# total_price=[]
# # user_shopping_list=[]
# def action1():
#     print("Do you want to display shopping list according to category, alphabetical order or in ascending price?")
#     input("Please input C for category, A for alphabetical order and P for ascending price:")
#
# def action1_category():
#     print("***DAIRY***")
#     for key in dairy:
#         print('%s - $%.2f' % (key, dairy[key]))
#     print()
#
#     print("***PACKAGED GOODS***")
#     for key in packaged_goods:
#         print('%s - $%.2f' % (key, packaged_goods[key]))
#     print()
#
#     print("***CANNED GOODS***")
#     for key in canned_goods:
#         print('%s - $%.2f' % (key, canned_goods[key]))
#     print()
#
#     print("***CONDIMENTS/SAUCES***")
#     for key in condiments_sauces:
#         print('%s - $%.2f' % (key, condiments_sauces[key]))
#     print()
#
#     print("***DRINKS AND BEVERAGES***")
#     for key in drinks_and_beverages:
#         print('%s - $%.2f' % (key, drinks_and_beverages[key]))
#     print()
#
# def action2():
#     action1_category()
#     global qlist
#     qlist=[]
#     while True:
#         num=input('Key the number of the item you would like to get [item (no.)]: ')
#         global q
#         q=int(input('Key the number of the items you would like: '))
#         user_shopping_list.append('{} x {}'.format(q,num))
#         total_price.append(q*shopping_menu.get(num))
#         choice=input('Would you like to add more things to your cart?(y/n) ')
#         if choice == 'y':
#             continue
#         else:
#             main()
#             break
#
# def action3():
#     print(user_shopping_list)
#     while True:
#         print()
#         print('Be warned that all quantities of the item would be removed')
#         print()
#         delete=int(input('Key in the number that you would like to remove'
#                          '(1 being the first item in the list)  : '))
#         user_shopping_list.remove(user_shopping_list[delete-1])
#         total_price.remove(total_price[delete-1])
#         choice=input('Would you like to delete more things from your cart?(y/n) ')
#         if choice == 'y':
#             print(user_shopping_list)
#             continue
#         else:
#             main()
#             break
#
#
#
# main()

