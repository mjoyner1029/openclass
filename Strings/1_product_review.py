# task 1

python_reviews = [ "This product is really good. I'm impressed with its quality.", 
                  "The performance of this product is excellent. Highly recommended!", 
                  "I had a bad experience with this product. It didn't meet my expectations.", 
                  "Poor quality product. Wouldn't recommend it to anyone.", 
                  "The product was average. Nothing extraordinary about it." ]
def find_text(text):
    if text == ("good", "excellent", "bad", "poor", "average"):
        index = text.find(text)
        if index == 'good':
            return f'the keywords {text} was found in the reviews'
        elif index ==  "excellent":
            return f'the keywords {text} was found in the reviews'
        elif index == "bad":
            return f'the keywords {text} was found in the reviews'
        elif index == "poor":
            return f'the keywords {text} was found in the reviews'
        elif index == "average":
            return f'the keywords {text} was found in the reviews'
        else:
            return 'keyword not found'

while True:

    text_input = input('What keyword are you looking for? ')

    result = find_text(text_input)
    print(result).upper()

    continue_search_input = input('do you want to search for more text? (y/n) ').lower()
    if continue_search_input != 'y':
        break



# task 2 

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

s = [ "This product is really good. I'm impressed with its quality.", 
        "The performance of this product is excellent. Highly recommended!", 
        "I had a bad experience with this product. It didn't meet my expectations.", 
        "Poor quality product. Wouldn't recommend it to anyone.", 
        "The product was average. Nothing extraordinary about it." ].split()
def words(s):
    counter = []
    for i in set(s):
        counter.append((i,s.count(i)))
    return counter
print(words(s))


# task 3

string_summary = python_reviews[:31]
print(string_summary)