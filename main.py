def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
    
    def countWords(content):
        text_split = content.split()
        wordcount = len(text_split)
        return print(f"The number of words in the file is {wordcount}!")
    
    def countLetters(content):
        to_lower = content.lower()
        to_lower_allowed = "abcdefghijklmnopqrstuvwxyz"
        letter_count = {}
        for letter in to_lower:
            if letter in to_lower_allowed:
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
        
        return print(f"The count of the letters is as follows: {letter_count}")

    return print(content), countWords(content), countLetters(content)

    
    
main()

