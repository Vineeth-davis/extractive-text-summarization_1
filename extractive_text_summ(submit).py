#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##EXTRACTIVE TEXT SUMMERIZATION


# In[ ]:


#Step1
#Importing necessary libraries


# In[1]:



import bs4 as bs
import urllib.request
import re
import nltk
from nltk.corpus import stopwords


# In[ ]:


#Step2
#Fetching an article on ai from Wikipedia


# In[12]:


scrapped_data=urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')

article=scrapped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

file = ""

for p in paragraphs:
    file += p.text

print(file)


# In[ ]:


#Step3:
#preprocessing text (removing special characters and nos)


# In[13]:



file=re.sub('[^a-zA-Z.e.g. ]',' ',file)
file=re.sub(r'\s+',' ',file)
print(file)


# In[ ]:


#Step4:
#tokenizing/splitting sentences and words


# In[14]:


file_sen_split=file.split(". ")
print("total no.of sentences after removing special charcters and nos = ",len(file_sen_split))

file_words_split=file.split(" ")


# In[ ]:


#filtering/tokenizing only useful/necessary words


# In[15]:


from nltk.corpus import stopwords
stopwords=stopwords.words('english')
print("words that are too common an can be ignored if found in the article\n",stopwords)


# In[16]:


token_words=[]
for word in file_words_split:
    if word not in stopwords:
        token_words.append(word)
        
token_words.remove('')
#print("tokenized\useful important words")
print(token_words)


# In[ ]:


#Step5:
#ranking each word and sentences


# In[ ]:


#frequency of occurence of each imp word


# In[17]:


def freq(list,word):
    return list.count(word)
    
word_count={}
list=token_words
for word in token_words:
    word_count[word]= freq(list,word)
print(word_count)


# In[ ]:


#weighting each word


# In[18]:


max_value=max(word_count.values())

for keys in word_count:
    word_count[keys]=word_count[keys]/max_value
    
print(word_count)


# In[ ]:


#ranking each sentences


# In[19]:


sentence_score={}
#sen_score={}
key=0
for sentence in file_sen_split:
    count=0
    #key+=1
    for words in token_words:
        if words in sentence:
            #print(word_count[words])
            count+=word_count[words]
        else:
            pass
    #print(count,sentence)
    sentence_score.update({key:count})
    #sen_score.update({sentence:count})
    key+=1
print("score of all of the sentences in order starting from 0 to 606(last one)\n")
print(sentence_score)
#print(sen_score)


# In[ ]:


#Step6:
#summerizing the whole to 15%of the article


# In[11]:


#25% of text

def summ(file_sen_split,sentence_score,percentage):
    len_para=len(sentence_score)
    len_summ=int((percentage/100)*len_para)
    #print(len_para,len_summ)
    i=1
    k=[]
    while i<=len_summ:
        key_max=max(sentence_score, key=sentence_score.get)
        #print("key_max",key_max)
        s=sentence_score.pop(key_max)
        k.append(key_max)
        #print(k)
        #print(i)
        i+=1
    #print(k)
    k.reverse()
    summary=''

    for nos in k:
        summary+=file_sen_split[nos]+'. '
    b=summary.split(". ")    
    return summary, len(b)
        

print(summ(file_sen_split,sentence_score,25))


# In[ ]:




