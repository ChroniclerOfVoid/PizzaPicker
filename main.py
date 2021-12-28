# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!\n")
size = input("What size pizza do you want? S, M, or L \n").upper()
krabby_patties = input("How many would you want?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
krabby_patties=int(krabby_patties)
mr_krabbs = 0
alt_pepperoni=(f"Might you be interested in an alternative product instead the pepperoni? type Y/N\n")
alt_cheese=(f"Might you be interested in an alternative product instead the cheese? type Y/N\n")
size = str(size)
if size == "S":
    mr_krabbs += 15
    add_pepperoni = input("Do you want pepperoni? Y or N \n").upper()
    if add_pepperoni == "Y":
        mr_krabbs += 2
    if add_pepperoni == "N":
        input(alt_pepperoni).upper()
        if alt_pepperoni=="Y":
          mr_krabbs+=10
        else:
          print:(f"Just why...?")

    extra_cheese = input("Do you want extra cheese? Y or N \n").upper()
    if extra_cheese == "Y":
        mr_krabbs += 1
    if extra_cheese == "N":
        input(alt_cheese).upper()
        if alt_cheese=="Y":
          mr_krabbs+=5
        else:
          print(f"But why don't you like cheese?")



    mr_krabbs=krabby_patties*mr_krabbs
    mr_krabbs = "{:.2f}".format(mr_krabbs)


if size == "M":
    mr_krabbs += 20
    add_pepperoni = input("Do you want pepperoni? Y or N \n").upper()
    if add_pepperoni == "Y":
        mr_krabbs += 3
    if add_pepperoni == "N":
        input(alt_pepperoni).upper()
        if alt_pepperoni=="Y":
          mr_krabbs+=10
        else:
          print:(f"Just why...?")

    extra_cheese = input("Do you want extra cheese? Y or N \n").upper()
    if extra_cheese == "Y":
        mr_krabbs += 1
    if extra_cheese == "N":
        input(alt_cheese).upper()
        if alt_cheese=="Y":
          mr_krabbs+=5
        else:
          print(f"But why don't you like cheese?")



    mr_krabbs=krabby_patties*mr_krabbs
    mr_krabbs = "{:.2f}".format(mr_krabbs)


if size == "L":
    mr_krabbs += 25
    add_pepperoni = input("Do you want pepperoni? Y or N \n").upper()
    if add_pepperoni == "Y":
        mr_krabbs += 3
    if add_pepperoni == "N":
        input(alt_pepperoni).upper()
        if alt_pepperoni=="Y":
          mr_krabbs+=10
        else:
          print:(f"Just why...?")

    extra_cheese = input("Do you want extra cheese? Y or N \n").upper()
    if extra_cheese == "Y":
        mr_krabbs += 1
    if extra_cheese == "N":
        input(alt_cheese).upper()
        if alt_cheese=="Y":
          mr_krabbs+=5
        else:
          print(f"But why don't you like cheese?")



    mr_krabbs=krabby_patties*mr_krabbs
    mr_krabbs = "{:.2f}".format(mr_krabbs)



print(f"Your final bill is: ${mr_krabbs}.")
