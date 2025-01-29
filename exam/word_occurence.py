#Word Counter
# Create a program to count the occurrences of each word in a sentence provided by the user.
def word_counter(sentence):
    words=sentence.split()
    word_count={}
    for word in words:
        word=word.lower()
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count
if __name__=="__main__":
    sentence=input("Enter a sentence: ")
    counts =word_counter(sentence)
    for word, count in counts.items():
        print(f"{word}:{count}")