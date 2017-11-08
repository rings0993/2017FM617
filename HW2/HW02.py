
# coding: utf-8

# In[1]:


#載入OS模組
#This module provides a portable way of using operating system dependent functionality.

import os


# In[3]:


def main():
    print ("Hello World!")
    
    print ("This is Alice's greeting.")
    #用單斜線的時候，再次使用'要加上\
    print ('This is Bob\'s greeting')
    
    foo(5,10)
    
    # ============================
    print ('=' * 30)
    print ("Current working directory is " + os.getcwd())
    
    counter = 0
    counter += 1
    
    food = ['apple', 'orange', 'lemmon']
    
    for i in food:
        print ("I like to eat " + i)
        
    print ("Count to ten")
    
    #從 1 開始數到 10
    for i in range(1, 11):
        print(i)
        


# In[4]:


def foo (para1, para2):
    res = para1 + para2
    
    print ("%s plus %s is equal to %s" % (para1,para2,res))
    
    if res < 50:
        print ("foo")
        
    elif (res>=50) and ((para1 == 24) or para2):
        print ("bar")
        
    else:
        print ("moo")
        
    return res


# In[ ]:


if __name__ == '__main__'

