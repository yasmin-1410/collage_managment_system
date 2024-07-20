import re
class Library():
    __libraryId=0
    __librarianName=""
    __BookSection=""
    __TotalBooks=0
    
    def LibraryDetails(self, LibraryId):
        with open("Library.txt", "r") as file:
            lines = file.readlines()
        
        library_found = False
    
        for line in lines:
            details = line.strip().split(",")
            if len(details) == 4:
                id = details[0]
                Name = details[1]
                BookSection = details[2]
                TotalBooks = details[3]
                if id == str(LibraryId):
                    print(f"id: {id}")
                    print(f"Librarian Name: {Name}")
                    print(f"Book Section: {BookSection}")
                    print(f"Total Books: {TotalBooks}")
                    library_found = True
                    break
    
        if not library_found:
            print("Library details not found")
            
    def SearchBooks(self, BookName):
        with open("Books.txt", "r") as file:
            lines = file.readlines()
        
        book_found = False
        pattern = re.compile(re.escape(BookName), re.IGNORECASE)

        for line in lines:
            details = line.strip().split(",")
            if len(details) == 3:
                id = details[0]
                Name = details[1]
                book_type = details[2]
                if pattern.search(Name):
                    print(f"id: {id}")
                    print(f"Book Name: {Name}")
                    print(f"Book Type: {book_type}")
                    book_found = True
                    
        
        if not book_found:
            print("Book does not exist")
    
    def LendBooks(self,BookName):
        
        with open("Books.txt", "r") as file:
            lines = file.readlines()
        
        book_found = False
        pattern = re.compile(re.escape(BookName), re.IGNORECASE)

        for line in lines:
            details = line.strip().split(",")
            if len(details) == 3:
                id = details[0]
                Name = details[1]
                book_type = details[2]
                if pattern.search(Name):
                    with open("LendBooks.txt", "r") as lend_file:
                        lend_lines = lend_file.readlines()
                    
                    already_lent = False
                    for lend_line in lend_lines:
                        lend_details = lend_line.strip().split(",")
                        if len(lend_details) == 3 and lend_details[1] == Name:
                            already_lent = True
                            break
                    
                    if already_lent:
                        print(f"The book '{Name}' has already been lent out.")
                    else:
                        with open("LendBooks.txt", "a") as lend_file:
                            lend_file.write(f"{id},{Name},{book_type}\n")
                        print(f"Book '{Name}' has been successfully lent out.")
                    
                    book_found = True
                    break
                    
        
        if not book_found:
            print("Book does not exist")
            
    def ReturnBooks(self, BookName):
        
        pattern = re.compile(re.escape(BookName), re.IGNORECASE)

        try:
            with open("LendBooks.txt", "r") as lend_file:
                lend_lines = lend_file.readlines()
        except FileNotFoundError:
            print("LendBooks.txt file not found.")
            return

        book_found = False
        new_lend_lines = []

        for line in lend_lines:
            details = line.strip().split(",")
            if len(details) == 3:
                id = details[0]
                Name = details[1]
                book_type = details[2]
                
                if pattern.search(Name):
                    book_found = True
                    print(f"Book '{Name}' has been returned successfully.")
                else:
                    new_lend_lines.append(line)

        if not book_found:
            print("Book does not exist in the lent list.")
            return

        with open("LendBooks.txt", "w") as lend_file:
            lend_file.writelines(new_lend_lines)

    
        
                
        