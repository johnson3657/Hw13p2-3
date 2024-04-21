#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3


# In[4]:


connection = sqlite3.connect('chp17/books.db')


# In[5]:


import pandas as pd


# In[6]:


pd.options.display.max_columns = 10


# In[7]:


pd.read_sql('SELECT * FROM authors',connection,index_col=['id'])


# In[8]:


pd.read_sql('SELECT * FROM titles', connection)


# In[9]:


df = pd.read_sql('SELECT * FROM author_ISBN', connection)


# In[10]:


df.head()


# In[11]:


pd.read_sql('SELECT first, last FROM authors', connection)


# In[12]:


pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""",connection)


# In[13]:


pd.read_sql("""SELECT id,first,last FROM authors WHERE last LIKE 'D%'""",connection,index_col=['id'])


# In[14]:


pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""",connection,index_col=['id'])


# In[15]:


pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last,first""",connection, index_col=['id'])


# In[16]:


pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last DESC,first ASC""",connection, index_col=['id'])


# In[17]:


pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title""",connection)


# In[18]:


pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first""",connection).head()


# In[19]:


cursor = connection.cursor()


# In[20]:


cursor = cursor.execute("""INSERT INTO authors (first,last) VALUES ('Sue','Red')""")


# In[21]:


pd.read_sql('SELECT id,first,last FROM authors',connection,index_col=['id'])


# In[22]:


curor =cursor.execute("""UPDATE authors SET last='Black'
WHERE last='RED' AND first='Sue'""")


# In[23]:


pd.read_sql('SELECT id,first, last FROM authors',connection,index_col=['id'])


# In[24]:


cursor.rowcount


# In[25]:


pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])


# In[26]:


cursor = cursor.execute('DELETE FROM authors WHERE id=6')


# In[27]:


cursor.rowcount


# In[28]:


pd.read_sql('SELEct id, first, last FROM authors', connection,index_col=['id'])


# In[29]:


conn = sqlite3.connect('chp17/books.db')
cursor = conn.cursor()


# In[30]:


cursor.execute("SELECT last FROM authors ORDER BY last DESC")
authors_last_names = cursor.fetchall()
print("Authors' last names (descending order):", authors_last_names)


# In[31]:


cursor.execute("SELECT title FROM titles ORDER BY title ASC")
titles = cursor.fetchall()
print("Book titles (ascending order):", titles)


# In[32]:


cursor.execute("""
    SELECT titles.title, titles.copyright, titles.ISBN
    FROM titles
    INNER JOIN author_ISBN ON titles.ISBN = author_ISBN.ISBN
    WHERE title = 'Deitel'
    ORDER BY titles.title
""")
deitel_books = cursor.fetchall()
print("Books by Deitel:", deitel_books)


# In[35]:


cursor.execute("INSERT INTO authors (first, last) VALUES (?, ?)", ('Stephen', 'King'))
conn.commit()
print("New author Stephen King added.")


# In[34]:


cursor.execute("INSERT INTO titles (title, copyright, ISBN) VALUES (?, ?, ?)", ('The Shining', 2022, '1234567890'))
conn.commit()
print("New title 'The Shining' added for Stephen King.")


# In[ ]:





# In[ ]:




