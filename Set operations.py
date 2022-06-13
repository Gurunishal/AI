#!/usr/bin/env python
# coding: utf-8

# In[2]:


E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

union = E|N
intersection = E&N
diff = E-N
symmdiff = E^N

print("Union of E and N is",union)
print("Intersection of E and N is",intersection)
print("Difference of E and N is",diff)
print("Symmetric difference of E and N is",E ^ N)


# In[ ]:




