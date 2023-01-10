#!/usr/bin/env python
# coding: utf-8

# ### ANALYSIS OF THE 100 MOST POWERFUL WOMEN IN THE WORLD 2022 RANKINGS

# ### CONTENTS
# - [x] Introduction
# - [x] Libraries imports 
# - [x] Data exploration 
# - [x] Data cleaning
# - [x] Data analysis
# - [x] Data visualization
# - [x] Conclusion and Findings

# #### IINTRODUCTION
# 
# Power is the ability to influence the behavior of others with or without resistance. Power is the ability to get things done. People with power are able to influence others behavior to achieve a goal or objective. Influence occurs when a person’s emotions, opinions, or behaviors are affected by others. It is an important component of a leader’s ability to use power and maintain respect in an organization or a nation. 
# 
# A powerful woman is a woman who is not afraid to share her ideas and thoughts, regardless of what others think. She speaks her heart and her mind, she respects herself enough to stand up for herself,  believes in herself, and for the welfare of others.
# 
# #### ABOUT THE DATA
# The data is originally from https://www.forbes.com/lists/power-women but my dataset was downloaded from https://www.kaggle.com/datasets/devrimtuner/the-worlds-100-most-powerful-women, as a CSV file. The data shows their ranks in the world most powerful women, shows their age and country. The dataset is reliable, original and comprehensive. The source has their own licence over the dataset. All the files have consistent columns. Finally, It would be good to have some updated information about the age of some of the women in the dataset, because I had to do some research in order to find the particular age of some of the women in the dataset which was intially stored with an `hyphen sign '-'`. The dataset was determined by four main metrics: money, media, impact and spheres of influence. For political leaders, it weighed gross domestic products and populations; for corporate leaders, revenues and employee counts; and media mentions and reach of all. The result is a collection of women who are fighting the status quo.

# #### QUESTION(S) FOR MY ANALYSIS ON THE TOP 100 MOST POWERFUL WOMEN IN THE WORLD
# 
# The following are a list of questions to be answered after carefully studying the dataset:
# * Top 10 most powerful women by their rank
# * Most powerful women in politics, business, finance, philanthropy, wealth management, singing & songwriting, diplomacy, venture capital, media & entertainment
# * Total number of powerful women in each category
# * The country with the most powerful women 
# * The most powerful women from North America
# * The most powerful women from Africa
# * The most powerful women from Asia
# * The most powerful women from Europe
# * The most powerful women from Australia
# * The continent with the most powerful women 
# * Most powerful women under the age of 50
# * Youngest most powerful woman

# #### IMPORT THE LIBRARY

# In[1]:


# Libraries import
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# #### LOAD MY DATASET

# In[2]:


#loading my data set
df = pd.read_csv("worlds_100_Powerful_women.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# #### EXPLORING MY DATASET

# In[5]:


#Now let's explore the datset


# In[6]:


#checking the shape of the dataframe
df.shape


# In[7]:


#Basic info about the DataFrame
df.info()


# In[8]:


#Checking for duplicates
df.duplicated().sum()


# In[9]:


#Checking for null values
df.isnull().any()


# In[10]:


#checking for null values
df.isnull().sum()


# In[11]:


# Using isna() to cross check the entire dataset for null or missing values 
df.isna()


# #### DATA CLEANING

# After going through the data provided in the dataset, I found out that some informations in the data of the `Category column` are not accurate and some data for the `Age column` has the `hyphen sign '-'` inputted for the age value instead of their age. The accurate informations on some of these data can be gotten from wikipedia where you can find their personal profiles and information including age and their occupation and some other informations on age can be gotten from some reliable websites.
# * I will be inputting the accurate data on some of the categories of our most powerful women
# * Filling up the age values that has the hyphen sign `'-'` with their appropriate age
# * Inputting the accurate country information on Christine Lagarde's data on the  `location column`	
# * I will be inputting a new column for `Continents` that this powerful women are from. This will help our analysis on the continent with the most powerful women.

# 1. Inputting accurate information on some of the data values in our `Category column`

# * I will start by updating for Abigail Johnson's category column

# In[12]:


# Changing Abigail Johnson category column 
df.loc[4]


# In[13]:


# Note Abigail Johnson is into business
df.loc[4] = ['5.0','Abigail Johnson','60','United States','Business']
df


# * updating category column for MacKenzie Scott

# In[14]:


# Changing MacKenzie Scott category column 
df.loc[10]


# In[15]:


#  MacKenzie Scott is into philanthropy 
df.loc[10] = ['11.0','MacKenzie Scott','52','United States','Philanthropy']
df


# * updating category column for Shari Redstone 

# In[16]:


# Changing Shari Redstone's category column 
df.loc[31]


# In[17]:


# Shari Redstone is into media and entertainment
df.loc[31] = ['32.0','Shari Redstone','68','United States','Media & Entertainment']
df


# * updating category column for Mary Callahan Erdoes

# In[18]:


# Changing Mary Callahan Erdoes's category column 
df.loc[42]


# In[19]:


# Mary Callahan Erdoes is into wealth mangement
df.loc[42] = ['43.0','Mary Callahan Erdoes','55','United States','Wealth Management']
df


# * updating category column for Jenny Johnson

# In[20]:


# Changing Jenny Johnson's category column 
df.loc[58]


# In[21]:


#  Jenny Johnson is into business
df.loc[58] = ['59.0','Jenny Johnson','58','United States','Business']
df


# * updating category column for Linda Thomas-Greenfield

# In[22]:


# Changing Linda Thomas-Greenfield's category column 
df.loc[81]


# In[23]:


# Linda Thomas-Greenfield is into diplomacy
df.loc[81] = ['82.0','Linda Thomas-Greenfield','70','United States','Diplomat']
df


# * updating category column for Shonda Rhimes

# In[24]:


# Changing Shonda Rhimes's category column 
df.loc[92]


# In[25]:


# Shonda Rhimes is into media and entertainment
df.loc[92] = ['93.0','Shonda Rhimes','52','United States','Media & Entertainment']
df


# * updating category column for Dolly Parton

# In[26]:


# Changing Dolly Parton's category column 
df.loc[95]


# In[27]:


# Dolly Parton is into singing and songwriting
df.loc[95] = ['96.0','Dolly Parton','76','United States','Singer-songwriter']
df


# * updating category column for Kirsten Green	

# In[28]:


# Changing Kirsten Green's category column 
df.loc[96]


# In[29]:


# Kirsten Green is into venture capitals
df.loc[96] = ['97.0','Kirsten Green','51','United States','Venture Capital']
df


# A preview of the updated dataset

# In[30]:


# Preview of the updated dataset with the first 40 rows
df.head(40)


# In[31]:


# Bottom 20 preview of the updated dataset
df.tail(20)


# In[ ]:





# 2. Filling up the various age values that has the hyphen sign `'-'` with their appropriate age values. The various websites we got their ages from will be written on their code blocks.

# In[32]:


# Updating the 'Age" value for Marianne Lake and Jennifer Piepszak
# Age gotten from: (https://en.wikipedia.org/wiki/Marianne_Lake)
# Age gotten from: (https://www.barrons.com/articles/barrons-100-most-influential-women-in-u-s-finance-jennifer-piepszak-5165061442)
df.loc[38]


# I noticed that this cell has more than one profile name. Note that these two profiles where `ranked` at the same position that is the reason for the two profiles showing on the same position. Jennifer Piepszak's age `(52_years)` will be fixed to her name, while Marianne Lake's age `(54_years)` will be left on the age column, so that it won't affect my analysis on age later. I will be looking for powerful women who are less than 50 years of age later in my analysis. That means her age will not affect the analysis when analyzing ages below 50.

# In[33]:


# Updating age data for Marianne Lake and Jennifer Piepszak. 
# I fixed Jennifer Piepszak age (52_years) to her name so that it won't affect my analysis on powerful women under the age of 50 later
df.loc[38] = ['39.0','Marianne Lake, Jennifer Piepszak(52_years)','54','United States','Finance']
df


# In[34]:


# Updating the 'Age" data for Paula Santilli. 
# Age gotten from: (https://app.boardroomalpha.com/profiles/people/A1176721-PAULA_SANTILLI)
df.loc[70]


# In[35]:


# Updating the age data for Paula Santilli 
df.loc[70] = ['71.0','Paula Santilli','57','Mexico','Business']
df


# In[36]:


# Updating the 'Age" data for Laura Cha. 
# Age gotten from: (https://en.wikipedia.org/wiki/Laura_Cha)
df.loc[71]


# In[37]:


# Updating the age data for Laura Cha
df.loc[71] = ['72.0','Laura Cha','73','China','Finance']
df


# In[38]:


# Updating the 'Age" data for Raja Easa Al Gurg. 
# Age gotten from: (https://www.thenationalnews.com/arts-culture/books/raja-al-gurg-in-life-and-business-uae-women-can-have-it-all-1.805368)
# According to the website Raja Easa Al Gurg was born in November 5, 1955, that's approximately 67 years old.
df.loc[91]


# In[39]:


# Updating the age data for Raja Easa Al Gurg
df.loc[91] = ['92.0','Raja Easa Al Gurg','67','United Arab Emirates','Business']
df


# In[40]:


# Updating the 'Age" data for Mahsa Amini (posthumous). 
# Age gotten from: (https://en.wikipedia.org/wiki/Death_of_Mahsa_Amini)
df.loc[99]


# In[41]:


# Updating the age data for Mahsa Amini (posthumous)
df.loc[99] = ['100.0','Mahsa Amini (posthumous)','22','Iran','Politics & Policy']
df


# In[42]:


# I couldn't find the age for Hana Al Rostamani after a thorough research on her age
# So I am going to remove the hyphen sign '-' and leave it blank so it won't distrupt my analysis on age later
df.loc[59]


# In[43]:


# I will remove the hyphen sign '-' for Hana Al Rostamani and also leave the age blank so it won't affect my analysis for age later
df.loc[59] = ['60.0','Hana Al Rostamani','','United Arab Emirates','Finance']
df


# 3. Inputting the accurate country information on Christine Lagarde's data on the location column

# In[44]:


# updating Christine Lagarde's location info
df.loc[1]


# In[45]:


# Christine Lagarde is a French politician and the current President of the European Central Bank
# She is from France and the information about her nationality can be gotten from:(https://en.wikipedia.org/wiki/Christine_Lagarde)
df.loc[1] = ['2.0','Christine Lagarde','66','France','Politics & Policy']
df


# 4. Inputting a new column for Continents that this powerful women are from. This will help our analysis on the continent with the most powerful women

# To add the new `Continent` column to the existing dataframe I will be uploading another CSV file containing only their various continents which I updated using excel, then I will concatenate the new file and the existing dataframe. This will help me save time instead of creating a column and inputting their continents one after each other, because I have over 100 rows to fill with their various continents.

# In[46]:


#load the continent dataset
df1 = pd.read_csv("continents_powerful women.csv")


# In[47]:


# The data for the continents where our top 100 most powerful women came from
df1.head()


# In[48]:


# My previous cleaned/updated data which i will be concatenating with their continents data
df.head() 


# In[49]:


# Concatenating the continents data with the cleaned data to give us the updated dataset with their various continents
df_updated = pd.concat([df, df1], axis=1)


# In[50]:


df_updated


# I will have to save this new updated dataset to a CSV file incase of any future use of this cleaned and updated dataset

# In[51]:


# Save manipulated dataframe to CSV file
df_updated.to_csv("saved_powerful_women.csv", index = False)


# #### DATA ANALYSIS AND VISUALIZATION 

# ##### QUESTION 1: THE TOP 10 MOST POWERFUL WOMEN IN THE WORLD BY THEIR RANK

# In[52]:


# Searching for the top 10 most powerful women by their ranks using transform('any')
df_updated['RANK'] = pd.to_numeric(df_updated['RANK']) #This code is to parse some RANK values to numeric values due to our previous data cleaning process
top_10 = (df_updated['RANK'].isin([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[top_10]
df_top10 = df_updated.loc[top_10]
df_top10


# * This list shows the top 10 most powerful women on earth according to their ranks
# * Ursula von der Leyen is the most powerful woman on earth and a politician by occupation
# * Christine Lagarde the President of the European Central Bank is the second most powerful woman in the world
# * The United States has about seven (7) powerful women on this list, making them the country with the most powerful women on the top 10 list
# * Kamala Harris who is the vice president of the United States is the 3rd most powerful woman in the world
# * Giorgia Meloni (45_years) who is an Italian politician and the current prime minister of Italy is the youngest amongst the top 10 most powerful women in the world 

# ##### QUESTION 2: MOST POWERFUL WOMEN IN POLITICS, BUSINESS, FINANCE, PHILANTROPY, WEALTH MANAGEMENT, SINGING & SONGWRITING, DIPLOMACY, VENTURE CAPITAL, MEDIA & ENTERTAINMENT

#   Most Powerful Women in Politics

# In[53]:


# Most Powerful Women in Politics
politics = (df_updated['CATEGORY'].isin(['Politics & Policy']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[politics]


# * Ursula von der Leyen is the most powerful woman in politics
# * Mahsa Amini (posthumous) the Iranian who died late last year became one of the most poweful women in politics and in the world

# Most Powerful Women in Business

# In[54]:


# Most Powerful Women in Business
business = (df_updated['CATEGORY'].isin(['Business']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[business]


# *  Mary Barra an American businesswoman and executive officer (CEO) of General Motors is the most powerul woman in business
# *  Abigail Johnson an American billoniare business woman and the Chairwoman, CEO, and president, Fidelity Investments is the second most powerful woman in business
# * Sinead Gorman is the youngest most powerful woman in business

#  Most Powerful Women in Finance

# In[55]:


# Most Powerful Women in Finance
finance = (df_updated['CATEGORY'].isin(['Finance']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[finance]


# * Jane Fraser the chief executive (CEO) of Citigroup is the most powerful woman in the finance sector and the 10th most powerful woman on earth
# *  Marianne Lake and Jennifer Piepszak are both the 6th most powerful woman in the finance sector and both also 39th most powerful women on earth
# * Lynn Martin is the youngest most powerful woman in finance 

# Most Powerful Women in Philanthropy

# In[56]:


# Most Powerful Women in Philanthropy
philanthropist = (df_updated['CATEGORY'].isin(['Philanthropy']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[philanthropist]


# * Melinda French Gates an American philanthropist is the most powerful woman in  Philanthropy

# Most Powerful Women in Wealth Management

# In[57]:


# Most Powerful Women in Wealth Management
wealth_investment = (df_updated['CATEGORY'].isin(['Wealth Management']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[wealth_investment]


# * Mary Callahan Erdoes the CEO at JPMorgan Chase & C is the most powerful woman in Wealth management and the 43rd most powerful in the world

# Most Powerful Women in Singing and songwriting

# In[58]:


# Most Powerful Women in Singing and songwriting
singing = (df_updated['CATEGORY'].isin(['Singer-songwriter']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[singing]


# * Dolly Parton the American singer is the most powerful woman in singing and songwriting

# Most Powerful Women in Diplomacy

# In[59]:


# Most Powerful Women in Diplomacy
diplomacy = (df_updated['CATEGORY'].isin(['Diplomat']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[diplomacy]


# * Linda Thomas-Greenfield an American diplomat who is the United States ambassador to the United Nations under President Joe Biden is the most powerful woman in diplomacy

#  Most Powerful Women in Venture Capital

# In[60]:


# Most Powerful Women in Venture Capital
venture_capital = (df_updated['CATEGORY'].isin(['Venture Capital']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[venture_capital]


# * Mary Meeker an American venture capitalist is the most powerful woman in Venture Capital

# Most Powerful Women in Media & Entertainment

# In[61]:


# Most Powerful Women in Media & Entertainment
media = (df_updated['CATEGORY'].isin(['Media & Entertainment']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[media]


# * Oprah Winfrey an American talk show host and television producer is the most powerful woman in the Media & Entertainment sector
# * Taylor Swift is the youngest among the most powerful women in Media & Entertainment
# * Rihana came as the second most youngest woman in Media & Entertainment after Taylor Swift

# ##### QUESTION 3: TOTAL NUMBER OF POWERFUL WOMEN IN EACH CATEGORY
# 
# I want to find the total number of powerful women from each category and use a visualization to display the category that has the most powerful women. I will visualize this using a bar chart. 

# In[62]:


#  Grouping each category by their total count. This will show the total number of powerful women in each catergory.
df_counted1 = df_updated.groupby(['CATEGORY','NAME']).size().groupby('CATEGORY').count()


# In[63]:


df_counted1 


# In[64]:


# Bar chart showing the category that has the most powerful women in the world

plot_df=df_updated.groupby(['CATEGORY']).count().sort_values(['NAME'],ascending=False)
plot_df=plot_df.sort_values('CATEGORY').reset_index()
x=plot_df['CATEGORY'].astype(str)
y=plot_df['NAME']
plt.bar(x, height=y, width=0.8)
plt.title("Total Number of Powerful Women in Each Category")
plt.xticks(rotation=80);


# * Business category has the most powerful women in the world
# * That is most of the powerful women in the world are business women or into business
# * Politics and policy is also stacked with a lot of powerful women after business category being first. This shows that women are diving more into politics
# * Singing, Wealth management and Diplomat had the lowest amount of powerful women in the top 100 most powerful women inthe world

# ##### QUESTION 4: THE COUNTRY WITH THE MOST POWERFUL WOMEN 

# In[65]:


# Here I will be looking for the country with the most powerful women in the list
df_country = df_updated.groupby(['LOCATION','NAME']).size().groupby('LOCATION').count()


# In[66]:


df_country


# In[67]:


# Bar chart showing the country with the most powerful women
def addlabels(x,y):  #function to add value labels
    for i in range(len(x)):
        plt.text(i,y[i],y[i])
        
fig, ax = plt.subplots(figsize=(10, 6))
plot_df=df_updated.groupby(['LOCATION']).count().sort_values(['NAME'],ascending=False)
plot_df=plot_df.sort_values('LOCATION').reset_index()
x=plot_df['LOCATION'].astype(str)
y=plot_df['NAME']
plt.bar(x, height=y, width=0.9, color='red')   #making the bar chart 

# calling the function to add value labels
addlabels(x, y)

plt.title("The Country with the Most Powerful Women")

# giving X and Y labels
plt.xlabel("LOCATION")
plt.ylabel("NAME")
    
plt.xticks(rotation=90);

plt.show() #visualizing the plot


# * The United States is the country with the most powerful women and this shows how women rights, involvement in politics and policy making, equality, women in business and other sectors has grown positively in the united States
# * The United States had a very high volume of powerful women with about 50% of the women coming from the country compared to other countries
# * India was the second country with the most  powerful women in the world with very low numbers compared to the United States

# ##### QUESTION 5: THE MOST POWERFUL WOMEN FROM NORTH AMERICA

# In[68]:


# Finding the most powerful women from North America
north_america = (df_updated['CONTINENT'].isin(['North America']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[north_america]
north_america1 = df_updated.loc[north_america]
north_america1


# * The most powerful woman from North America is Kamala Harris, who is a politician and the current vice president of the United States of America
# * North America is the continent with the most powerful women on earth
# * Taylor Swift is the youngest most powerful woman from North America

# ##### QUESTION 6: THE MOST POWERFUL WOMEN FROM AFRICA

# In[69]:


# Finding the most powerful women from Africa
africa = (df_updated['CONTINENT'].isin(['Africa']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[africa]
africa1 = df_updated.loc[africa]
africa1.head()


# * Nigeria has the most powerful women from Africa on the list of top 100 most powerful women in the world
# * Only 3 African countries and 3 Africans are part of the 100 most powerful women in the world
# * Ngozi Okonjo-Iweala is the most powerful woman from Africa
# * Samia Suluhu Hassan a Tanzanian politician is the 2nd most powerful woman in Africa and one of the 3 women from Africa who made it to the top 100 list of the most powerful women in the world
# * Mo Abudu is the 3rd most powerful woman in Africa and one of the only two women from Nigeria who made the top 100 list of the most powerful women in the world

# ##### QUESTION 7: THE MOST POWERFUL WOMEN FROM ASIA

# In[70]:


# Finding the most powerful women from Asia
asia = (df_updated['CONTINENT'].isin(['Asia']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[asia]
asia1 = df_updated.loc[asia]
asia1


# * Tsai Ing-wen a Taiwanese politician is the most powerful woman from Asia and the 17th in the world
# * Mahsa Amini (posthumous) the Iranian lady who died late last year is the youngest most powerful woman from Asia and the only woman from Iran to make the list of the top 100 most powerful women in the world

# ##### QUESTION 8: MOST POWERFUL WOMEN FROM EUROPE 

# In[71]:


# Finding the most powerful women from Europe
europe = (df_updated['CONTINENT'].isin(['Europe']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[europe]
europe1 = df_updated.loc[europe]
europe1


# * Ursula von der Leyen the most powerful woman in the world topped the list as the most powerful woman from Europe
# * Sanna Marin a Finnish politician is the youngest most powerful woman from Europe

# ##### QUESTION 9: MOST POWERFUL WOMEN FROM AUSTRALIA

# In[72]:


# Finding the most powerful women from Australia
australia = (df_updated['CONTINENT'].isin(['Australia']).groupby(df_updated['NAME']).transform('any'))
df_updated.loc[australia]
australia1 = df_updated.loc[australia]
australia1                      


# * Jacinda Ardern the 40th Prime Minister of New Zealand is the most powerful woman from the Australian continent
# * Jacinda Ardern is the only woman from New Zealand to make it to top the 100 list of the most powerful women in the world
# * Australia as a country has the most powerful women from the Australian continent
# * Gina Rinehart an Australian mining magnate and businesswoman is the second most powerful woman from the Australian continent and the most powerful woman from Australia as a country

# ##### QUESTION 10: THE CONTINENT WITH THE MOST POWERFUL WOMEN

# In terms of the top 100 most powerful women list, I will be looking for the continent with the most powerful women 

# In[73]:


# Here I will be looking for the continent with the most powerful women out of the top 100 list of powerful women in the world
df_continent = df_updated.groupby(['CONTINENT','NAME']).size().groupby('CONTINENT').count()


# In[74]:


df_continent


# In[75]:


# Using a barplot to show the continent with the most powerful women in the top 100 list
color = ['green']
plot_df1=df_updated.groupby(['CONTINENT']).count().sort_values(['NAME'],ascending=False)
plot_df1=plot_df1.sort_values('CONTINENT').reset_index()
ax = sns.barplot(x=plot_df1['CONTINENT'].astype(str), y=plot_df1['NAME'], data=plot_df1, palette=color)
ax.set_title("The Continent with the Most Powerful Women")
plt.xticks(rotation=45);


#  Using a pie chart to show the percentage each continent represents in the top 100 most powerful women list

# In[76]:


# Using a pie chart to show the percentage each continent represents in the top 100 most powerful women list

my_data = (plot_df1['NAME'])
my_labels = (plot_df1['CONTINENT'])
plt.pie(my_data, labels=my_labels, startangle=25, autopct='%1.1f%%')
plt.suptitle('The Continent with the Most Powerful Women')
plt.axis('equal')
plt.legend(my_labels, loc='best', bbox_to_anchor=(-0.4, 1), fontsize=8)
plt.show()


# * Here we can see that North America has 53 out of the 100 most powerful women in the world, making them the continent with the most amount of powerful women in the world
# * Africa and Australia had the lowest with Africa having 3 powerful women and Australia having only 5 powerful women
# * Asia is the second continent with more powerful women in the list after North America with total of 23 powerful women in the world
# * Europe had about 16 most powerful women in the list

# ##### QUESTION 11: MOST POWERFUL WOMEN UNDER THE AGE OF 50

# In[77]:


# Before running the code for the most powerful women under age 50, I have to convert the age values to numeric values, so that the code can run
df_updated['AGE'] = pd.to_numeric(df_updated['AGE'])


# In[78]:


# Finding the most powerful women under age 50
df_under_50 = df_updated.loc[df_updated['AGE']<50]
df_under_50 


# * Giorgia Meloni the Prime Minister of Italy is the most powerful woman under age 50 
# * Most of the powerful women under age 50 are politicians
# * Mahsa Amini (posthumous) who is late is the youngest woman to feature on the most powerful women  list in the world

# ##### QUESTION 12: YOUNGEST MOST POWERFUL WOMEN

# Here I will be visualizing the youngest most powerful women in the world. I will use the data from the most powerful women under the age of 50 to find and visualize the youngest powerful women on earth.

# In[79]:


# Youngest most powerful women in the world

ax = sns.barplot(x='NAME', y='AGE', data=df_under_50, color='blue')
ax.set_title("Youngest Most Powerful Women")
ax.margins(x=0.03)
ax.bar_label(ax.containers[0])
plt.xticks(rotation=90);


# * Mahsa Amini (posthumous) who is late is the youngest most powerful woman in the world. She was 22 at the time of her death and appeared on the list of the most powerful women on earth
# * Taylor Swift the American entertainment star and musician came as the second youngest most powerful wooman on earth. She  is just 32 years old

# In[ ]:





# #### CONCLUSION AND FINDINGS FROM MY ANALYSIS

# Women are often dynamic leaders of change, they understand the importance of inspiring others and achieving success through team work. Women also strengthen their communities and protect their planet. And I can say women has also contributed heavily to the development of nations. These findings are the various insights I got from my analysis on the top 100 most powerful women in the world;
# 
# * This list shows the top 10 most powerful women on earth according to their ranks
# * Ursula von der Leyen is the most powerful woman on earth and a politician by occupation
# * Christine Lagarde the President of the European Central Bank is the second most powerful woman in the world
# * The United States has about seven (7) powerful women on this list, making them the country with the most powerful women on the top 10 list
# * Kamala Harris who is the vice president of the United States is the 3rd most powerful woman in the world
# * Giorgia Meloni (45_years) who is an Italian politician and the current prime minister of Italy is the youngest amongst the top 10 most powerful women in the world
# * Ursula von der Leyen is the most powerful woman in politics
# * Mahsa Amini (posthumous) the Iranian who died late last year became one of the most poweful women in politics and in the world
# * Mary Barra an American businesswoman and executive officer (CEO) of General Motors is the most powerul woman in business
# * Abigail Johnson an American billoniare business woman and the Chairwoman, CEO, and president, Fidelity Investments is the second most powerful woman in business
# * Sinead Gorman is the youngest most powerful woman in business
# * Jane Fraser the chief executive (CEO) of Citigroup is the most powerful woman in the finance sector and the 10th most powerful woman on earth
# * Marianne Lake and Jennifer Piepszak are both the 6th most powerful woman in the finance sector and both also 39th most powerful women on earth
# * Lynn Martin is the youngest most powerful woman in finance
# * Melinda French Gates an American philanthropist is the most powerful woman in Philanthropy
# * Mary Callahan Erdoes the CEO at JPMorgan Chase & C is the most powerful woman in Wealth management and the 43rd most powerful in the world
# * Dolly Parton the American singer is the most powerful woman in singing and songwrritting
# * Linda Thomas-Greenfield an American diplomat who is the United States ambassador to the United Nations under President Joe Biden is the most powerful woman in diplomacy
# * Mary Meeker an American venture capitalist is the most powerful woman in Venture Capital
# * Oprah Winfrey an American talk show host and television producer is the most powerful woman in the Media & Entertainment sector
# * Taylor Swift is the youngest among the most powerful women in Media & Entertainment
# * Rihana came as the second most youngest woman in Media & Entertainment after Taylor Swift
# * Business category has the most powerful women in the world
# * That is most of the powerful women in the world are business women or into business
# * Politics and policy is also stacked with a lot of powerful women after business category being first. This shows that women are diving more into politics
# * Singing, Wealth management and Diplomat had the lowest amount of powerful women in the top 100 most powerful women inthe world
# * The United States is the country with the most powerful women and this shows how women rights, involvement in politics and policy making, equality, women in business and other sectors has grown positively in the united States
# * The United States had a very high volume of powerful women with about 50% of the women coming from the country compared to other countries
# * India was the second country with the most powerful women in the world with very low numbers compared to the United States
# * The most powerful woman from North America is Kamala Harris, who is a politician and the current vice president of the United States of America
# * North America is the continent with the most powerful women on earth
# * Taylor Swift is the youngest most powerful woman from North America
# * Nigeria has the most powerful women from Africa on the list of top 100 most powerful women in the world
# * Only 3 African countries and 3 Africans are part of the 100 most powerful women in the world
# * Ngozi Okonjo-Iweala is the most powerful woman from Africa
# * Samia Suluhu Hassan a Tanzanian politician is the 2nd most powerful woman in Africa and one of the 3 women from Africa who made it to the top 100 list of the most powerful women in the world
# * Mo Abudu is the 3rd most powerful woman in Africa and one of the only two women from Nigeria who made the top 100 list of the most powerful women in the world
# * Tsai Ing-wen a Taiwanese politician is the most powerful woman from Asia and the 17th in the world
# * Mahsa Amini (posthumous) the Iranian lady who died late last year is the youngest most powerful woman from Asia and the only woman from Iran to make the list of the top 100 most powerful women in the world
# * Ursula von der Leyen the most powerful woman in the world topped the list as the most powerful woman from Europe
# * Sanna Marin a Finnish politician is the youngest most powerful woman from Europe
# * Jacinda Ardern the 40th Prime Minister of New Zealand is the most powerful woman from the Australian continent
# * Jacinda Ardern is the only woman from New Zealand to make it to top the 100 list of the most powerful women in the world
# * Australia as a country has the most powerful women from the Australian continent
# * Gina Rinehart an Australian mining magnate and businesswoman is the second most powerful woman from the Australian continent and the most powerful woman from Australia as a country
# * Here we can see that North America has 53 out of the 100 most powerful women in the world, making them the continent with the most amount of powerful women in the world
# * Africa and Australia had the lowest with Africa having 3 powerful women and Australia having only 5 powerful women
# * Asia is the second continent with more powerful women in the list after North America with total of 23 powerful women in the world
# * Europe had about 16 most powerful women in the list
# * Giorgia Meloni the Prime Minister of Italy is the most powerful woman under age 50
# * Most of the powerful women under age 50 are politicians
# * Mahsa Amini (posthumous) who is late is the youngest woman to feature on the most powerful women list in the world
# * Mahsa Amini (posthumous) who is late is the youngest most powerful woman in the world. She was 22 at the time of her death and appeared on the list of the most powerful women on earth
# * Taylor Swift the American entertainment star and musician came as the second youngest most powerful wooman on earth. She is just 32 years old
