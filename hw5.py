
# coding: utf-8

# In[8]:


import csv
import json
import string
import pickle


# In[9]:


def main(filename):
    txtfile=open(filename)
    lines=txtfile.readlines()
    all_words=[]
    for line in lines:
        words=line.split()
        for word in words:
            word=word.strip(string.punctuation)
            if word!=(''):
                all_words.append(word)
    from collections import Counter
    counter=Counter(all_words)
    with open('wordcount.csv','w',newline='')as csv_file:
        writer=csv.writer(csv_file,delimiter=',')
        writer.writerow(['word','count'])
        writer.writerows(counter.most_common())
    with open('wordcount.json','w')as json_file:
        json.dump(counter,json_file)
    with open('wordcount.pkl','wb')as pkl_file:
        pickle.dump(counter,pkl_file)


# In[10]:


if __name__ == '__main__':
    main("i_have_a_dream.txt")

