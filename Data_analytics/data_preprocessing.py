#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


nltk.download()


# In[23]:


nltk.download('punkt')


# In[24]:


import os
import nltk.corpus
x='Hello vedant, how are you?' 
a=' Hi I am fine, wbu?'
from nltk.tokenize import word_tokenize,sent_tokenize
z=word_tokenize(x)
y=sent_tokenize(x,a)
print(y,z)


# In[7]:


from nltk.corpus import brown
brown.words()


# In[8]:


nltk.corpus.gutenberg.fileids()


# In[9]:


from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)


# In[16]:


filtered_word=[word for word in z if word not in stop_words]
print(filtered_word)


# In[17]:


from nltk.stem import PorterStemmer
ps=PorterStemmer()
sample_words=['python','pythoner','pythoning','pycharm']
for i in sample_words:
    print(ps.stem(i))


# In[18]:


from nltk import pos_tag
pos=pos_tag(filtered_word)
print(filtered_word)


# In[19]:


# 4 operations of Text Analysis
# 1)Tokenization 2)POS Tagging 3)Stemming 4)Stopwords
1)
import os
import nltk.corpus
from nltk.tokenize import word_tokenize,sent_tokenize
word1=word_tokenize(x)
word2=sent_tokenize(x)
print(word1,word2)

from nltk.corpus import brown
brown.words()

2)
from nltk.corpus import pos_tag
pos=pos_tag(filtered_words)
print(pos)

3)
from nltk.stem import PorterStemmer
ps=PorterStemmer()
x=['python','pycharm','pythonly','pythoner']
for i in range:
    print(ps.stem(i))

4)
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
filtered_words=[word for word in word1 if word not in stop_words]
print(filtered_words)


# In[ ]:




