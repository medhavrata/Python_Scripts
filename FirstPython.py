def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    words_frequency = {}
    
    file_contents_lower = file_contents.lower()
    file_contents_split = file_contents_lower.split()
    
    for word in file_contents_split:
        if word in uninteresting_words:
            continue
        for punctuation in punctuations:
            if punctuation in word:
                word = word.replace(punctuation, "")
        if word in words_frequency:
            words_frequency[word] += 1
        else:
            words_frequency[word] = 1
    print(words_frequency)

file_contents = "This is the simply! amazing, journey Towards the Cloud. Enjoy the Journey boys ok.This is the simply! amazing, journey Towards the Cloud. Enjoy the Journey boys ok."
calculate_frequencies(file_contents)