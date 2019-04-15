# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier



#
# # print ("-------------------------")
# # print ("for predictions ")
#
# # import the data
# music_data = pd.read_csv('music.csv')
# #print(music_data)
#
# # clean the data
# # As this data has no duplicates, no empty values, so there is no need to clean the data
#
#
# # spliting the dataset
# X = music_data.drop(columns = ['genre'])
# #print(X)
#
# Y = music_data['genre']
#
#
# # training model
# model = DecisionTreeClassifier()
# model.fit(X,Y)
#
# #predicting the data for missing values
# predictions= model.predict([[21,1],[22,0]])
# print(predictions)
#
#
# #print("--------------------------")
# #print("Accurcy")


#
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score


# print("------------------------")
# # import the data
# music_data = pd.read_csv('music.csv')
# #print(music_data)
#
# # clean the data
# # As this data has no duplicates, no empty values, so there is no need to clean the data
#
#
# # spliting the dataset
# X = music_data.drop(columns = ['genre'])
# #print(X)
#
# Y = music_data['genre']
#
# # train_test_split() --this returns 4 tuple so we can store them as
# X_train, X_test, Y_train, Y_test =train_test_split(X,Y,test_size=0.2)
#
# model = DecisionTreeClassifier()
# model.fit(X_train,Y_train)
# predictions = model.predict(X_test)
#
# score = accuracy_score(Y_test,predictions)
#
# print(score)
#
# print("------------------------")
#


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

music_data = pd.read_csv('music.csv')
# #print(music_data)
#
# # clean the data
# # As this data has no duplicates, no empty values, so there is no need to clean the data
#
#
# # spliting the dataset
X = music_data.drop(columns = ['genre'])
# #print(X)
#
Y = music_data['genre']
#
# # training model
model = DecisionTreeClassifier()
model.fit(X,Y)

#joblib.dump(model,'music-recommender.joblib')
# Now as the data is loaded now comment out the above steps

model = joblib.load('music-recommender.joblib')
predictions = model.predict ([[21,1]])
#print(predictions)


from sklearn import tree

tree.export_graphviz(model, out_file= "music-recommender.dot",
                     feature_names=['age','gender'],
                     class_names=sorted(Y.unique()),
                     label='all',
                     rounded=True,
                     filled=True)