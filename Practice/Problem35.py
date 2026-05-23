def find_index(word, letter):
    index = 0
    for char in word: 
         if char == letter: 
            return index 
         index += 1
    return-1

w = input("Enter the word: ")
letter = input("Enter the letter: ")

result = find_index(w, letter)

print(result)