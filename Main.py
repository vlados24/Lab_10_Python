from Book import Book

def main():
    paper_book = Book("Mountains of World", 125, 300, "Jeremy Lanister", 43, "White", "Scientific")
    magazine = Book("Top Gear", 300, 230, "Jeremy Clarkson")
    picture_book = Book("Photos of Galaxy")

    print(paper_book)
    print(magazine)
    print(picture_book)
    print(Book.amount_of_books)


main()