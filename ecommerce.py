import json
def register():
    rname = input("Enter your name: ").lower()
    with open("regdata.txt", "r") as reg:
        conf=reg.read()
    check=conf.split("-")
    for i in check:
        if i!="":
            jcheck=json.loads(i)
            if jcheck.get("Name")==rname:
                print("This user name already exit. Please try an another username.")
                register()
                break
    else:
        rpw = input("Enter the password: ").lower()
        role= input('''Are you 
                        Buyer or seller?
                        ''').lower()
        if rname!="" and rpw!="" and role!="":
            jdata = {"Name": rname, "Password": rpw, "Role":role}
            jstr = json.dumps(jdata)
            with open("regdata.txt","a") as success:
                success.write(jstr+"-")
                print("You have registered your account successfully")
                
        else:
            print("Please donot enter the null value.")
            register()
    reg_ask=input("Do you want to login?yes/no? ") .lower()
    if reg_ask=="yes":
        login()
    elif reg_ask=="no":
        print("Thank you for registering")
    else:
        print("Invalid entry. Please return to login")  

def login():
    lname = input("Enter your name: ").lower()
    lpw = input("Enter the password: ").lower()
    try:
        with open("regdata.txt", "r") as log:
            data = log.read()
    except FileNotFoundError:
        print("No users registered yet.")
        return

    sdata = data.split("-")
    for entry in sdata:
        if entry!= "":
            jldata = json.loads(entry) # Skip invalid JSON entries
            if jldata.get("Name")==lname and jldata.get("Password")==lpw:
                if jldata.get("Role")=="buyer":
                    print("Login successful")
                    buyer()
                    break
                elif jldata.get("Role")=="seller":
                    seller()
                    break
                else:
                    print("Invalid credentials")
                    break
            else:
                print("Invalid credentials. Please try again")
                login()     
            
            
def seller():
    seller_ask=input('''What do you want to do?
                     1) Add product
                     2) View product
                     ''')
    if seller_ask=="1":
        add_prod=input("What is the name of the product that you want to add? ").lower()
        prod_price= input("What is the price of the product per piece?")
        prod_des= input("Write the description of your product ")
        prod_data={"Product": add_prod, "Price":prod_price, "Description": prod_des}
        jprod=json.dumps(prod_data)
        with open("seller.txt","a") as add:
            add.write(jprod+ "-")
            print("Your prodcut has been added")
    elif seller_ask=="2":
        with open("seller.txt","r") as view:
            read=view.read()
            print(read)
                    
    else:
        print("Invalid command")
def bill():
    bil=0
    with open("added product","r") as b:
        a=b.read()
    x=a.split("-")
    for i in x:
        if i!="":
            jbill=json.loads(i)
            bil=bil+int(jbill.get("Price"))*int(jbill.get("Quantity"))
    print(bil)      

def add():
    choice=input("Which product do you want to add? ")
    quantity=input("How much quantity do you want??Write in numbers ")
    with open("seller.txt","r") as view:
        read=view.read()
        view_data= read.split("-")
        for i in view_data:
            if i!="":
                jview=json.loads(i)
                if jview.get("Product")==choice:
                    aprice=jview.get("Price")
                    adata={"added":choice, "Price":aprice, "Quantity": quantity}
                    jadata=json.dumps(adata)
                    with open("added product","a") as added:
                        added.write(jadata + '-')
                        print("product added successfully")
                

def buyer():
    buyer_ask= input('''What do you want to do?
                     1) View Products
                     2) Add product
                     3) Show bill
                     ''')
    if buyer_ask=="1":
        with open("seller.txt","r") as buyer:
            r= buyer.read()
            print(r)
        ask=input("Do you want to continue?yes/no? ").lower()
        if ask=="yes":
            add()
        else:
            pass 


    elif buyer_ask=="2":
        add()
    elif buyer_ask=="3":
        bill()
        
def main():
    ask_user= input('''
                    What do you want to do?
                    1)Register
                    2)Login  
                    ''')
   
    if ask_user=="1":
        register()
    elif ask_user=="2":
        login()
    else:
        print("Invalid command")
   
main()
