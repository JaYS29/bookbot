def countLetters():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    with open("books/frankenstein.txt") as f:
        letter_list = set()
        book = f.read().lower()
        for char in alphabet:
            if char in set(book):
                letter_list.add(f"{char}: {book.count(char)}")
        print(letter_list)
        
def report():
    with open("books/frankenstein.txt") as f:
        book = f.read().lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        print(f"--- Begining the report of the file {f.name} ---")
        for char in set(book):
            if char in alphabet:
                print(f"The character {char} was found {book.count(char)} times.")
        
                    
def main():
    with open("books/frankenstein.txt") as f:
        lines = f.readlines()
        total_words = 0
        for line in lines:
            words = line.split()
            total_words += len(words)
        print(f"The book has {total_words} words")
        countLetters()
report()
# main()
# countLetters()