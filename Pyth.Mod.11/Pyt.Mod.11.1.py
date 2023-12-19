class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        raise NotImplementedError("Subclasses must implement print_information method")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Information:")
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Information:")
        print(f"Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")


# Main program
def main():
    # Create publications
    donald_duck = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")
    compartment_no_6 = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)

    # Print information for each publication
    donald_duck.print_information()
    print("\n" + "=" * 30 + "\n")
    compartment_no_6.print_information()


if __name__ == "__main__":
    main()
