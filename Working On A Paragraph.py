# Example paragraph for analysis
paragraph = """
The Industrial Revolution was a period in history that transformed the world and had a profound impact on society. It began in the late 18th century and continued into the 19th century, marked by significant advancements in technology, industry, and manufacturing processes. The invention of steam engines, spinning jennies, and power looms revolutionized production and transportation, leading to the growth of cities and the rise of factories.

This period of industrialization brought about urbanization, as people moved from rural areas to work in factories and mills. It also led to changes in social structures, with a new class of industrial workers emerging alongside wealthy factory owners. The working conditions during this time were often harsh, and labor movements arose to advocate for better treatment and workers' rights.

The Industrial Revolution not only transformed the economy and society but also had far-reaching consequences on the environment. The increased use of coal and other fossil fuels for energy led to pollution and contributed to climate change. However, it also laid the foundation for modern industrial societies and set the stage for further technological advancements in the centuries to come.
"""

# How many characters it contains
num_characters = len(paragraph)

# How many sentences it contains
num_sentences = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')

# How many words it contains
words = paragraph.split()
num_words = len(words)

# How many unique words it contains
unique_words = set(words)
num_unique_words = len(unique_words)

# Bonus: How many non-whitespace characters it contains
num_non_whitespace_chars = len(paragraph.replace(' ', '').replace('\n', ''))

# Bonus: The average amount of words per sentence in the paragraph
average_words_per_sentence = num_words / num_sentences

# Bonus: The amount of non-unique words in the paragraph
num_non_unique_words = num_words - num_unique_words

# Print the analysis results
print("Analysis of the paragraph:")
print("Number of characters:", num_characters)
print("Number of sentences:", num_sentences)
print("Number of words:", num_words)
print("Number of unique words:", num_unique_words)
print("Number of non-whitespace characters:", num_non_whitespace_chars)
print("Average words per sentence:", average_words_per_sentence)
print("Number of non-unique words:", num_non_unique_words)
