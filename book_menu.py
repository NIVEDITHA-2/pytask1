books={}
list=[]
def add_book():
    books['book_id']=input("Enter the id of book:")
    books['book_name']=input("Enter the book name:")
    books['author']=input("Enter the author of book:")
    books['price']=input("Enter the price of book:")
    books['publisher']=input("Enter the publisher:")


def display():
    display_book=input("Enter the book name:")
    # if display_book in books:
    #     print("book already exists:")
    # else:
    #     print("book added")
    print(books)

def update():
    books['price']=input("Enter the new price:")
    #
    # if books==book:
    #     print("price is same")
    # else:
    #     print("book_price is updated successfully")


def delete():
    books['delete']=input("Enter the name of the book to be deleted:")
    # if book in books:
    #     del books[book]
    #     print("Book is deleted successfully:")
    # else:
    #     print("Book not found")

    del(books['delete'])


while True:
    print("\n Book Menu")
    print("1.Add_book")
    print("2.display_book")
    print("3.update_price")
    print("4.Delete_book")
    print("5.Exit")
    choice=int(input("Enter your choice:"))

    if choice==1:
        add_book()
    elif choice==2:
        display()
    elif choice==3:
        update()
    elif choice==4:
        delete()
    elif choice==5:
        print("Exit")
        break
    else:
        print("you selected wrong number:")




