
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


movieData=pd.read_csv("data.txt",sep="|")


# In[7]:


movieData.columns=["ID","Title","Release_Date","Video_Release_Date","IMDB","Unknown","Action","Adventure","Animation","Childrens","Comedy","Crime","Documentary","Drama","Fantasy","FilmNoir","Horror","Musical","Mystery","Ramance","Sci-fi","Thriller","War","Western"]


# In[9]:


movieData.head()


# In[17]:


#deleting duplicates
movieData.drop_duplicates(subset=['Title'],inplace=True)
print movieData.shape 


# In[19]:


movies=movieData.drop(['ID','Release_Date','Video_Release_Date','IMDB'],axis=1)
movies.head()


# In[21]:



from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

Z = linkage(movies.drop(['Title'],axis=1), 'ward')


# In[26]:


# calculate full dendrogram
plt.figure(figsize=(20, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Movies',fontsize=20)
plt.ylabel('distance',fontsize=20)
dendrogram(Z,leaf_rotation=90.,leaf_font_size=1)
plt.show()


# In[29]:


from scipy.cluster.hierarchy import fcluster
k=6 
clusters = fcluster(Z, k, criterion='maxclust') 


# In[31]:


movies['Cluster']=clusters
movies.head(10)


# In[35]:


movies_plot=movies.groupby(['Cluster']).mean()
movies_plot


# In[37]:


import seaborn as sns
plt.figure(figsize=(25, 12))
g=sns.heatmap(movies_plot,cmap="Greens")
g.set_yticklabels(g.get_yticklabels(), rotation = 0, fontsize = 20)
g.set_xticklabels(g.get_xticklabels(), rotation = 40, fontsize = 20)
plt.title('Movie Clusters',fontsize=40)
plt.xlabel('Movie Genres',fontsize=20)
plt.ylabel('Clusters',fontsize=20)

