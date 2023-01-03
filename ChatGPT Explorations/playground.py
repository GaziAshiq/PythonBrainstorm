word = input("Enter a word: ")

# Iterate through the characters of the word in reverse order
for i in range(len(word) - 1, -1, -1):
    # Print the current character
    print(word[i], end="")

print()  # Add a newline at the end
