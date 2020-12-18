dict={}
while True:
    print("----------HAPPY BIRTHDAY--------------")
    print("1, show Birthday")
    print("2, add birthday")
    print("3, exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        if len(dict.keys())==0:
            print("Nothing to Show")
        else:
            name = input("Enter name")
            birthday = dict.get(name, "Not found")
            print(birthday)
    elif choice==2:
        name= input("Enter name")
        date = input("enter date")
        dict[name]=date
        print("Birthday Added")
    elif choice ==3:
        break
    else:
        print("Choose valid option")