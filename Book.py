class Book:
    amount_of_books = 0

    def __init__(self, name="Rainy day Smoke Bell", price_in_hryvnias=260, number_of_pages=334, author_of_the_book="Jack London",
                 date_of_first_sale=25, color="black", genre_book= "Adventure"):
        self.name = name
        self.price_in_hryvnias = price_in_hryvnias
        self.number_of_pages = number_of_pages
        self.author_of_the_book = author_of_the_book
        self.date_of_first_sale = date_of_first_sale
        self.color = color
        self.genre_book = genre_book

    def __del__(self):
        print("Destructor " + self.name + " deleted")

    def __repr__(self):
        return str(self.__dict__)


def output_static_field():
    return Book.amount_of_books