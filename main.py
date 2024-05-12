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
        return letter_count #print(f"The count of the letters is as follows: {letter_count}")

    def sort_on(d):
        return d["letter"]

    # function calls
    letter_counts = countLetters(content)
    letter_list = [{"letter": key, "num": value} for key, value in letter_counts.items()]

    letter_list.sort(key=sort_on)
    
    result_of_count = "Sorted Letter Counts:\n"
    for item in letter_list:
        result_of_count += f"  {item['letter']}: {item['num']}\n"


    return (print(content),
            print("\n"),
            print("--- Begin report of books/frankenstein.txt ---"), 
            print("\n"),
            countWords(content), 
            print("\n"),
            print(result_of_count), 
            print("--- End report ---"))

main()



