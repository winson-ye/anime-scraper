#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


def extract_HTML_elements(text):
    elements = []
    acc = ''
    found_tag = False
    for char in text:
        if char == '>':
            acc += char
            elements.append(acc)
            found_tag = False
        elif char == '<':
            acc = char
            found_tag = True
        elif found_tag:
            acc += char
    return elements


# In[13]:


def getTop50():
    r = requests.get('https://myanimelist.net/topanime.php?type=bypopularity')
    elements = extract_HTML_elements(r.text)
    counter = 0
    links = []
    href_offset = 6
    for element in elements:
        if element[1] == 'a':
            tokens = element.split()
            if 'rel' in tokens[-1] and 'href="https://myanimelist.net/anime/' in tokens[1]:
                counter += 1
                links.append(tokens[1][href_offset:-1])
    print("Collected {} links.".format(counter))
    return links


# In[15]:


links = getTop50()


# In[17]:


with open('top50_anime.txt', 'w') as f:
    for link in links:
        f.write("{}\n".format(link))


# In[ ]:




