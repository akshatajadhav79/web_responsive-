import pymongo 

client =  pymongo.MongoClient("mongodb://localhost:27017/")
db = client["student_Info"]
con = db["stud"]

def insert_doc():
    name = input("Enter your Name :")
    age = int(input("Enter your Age :"))
    Marks = int(input("Enter Your marks:"))
    phone = input("Enter Your contact Number:")
    if name != None and age != None and Marks != None:
        con.insert_one({"Name":name , "Age":age ,"Marks":Marks,"Contact":phone})
        print("Successfully saved..!")
    menu()

def delete_doc():
    val = input("Enter Value Which you want to delete : ")
    if val is not None:
        con.delete_one({"Name":val})
        print("Deleted Successfully..!")
    menu()

def show():
    data = con.find()
    print("All records are : ----------------------")
    if data is None:
        print("Empty...!")
    else:
        for d in data:
            print(d)
    menu()

def specific_search():
    print("se")
    print("\n----------a:Greater than   b:less than   c:exists----------  ")
    s = input("ENter choice: ")
    if s == 'a':
        pass
    elif s == 'b':pass
    elif s== 'c':pass
    menu()

def update_doc():
    val = input("Enter your Name To Updated col :")
    mycol = {"Name":val}
    name = input("Enter your Name :")
    age = int(input("Enter your Age :"))
    Marks = int(input("Enter Your marks:"))
    phone = input("Enter Your contact Number:")
    newval = {"$set":{"Name":name,"Age":age,"Marks":Marks,"Contact":phone}}
    if name != None:
        con.update_one(mycol,newval)
        print("Data Updated..!")
    menu()
    

def menu():
    print("---------------------------------------Menu------------------------------------------")
    print("1:Insert \n2:Delete \n3.Display \n4.Exit \n5:Specific Search \n6:Update")
    ch = int(input("Enter Choice : "))
    if ch == 1:
        insert_doc()
    elif ch == 2:
        delete_doc()
    elif ch == 3:
        show()
    elif ch == 4:
        exit()    
    elif ch == 5:
        specific_search() 
    elif ch == 6:
        update_doc()            
    else:print("Enter correct Choice..!")  

menu()    
