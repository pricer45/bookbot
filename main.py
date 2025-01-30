def book_contents():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()

        print(file_contents)

def word_count():
    number_of_words = 0

    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()

        lines = file_contents.split()
        number_of_words += len(lines)
        print(number_of_words)    

def count_char():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()

        number_of_lines = 0
        number_of_words = 0
        number_of_chars = 0
        char_count = {}

        for line in file_contents:
            number_of_lines += 1
            words = line.split()
            number_of_words += len(words)
            number_of_chars += sum(len(word) for word in words)

            for char in line:
                char = char.lower()
                if char.isalpha():  # Check if the character is alphabetic
                    if char in char_count:
                        char_count[char] += 1
                    else:
                        char_count[char] = 1
            
        print(f"{number_of_chars} characters found in the document")
        
        for char, count in char_count.items():
            print(f"The '{char}' character was found {count} times")

#book_contents()
#word_count()
count_char()