
# 1- Lists: Write a function that takes a list of integers and returns a new list with each integer squared.
def squared_list(list):
    list_sq = []
    for i in list:
        sq = i ** 2
        list_sq.append(sq)
    return list_sq


# 2- Strings: Write a function that takes a string and checks if it's a palindrome (a word, phrase, or sequence that reads the same backward as forward, ignoring spaces, punctuation, and capitalization).
def palindrome(string):
    forward_char = []
    backward_char = []
    
    for element in string:
        forward_char.append(element)
    for element in string[ : :-1]:
        backward_char.append(element)
    
    if forward_char == backward_char:
        return True
    else:
        return False
    

# 3- Dictionaries: Given a list of words, write a function that counts the frequency of each word and stores it in a dictionary.
def word_freq(word_list):
    word_dic = {}
    for word in word_list:
        if word in word_dic.keys():
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return word_dic


# 4. Recursion
def fibonacci(n):
    if n <= 1:
       return n
    else:
       return(fibonacci(n-1) + fibonacci(n-2))
    
print(fibonacci(2))


    




