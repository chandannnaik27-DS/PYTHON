def count_a(word):
    count = 0
    for char in word:
        if char == 'a':
            count += 1
    return count

w = input("Enter any word: ")

result = count_a(w)
print(result)