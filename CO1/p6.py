def find_substring_in_wordlist(wordlist,name):
    count=0
    indices=[]
    for word in wordlist:
        if name in word:
            count+=1
            word_indices=[i for i in range(len(word)) if word.startswith(name,i)]
            indices.append(word.indices)
        else:
            indices.append(0)
    return(count,indices)
wordlist=["fathima","star","apple","unicorn","ghost"]
name="name"
result=find_substring_in_wordlist(wordlist,name)
print("Number of words with'{}' as substring:{}",format(name,result[0]))
print("Indices of'{}' in each word'{}'",format(name,result[1]))