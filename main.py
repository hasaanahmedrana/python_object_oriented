from Author import Author
from Book import Book  
def main():
    Jay_Asher = Author('Jay Asher', 'M', 'jay123@gmail.com')
    book_1 = Book('13 Reasons Why!', Jay_Asher, 1200, 17)
    print('Author name of the book:', book_1.getAuthorName())
    print()
    print("Author's Detail: ",book_1.get_author())
    print()
    print(" Complete Book's Detail:\n",book_1.book)
main()
 