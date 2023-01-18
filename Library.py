#library management system which include oops concept
from win32com.client import Dispatch
sp=Dispatch("SAPI.SpVoice")

class Library:
    def __init__(self,list,name): # pass agrument in a class
        self.booklist=list
        self.name=name
        self.lendDict={}
    def displaybook(self):
        print(f"WE have following books in our library:{self.name}")
        for book in self.booklist:
            print(book)
    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lend book database has been updated")
        else:
            print(f"Book has been already lend by {self.lendDict[book]}")
    def addbook(self,book):
        self.booklist.append(book)
        print("book has been added")
    def returnbook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    Li=Library(["Python","C++","Java","CNN","Algo","Harry potter"],"Hplibrary")
    while(True):
        sp.Speak(f"Welcome to {Li.name}")
        print(f"Welcome to {Li.name} library , PLease enter your choice :")
        print("1) Display book")
        print("2) Lend book")
        print("3) Add book")
        print("4) retrun book")
        user_choice = int(input("Your choice"))
        if user_choice not in[1,2,3,4]:
            print("Enter a valid choice: ")
            continue
        else:
            user_choice=int(user_choice)


        if user_choice==1:
            sp.Speak("Here are the available books")
            Li.displaybook()
        elif user_choice==2:
            user=input("Enter your name :")
            book=input(f"Which book {user} you want")
            if book not in Li.booklist:
                print("this book not available try again")
                continue
            Li.lendbook(user,book)
            sp.Speak(f"You have lend {book} book from Library")
        elif user_choice==3:
            book=input(f"Enter new book you want to add in {Li.name} Library")
            Li.addbook(book)
            sp.Speak(f"{book} book has been added to library Library")
        elif user_choice==4:
            book=input("enter the name of book you want ot return: ")
            Li.returnbook(book)
            sp.Speak(f"Book has been returned")
        else:
            print("Enter a valid choice: " )

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!= "q" and user_choice2!="c"):
            user_choice2=input()
            if user_choice2 =="q":
                sp.Speak("Thanks for using HP library")
                exit()
            elif user_choice2 == "c":
                continue




