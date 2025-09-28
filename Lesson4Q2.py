import pandas as pd

s = "I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation. Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity. But one hundred years later, the Negro still is not free. One hundred years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination. One hundred years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity. One hundred years later, the Negro is still languishing in the corners of American society and finds himself an exile in his own land. So we have come here today to dramatize a shameful condition"
print("String is :" , s)

# Convert string into a pandas Series of words
words = pd.Series(s.lower().split())

print("Total word count " , len(words))

# Remove punctuation using str.replace (vectorized)
words = words.str.replace(r'[^\w]', '', regex=True)

# Drop empty strings if any
words = words[words != ""]

print("Total word count after removing special chars and empty spaces" , len(words))

#Question 2.1 - Find out how many unique words in s

# Get unique words
print("\nQuestion 2.1 Find out how many unique words in s")
unique_words = words.unique()
print("\nTotal unique words:", len(unique_words))
print("\nUnique words in the text:")
print(unique_words)
#Convert to dictionary {word: count}
word_count_dict = words.value_counts().to_dict()
#Display Word counts as dictionary
print("\nWord counts as dictionary:")
print(word_count_dict)
print("\n------------------------")
#Question 2.2 Which word appears the most
print("\nQuestion 2.2 Most common word:")
# Get the most common word
most_common = words.value_counts().head(1)
# Display the most common word
print("Most common word is :", most_common.index[0])
#Display the count of the most common word
print("Most common word appears :", most_common.iloc[0], "times")
print("\n------------------------")

#Question 2.3 How many words start with ‘t’
print("\nQuestion 2.3 Words starting with 't':")
# Filter words starting with 't'
t_words = words[words.str.startswith('t')]
# Display the words starting with 't'
print("Number of words starting with 't':", t_words.shape[0])
# Display unique words starting with 't'
print("Unique words starting with 't':", t_words.unique())
print("\n------------------------")