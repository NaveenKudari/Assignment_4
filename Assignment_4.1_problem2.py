
# coding: utf-8

# In[43]:


list=[]
def filter_long_words(l,n):
    for words in l:
        if(len(words)>n):
            list.append(words)
    return list
    
filter_long_words(['def','abc','xyzcvf'],3)
    

