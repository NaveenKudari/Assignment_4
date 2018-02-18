
# coding: utf-8

# In[36]:


list1=[]
def listfunction(l):
    for words in l:
        list1.append(len(str(words)))
    return list1

listfunction(["abc","deffgh","uiopyt"])
        

