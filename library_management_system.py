class LibraryItem:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_available = True
        self.checkout_date = None
        self.due_date = None

class Book(LibraryItem):
    def __init__(self, title, author, category):
        super().__init__(title, author, category)

class Magazine(LibraryItem):
    def __init__(self, title, author, category, publication_date):
        super().__init__(title, author, category)
        self.publication_date = publication_date

class DVD(LibraryItem):
    def __init__(self, title, author, category, release_year):
        super().__init__(title, author, category)
        self.release_year = release_year

class Library:
    def __init__(self):
        self.items = []

    def add_item(self):
        item_type = input("Enter item type (book/magazine/dvd): ").lower()
        title = input("Enter title: ")
        author = input("Enter author / director name: ")
        category = input("Enter category: ")
        if item_type == "book":
            item = Book(title, author, category)
        elif item_type == "magazine":
            publication_date = input("Enter publication date (DD/MM/YYYY): ")
            item = Magazine(title, author, category, publication_date)
        elif item_type == "dvd":
            release_year = input("Enter release year: ")
            item = DVD(title, author, category, release_year)
        else:
            print("Invalid item type!")
            return
        self.items.append(item)
        print("Item added successfully!")

    def checkout_item(self):
        item_type = input("Enter item type (book/magazine/dvd): ").lower()
        title = input("Enter item title to checkout: ")
        item = self._find_item_by_title(title)
        if not item:
            print("Item not found!")
            return
        if not item.is_available:
            print("Item is already checked out!")
            return
        item.is_available = False
        checkout_date = input("Enter checkout date (DD/MM/YYYY): ")
        due_date = input("Enter due date (DD/MM/YYYY): ")
        item.checkout_date = checkout_date
        item.due_date = due_date
        print("Item checked out successfully!")
        print(f"Due date: {item.due_date}")

    def return_item(self):
        item_type = input("Enter item type (book/magazine/dvd): ").lower()
        title = input("Enter item title to return: ")
        item = self._find_item_by_title(title)
        if not item:
            print("Item not found!")
            return
        if item.is_available:
            print("Item is already returned!")
            return
        item.is_available = True
        while True:
            return_date = input("Enter return date (DD/MM/YYYY): ")
            try:
                return_day, return_month, return_year = map(int, return_date.split('/'))
                if 1 <= return_day <= 31 and 1 <= return_month <= 12 and return_year >= 1900:
                    break
                else:
                    print("Invalid date format. Please enter date as DD/MM/YYYY")
            except ValueError:
                print("Invalid date format. Please enter date as DD/MM/YYYY")
        checkout_day, checkout_month, checkout_year = map(int, item.checkout_date.split('/'))
        days_diff = (return_year - checkout_year) * 365 + (return_month - checkout_month) * 30 + (return_day - checkout_day)
        if days_diff > 10:
            print("Overdue! You need to pay a fine of 50 rupees.")
        print("Item returned successfully!")

    def search_items(self):
        item_type = input("Enter item type to search (book/magazine/dvd): ").lower()
        search_by = input("Enter how do you want to search (title/author/category): ").lower()
        search_term = input("Enter search term: ")

        found_items = []
        for item in self.items:
            # Check item type and search criteria match
            if (isinstance(item, Book) and item_type == "book") or \
               (isinstance(item, Magazine) and item_type == "magazine") or \
               (isinstance(item, DVD) and item_type == "dvd"):
                if search_by == "title" and item.title.lower() == search_term.lower():
                    found_items.append(item)
                elif search_by in ("author", "category") and getattr(item, search_by).lower() == search_term.lower():
                    found_items.append(item)

        if found_items:
            print("Search results:")
            for item in found_items:
                if isinstance(item, Book):
                    print(f"Book: {item.title}, Author: {item.author}, Category: {item.category}")
                elif isinstance(item, Magazine):
                    print(f"Magazine: {item.title}, Author: {item.author}, Category: {item.category}, Publication Date: {item.publication_date}")
                elif isinstance(item, DVD):
                    print(f"DVD: {item.title}, Director: {item.author}, Category: {item.category}, Release Year: {item.release_year}")
        else:
            print("No items found!")

    def _find_item_by_title(self, title):
        for item in self.items:
            if item.title == title:
                return item
        return None

library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add new item")
    print("2. Checkout item")
    print("3. Return item")
    print("4. Search items")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            library.add_item()
        elif choice == 2:
            library.checkout_item()
        elif choice == 3:
            library.return_item()
        elif choice == 4:
            library.search_items()
        elif choice == 5:
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")