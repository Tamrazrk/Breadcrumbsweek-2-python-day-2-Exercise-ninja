# Get the input string from the user
input_string = input("Enter a sentence: ")

# Split the input string into words
words = input_string.split()

# Create an empty dictionary to store word frequencies
word_freq = {}

# Count the frequency of each word
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Print the frequency of each word
for word, frequency in word_freq.items():
    print(f"{word}:{frequency}")
