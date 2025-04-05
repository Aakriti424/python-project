#Give users three options: Add book, view book detail, search book, remove book, list all books
#Add book: Ask for book name, description, author, price and make it as a object and store it permanently
#View book: Ask for the book name, search in the list of the book and show the details of the book
#Search book: Ask the book name, print "It is available" if found else print "Not found"
#Remove book: Ask the book name, find it in the list and delete it
#List all the book
import json

class add:
    def data(self):
        add_ask=input("Enter the name of the book: ")
        add_des=input("Please provide the description of the book: ")
        add_author=input("Please enter the name of the author: ")
        add_price=input("Enter the price of thee book: ")
        add_data={"Book":add_ask, "Description":add_des, "Author":add_author, "Price":add_price}
        json_add=json.dumps(add_data)
        with open("library.txt","a") as library:
            library.write(json_add+"-")

class view:
    def search(self):
        view_book=input("Enter the name of the book that you want to search: ")
        with open("library.txt","r") as search:
            load=search.read()
        data=load.split("-")
        for i in data:
            if i!="":
                json_data=json.loads(i)
                if json_data.get("Book")==view_book:
                    print("Your searched book has been found")
                    print(json_data)
                    break
        else:
            print("book not found")

class remove:
    def rem(self):
        rem_book=input("Enter the name of the book that you want to delete: ")
        with open("library.txt","r") as search:
            load=search.read()
        data=load.split("-")
        for i in data:
            if i!="":
                json_data=json.loads(i)
                if json_data.get("Book")==rem_book:
                   del json_data["Book"]
                   del json_data["Description"]
                   del json_data["Author"]
                   del json_data["Price"]
                   print("Your data is deleted")
                   continue
                with open("updated.txt", "a") as update:
                    update.write(json.dumps(json_data)+"-")
    
class list:
    def books(self):
        try:
            with open("Updated.txt","r")as list_book:
                read=list_book.read()
                book_data=read.split("-")
            for i in book_data:
                print(i)
        except FileNotFoundError:
            with open("Library.txt","r") as list_book2:
                read2=list_book2.read()
                book_data2=read2.split("-")
                for x in book_data2:
                    print(x) 
        


            


                    

def main():
    ask_user=input('''What do you want to do?
                      1)Add book
                      2)Search book
                      3)Remove book
                      4)List all the book''')
    if ask_user=="1":
        add1=add()
        add1.data()
        print("Your book is added successfully")
    elif ask_user=="2":
        view1=view()
        view1.search()
    elif ask_user=="3":
        remove1=remove()
        remove1.rem()
    elif ask_user=="4":
        list1=list()
        list1.books()
    else:
        print("Invalid data entered. Please try again.")
        main()
main()