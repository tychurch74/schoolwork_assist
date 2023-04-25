"""
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Two examples are shown below:
Example 1 doesn't use list comprehension, 
Example 2 uses list comprehension.
"""

# Given a list of words, use a list comprehension to generate a new list containing the length of each word, 
# and another list with words longer than a given length.

# Example 1: Without list comprehension
# Initialize list of words
words = ["hello", "world", "foo", "bar", "baz"]

# Initialize list of word lengths
word_lengths = []
# Iterate through each word in the list
for word in words:
    word_lengths.append(len(word))
print(f"Example 1 word lengths: {word_lengths}")

length = 3
# Initialize list of long words
long_words = []
# Iterate through each word in the list and if the length is greater than the given length then add it to the list.
for word in words:
    if len(word) > length:
        long_words.append(word)

print(f"Example 1 long words: {long_words}")


# Example 2: With list comprehension
# Initialize list of words
words = ["hello", "world", "foo", "bar", "baz"]

# Initialize list of word lengths
word_lengths = [len(word) for word in words]
print(f"Example 2 word lengths: {word_lengths}")

# Initialize long words length
length = 3

# Initialize list of long words
long_words = [word for word in words if len(word) > length]
print(f"Example 1 long words: {long_words}")
