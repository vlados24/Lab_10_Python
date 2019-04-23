from builtins import staticmethod


class Book:
    amount_of_books = 0

    def __init__(self, name="", price_in_hryvnias=0, number_of_pages=0, author_of_the_book="",
                 date_of_first_sale=0, color="", genre_book=""):
        self.name = name
        self.price_in_hryvnias = price_in_hryvnias
        self.number_of_pages = number_of_pages
        self.author_of_the_book = author_of_the_book
        self.date_of_first_sale = date_of_first_sale
        self.color = color
        self.genre_book = genre_book
        Book.amount_of_books += 1

        def __del__(self):
            print("Destructor was called")

    def __str__(self):
        return "Book{" \
               + " name = '" + str(self.name) + "'" \
               + ", price_in_hryvnias = " + str(self.price_in_hryvnias) \
               + ", number_of_pages = " + str(self.number_of_pages) \
               + ", author_of_the_book = " + str(self.author_of_the_book) \
               + ", date_of_first_sale = " + str(self.date_of_first_sale) \
               + ", color = " + str(self.color) \
               + ", genre_book = " + str(self.genre_book)


    @staticmethod
    def get_static_amount_of_books(self):
        return Book.amount_of_books