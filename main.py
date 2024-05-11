import datetime
import sqlite3
x = datetime.datetime.now()
dress=[]
dress1=dress

def adminLogin():
    print("*********************")
    print("1.Display Menu")
    print("2.Add item")
    print("3.Remove item")
    print("4.Order Details")
    print("5.Logout")
    print("*********************")
    

def adminDisplayMenu():
    con=sqlite3.connect("Shopping.db")
    c=con.cursor()
    c.execute("SELECT * FROM Shop")
    myresult = c.fetchall()
    for row in myresult:
        print("-----------------------------------")
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Available  = ", row[2])
        print("Price= ", row[3])
        print("Original_Price  = ", row[4])
        print("Stock Arrived On ", row[5])
        print("-----------------------------------\n")
                     
def addItem():
    n=int(input("Enter the no.of.items need to be added : "))
    for i in range(n):
        new_id=int(input("Enter id : ",))
        new_Name=input("Enter Name : ")
        new_Available=int(input("Enter Available : "))
        new_Price=int(input("Enter Price : "))
        new_original=int(input("Enter the original price : "))
        d=[{"id":new_id,"Name":new_Name,"Available":new_Available,"Price":new_Price,"Original_Price":new_original}]
        dress.extend(d)
        con=sqlite3.connect("Shopping.db")
        c=con.cursor()
        d=c.execute("INSERT INTO Shop(p_id,p_name,aval_p,p_price,ori_price) VALUES (?,?,?,?,?)",(new_id,new_Name,new_Available,new_Price,new_original))
        con.commit()
        adminDisplayMenu()
        
def removeItem():
    itemid=int(input("Enter the id need to be deleted : "))
    con=sqlite3.connect("Shopping.db")
    c=con.cursor()
    c.execute('DELETE FROM Shop WHERE p_id = ?',(itemid,))
    con.commit()
    print("Record Deleted...")                                                                              
    adminDisplayMenu()

def Orderlist():
    con=sqlite3.connect("Shopping.db")
    c=con.cursor()
    c.execute("SELECT * FROM Orders")
    myresult1 = c.fetchall()
    for row in myresult1:
        print("-----------------------------------")
        print("Order Id = ", row[0], )
        print("Name Of Customer=  ", row[1])
        print("Placed Order On  =", row[2])
        print("Product ID= ", row[3])
        print("-----------------------------------\n")
    
   
def logout():
    login()

    

def adminChoice():
    choice=int(input("Please Enter User Choice : "))
    if choice==1:
        adminDisplayMenu()
        adminLogin()
        adminChoice()
    elif choice==2:
        adminDisplayMenu()
        addItem()
        adminLogin()
        adminChoice()
    elif choice==3:
        adminDisplayMenu()
        removeItem()
        adminLogin()
        adminChoice()
    elif choice==4:
        Orderlist()
        adminLogin()
        adminChoice()
    elif choice==5:
        logout()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        adminLogin()
        adminChoice()

def userLogin():
    print("*********************\n")
    print("1.Display Menu")
    print("2.Place order")
    print("3.Cancel order")
    print("4.Logout")
    print("\n*********************")
def userDisplayMenu():
    con=sqlite3.connect("Shopping.db")
    c=con.cursor()
    c.execute("SELECT * FROM Shop")
    myresult1 = c.fetchall()
    for row in myresult1:
        print("-----------------------------------")
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Available  = ", row[2])
        print("Price= ", row[3])
        print("-----------------------------------\n")

def placeOrder():
    userDisplayMenu()
    po_id=int(input("\nEnter the Product ID: "))
    user_n=input("Enter User Name : ")
    con=sqlite3.connect("Shopping.db")
    c=con.cursor()
    c.execute('pragma foreign_keys=on')
    c.execute('UPDATE Shop SET aval_p = aval_p - 1 WHERE p_id =?',(po_id,))
    c.execute('INSERT INTO Orders(order_on,pro_id,name)VALUES (?,?,?)', (str(x),po_id,user_n))
    print("\nSuccessfully Placed The Order Dated By ",x)
    con.commit()
    
def cancelOrder():
    cn_id=int(input("\nEnter The Product ID To Cancel Order: "))
    us_n=(input("Enter the User Name: "))
    con=sqlite3.connect("Shopping.db")
    c=con.cursor()   
    c.execute('DELETE FROM Orders WHERE (name,pro_id)= (?,?)',(us_n,cn_id))
    c.execute('UPDATE Shop SET aval_p = aval_p + 1 WHERE p_id =?',(cn_id,))
    print("\nYour Order has been Cancelled!!!")
    con.commit()
    
def userChoice():
    choice=int(input("Please enter user choice : "))
    if choice==1:
        userDisplayMenu()
        userLogin()
        userChoice()
    elif choice==2:
        placeOrder()
        userLogin()
        userChoice()
    elif choice==3:
        cancelOrder()
        userLogin()
        userChoice()
    elif choice==4:
        logout()
    else:
        print("Invalid Choice. Please enter valid choice")
            

def login():
    tp=input("Admin/User [A/U] : ")
    if tp=='A' or tp=='a' :
        password=input("Enter the password : ")
        if password=="admin123":
            adminLogin()
            adminChoice()    
        else:
            print("Invalid password. Please enter valid password")

    elif tp=='U' or tp=='u':
        password=input("Enter the password : ")
        if(password=="user123"):
            userLogin()
            userChoice()
        else:
            print("Invalid password. Please enter valid password")
    else:
        print("Invalid user type. Enter valid user type")
con=sqlite3.connect("Shopping.db")
c=con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Shop(p_id INT PRIMARY KEY,p_name VARCHAR(50),aval_p INT,p_price INT,ori_price INT)''')
c.execute('''CREATE TABLE IF NOT EXISTS Orders(order_id INTEGER PRIMARY KEY AUTOINCREMENT, name text,order_on TEXT NOT NULL,pro_id INT NOT NULL,foreign key(pro_id) references Shop(p_id));''')
con.close()
login()