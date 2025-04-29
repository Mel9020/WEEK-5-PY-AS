# Parent class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title               # public attribute
        self.author = author             # public attribute
        self.__pages = pages             # private attribute (encapsulation)

    def get_pages(self):                # getter for encapsulated attribute
        return self.__pages

    def describe(self):
        print(f"'{self.title}' by {self.author}, {self.__pages} pages.")

# Child class: AudioBook (inherits from Book)
class AudioBook(Book):
    def __init__(self, title, author, pages, duration):
        super().__init__(title, author, pages)
        self.duration = duration  # duration in minutes

    def describe(self):
        print(f"'{self.title}' (Audiobook) by {self.author}, Duration: {self.duration} minutes.")

# Example usage
book1 = Book("Atomic Habits", "James Clear", 320)
audiobook1 = AudioBook("The Power of Now", "Eckhart Tolle", 236, 480)

book1.describe()
audiobook1.describe()

print("Pages in audiobook:", audiobook1.get_pages())  # Accessing private pages using method
