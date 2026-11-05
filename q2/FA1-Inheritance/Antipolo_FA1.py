#All library materials have attributes title and author.
#Books have attributes: title, author, and number of pages
#Magazines have the attributes: title, author, and issue_number.

class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        if isinstance(self, Book):
            print(f"Book Title: {self.get_title()} \nAuthor: {self.get_author()} \nNumber of Pages: {self.get_num_pages()}")
        elif isinstance(self, Magazine):
            print(f"Magazine Title: {self.get_title()} \nAuthor: {self.get_author()} \nIssue Number: {self.get_issue_number()}")
        elif isinstance(self, Publication):
            print(f"Publication Title: {self.get_title()} \nAuthor: {self.get_author()}")

class Book(Publication):
    def __init__(self, title, author, num_pages):
        super().__init__(title, author)
        self.__num_pages = num_pages

    def get_num_pages(self):
        return self.__num_pages
    
    def set_num_pages(self, num_pages):
        if num_pages <= 0:
            print("Number of pages must be positive.")
        else:
            self.__num_pages = num_pages

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return self.__issue_number
    
    def set_issue_number(self, issue_number):
        self.__issue_number = issue_number

pub1 = Publication("Journal of Expiremental Biology", "Ratchiffe, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook information:")
book1.set_num_pages(-320)
book1.display_info()
print(book1.get_num_pages())

print("\nMagazine information:")
mag1.display_info()
print(mag1.get_issue_number())
