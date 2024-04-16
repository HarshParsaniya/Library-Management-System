class Library:
    def __init__(self,library_name,list_of_books):
        self.library_name = library_name
        self.list_of_books = list_of_books
        self.lend = {}

    def display_book(self):
        print('\nThey have some book in the library like this\n')
        for key,values in self.list_of_books.items():
            print(f'{key} - {values}')
        print()

    def add_book(self, bookname, no_of_books):
        # for key, value in self.list_of_books.items():
        #     if bookname == key:
        #         # Book already exists, updating the quantity
        #         self.list_of_books[key] += no_of_books
        #         break
        # else:
        #     # Book doesn't exist, adding a new entry
        #     self.list_of_books[bookname] = no_of_books

        if bookname in self.list_of_books:
            # Book already exists, updating the quantity
            self.list_of_books[bookname] += no_of_books
        else:
            # Book doesn't exist, adding a new entry
            self.list_of_books[bookname] = no_of_books


    def lend_book(self):
        # self.lend = {}
        self.person_name = input('What is your name : ')
        self.bookname = input('Which book do you want : ')

        if self.bookname in self.list_of_books and self.list_of_books[self.bookname] > 0:
            if self.bookname not in self.lend:
                self.list_of_books[self.bookname] -= 1
                self.lend[self.bookname] = [self.person_name]
            else:
                self.list_of_books[self.bookname] -= 1
                self.lend[self.bookname].append(self.person_name)
        else:
            print(f'{self.bookname} is not available in the {self.library_name} library')
            answer = input(f'Do you want to know who has {self.bookname} book (y/n) : ')
            if answer.lower() == 'y' and self.bookname in self.lend:
                print(f'\n{self.bookname} book with {", ".join(self.lend[self.bookname])}\n')

    def return_book(self):
        bookname = input('Which book you have to return : ')
        person_name = input('What is your name : ')
        self.lend[bookname].remove(person_name)
        self.add_book(bookname,1)




library_name = input("Enter the library name : ")
print(f'Library Name is : {library_name}')
book_list = {'Harry Potter':2,'Money Heist':4}


harsh = Library(library_name,book_list)

while True:
    print('\n1. display_book')
    print('2. add_book')
    print('3. lend_book')
    print('4. return book')
    print('5. Exit')

    answer = input('Enter the choise of above list : ')

    match answer:
        case '1':
            harsh.display_book()
        case '2':
            bookname = input('Enter the book name : ')
            no_of_books = int(input('Enter the no of book you are add : '))
            harsh.add_book(bookname,no_of_books)
        case '3':
            harsh.lend_book()
        case '4':
            harsh.return_book()
        case '5':
            exit()
        case _:
            print('Enter the valid number from above mention')