# Predicting People's Education Level
### What
A Machine Learning model to predict people's education level based on factors such as income, expenditure, etc.
### Why
This is one of my first projects. I was browsing datasets to come up with project ideas and when I came across this one, I just started having questions and decided to see if I can answer them.
### How
First I imported the data as a pandas dataframe and cleaned it. Explored the data as individual variables and the relationships between them. Then I subsetted the relevant columns and fitted them into a Logistic Regression model, a K-Nearest Neighbors model, and a Random Forest model. For the Logistic Regression model, I tried between using the liblinear solver and just increasing max iterations for the default lbfgs solver. And for the KNN model, I used GridSearchCV to get the best parameter.
## Results
A Random Forest Model with 64% accuracy, a K-Nearest Neighbors model with 61% accuracy (5-fold cross validation), and a Logistic Regression model with 59.7% accuracy.

<img src="https://user-images.githubusercontent.com/123200960/218274033-ae6a86a6-ce78-403e-8e04-a3f1d90c8c61.png" width="540" height="360">
*Confusion Matrix of Random Forest model*

## Conclusion
I took a look at the data, asked a question and tried to answer it. During the process, I had doubts and wondered if I had maybe asked a wrong or a stupid question. I wondered if it is possible to have a good accuracy in predicting someone's education level based on just the data given in the dataset. 

But in the end, I decided that the best way to find out would be by trying. And it turns out, you **can** be atleast 14% more accurate by using ML than you can be by just guessing. I'll be updating this further as i learn more.

