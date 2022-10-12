def search(keyword) :
    res = []
    All_words = [keyword]
    for Entry in Thesaurus:
        if keyword == Entry.word:
            for Word in Entry.synonyms:
                All_words.append(Word)
    
    for Search_word in All_words:
        count = 0
        for Document in Corpus:
            for Word in Document:
                if Search_word == Word:
                    count+=1
    
        result = (All_words, count)
        res.append(result)

    return res

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
