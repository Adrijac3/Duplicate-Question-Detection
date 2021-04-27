#Function to count the common Bigrams
def common_bigrams_count(q1, q2):
    tokens_1 = custom_tokenize(q1)
    tokens_2 = custom_tokenize(q2)

    if len(tokens_1) < 2 or len(tokens_2) < 2 :
      return 0

    bigrams_1 = nltk.bigrams(tokens_1)
    bigrams_2 = nltk.bigrams(tokens_2)

    frequency_1 = nltk.FreqDist(bigrams_1)
    frequency_2 = nltk.FreqDist(bigrams_2)

    count = 0
    common_pair=[]
    for pair in frequency_1.keys():
      if pair in frequency_2.keys():
        count=count+1
        common_pair.append(pair)
    
    # print(common_pair)
  
  
    return count
  
  
  #Function to count the common trigrams
def common_trigrams_count(q1, q2):
    tokens_1 = custom_tokenize(q1)
    tokens_2 = custom_tokenize(q2)

    if len(tokens_1) < 3 or len(tokens_2) < 3:
      return 0

    trigrams_1 = nltk.trigrams(tokens_1)
    trigrams_2 = nltk.trigrams(tokens_2)

    # print(trigrams_1)
    # print(trigrams_2)

    frequency_1 = nltk.FreqDist(trigrams_1)
    frequency_2 = nltk.FreqDist(trigrams_2)

    # print(frequency_1)
    # print(frequency_2)

    count = 0
    common_pair=[]
    for pair in frequency_1.keys():
      if pair in frequency_2.keys():
        count=count+1
        common_pair.append(pair)
    
    # print(common_pair)
  
  
    return count
