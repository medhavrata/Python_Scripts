# Reverse the order of words in a given sentence (an array of characters).

def reverse_words(sentence):
    firstWord = ''
    lastWord = ''
    for i in range(0, len(sentence)):
        firstWord += sentence[i]
        if sentence[i] == ' ':
            lastWord += sentence[i+1 : ]
            return f"{lastWord}, {firstWord}"
    #return lastWord, firstWord

if __name__ == '__main__':
    print(reverse_words('Hello World'))