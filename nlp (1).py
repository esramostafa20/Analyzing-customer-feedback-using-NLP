# -*- coding: utf-8 -*-
"""NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TuZVc1w4-Nw_PYLZzEZ9xA55QjGUZdIp

# NLP
-- Problem Statement:

## 1. Importing Liberiaries
"""

import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
import re # to remove unwanted characters like : . / , " " ! ? and so on.
import nltk # have all words i need , engilish only
### Remove all unnessary Words
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer  # to get words demming جذور الكلمات
from sklearn.feature_extraction.text import CountVectorizer  # Making Tokenizer
from sklearn.ensemble import RandomForestClassifier #for random forest Classification
from sklearn.metrics import confusion_matrix

"""## 2. Open Data-Set"""

from google.colab import drive
drive.mount('/content/drive')

df=pd.read_csv('/content/drive/MyDrive/Machine-Learning-NanoDegree/Section 33 - Natural Language Processing/Python/Restaurant_Reviews.tsv',delimiter='\t',quoting=3)

df.head()

"""## 3. Cleaning The Data 
#### This is a training for the first row cell
"""

### Removing UnWanted Characters!
review=re.sub('[^a-zA-Z]',' ',df['Review'][0])

### Get Ride of Capital Letters
review = review.lower()

### Put every row as vector
review = review.split()

### remove Stop worlds like this,that...
review =[word for word in review if not word in set(stopwords.words('english'))]

### Getting demming of words
ps = PorterStemmer()
review =[ps.stem(word) for word in review ]

### Get my data string baack
review =' '.join(review)

review

"""## 4.Cleaning The Entire Data-Set"""

corpus=[] #empty list to hold the output of the Cleaning 
for i in range(0,1000):
  ### Removing UnWanted Characters!
  review=re.sub('[^a-zA-Z]',' ',df['Review'][i])

  ### Get Ride of Capital Letters
  review = review.lower()

  ### Put every row as vector
  review = review.split()

  ### remove Stop worlds like this,that...
  review =[word for word in review if not word in set(stopwords.words('english'))]

  ### Getting demming of words
  ps = PorterStemmer()
  review =[ps.stem(word) for word in review ]

  ### Get my data string baack
  review =' '.join(review)

  ### Here after each loop the review(i) will be automatically saved in corpus
  corpus.append(review)

"""### 5.Bag of Words Model
Tokanization


"""

cv = CountVectorizer(max_features = 1500) # max-feature takes the most common values as i five it 
X = cv.fit_transform(corpus).toarray()

"""## From Here the Ordinary Machine Learing Sequence...!

# 6. Creating my Independant Variable
"""

y=df.iloc[:,1].values

"""## 7. Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

"""## 8. Classification
Classification tree or Random forest
I chosed Random forest
"""

classifier = RandomForestClassifier(n_estimators= 10, random_state=0,criterion='entropy')
classifier.fit(X_train,y_train)

# Making Prediction Using OUR Model
y_predict=classifier.predict(X_test)

"""## 9. Confusion Matrix"""

cm = confusion_matrix(y_test, y_predict)
print(cm)