# Intro to Scikit-learn (sklearn)
# This demonstrates some of the most useful functions of the beautiful Scikit-Learn library. What we're going to cover:
# 0. An end-to-end Scikit-learn workflow
# 1. Getting the data ready
# 2. Choose the right estimator/algorithm for our problems
# 3. Fit the model/algorithm and use it to make predictions on our data
# 4. Evaluating a model
# 5. Improve a model
# 6. Save and load a trained model
# 7. Putting it all together

# 0. An end-to-end Scikit-learn workflow
# 1. Getting the data ready
import pandas as pd
import numpy as np

heart_disease = pd.read_csv("./data/heart-disease.csv")
# print(heart_disease.head())
# Create X (features matrix)
x = heart_disease.drop("target", axis=1)
# y = Create Y (labels)
y = heart_disease["target"]
# 2. Choose the right estimator/algorithm for our problems
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
# We'll keep the default hyperparameters
clf.get_params()
# 3. Fit the model/algorithm and use it to make predictions on our data
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
clf.fit(x_train, y_train)
y_preds = clf.predict(x_test)
y_probs = clf.predict_proba(x_test)
print(f"The first 10 predictions of having heart disease are: {y_preds[:10]}")
print(f"The first 10 probabilities of having heart disease are: {y_probs[:10]}")
print(clf.score(x_train, y_train))
print(clf.score(x_test, y_test))
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(classification_report(y_test, y_preds))
print(accuracy_score(y_test, y_preds))
print(confusion_matrix(y_test, y_preds))

# Improve a model
np.random.seed(42)
for i in range(10, 100, 10):
    print(f"Trying model with {i} estimators...")
    clf = RandomForestClassifier(n_estimators=i).fit(x_train, y_train)
    print(f"Model accuracy on test set: {clf.score(x_test, y_test) * 100}%")

#Save and load a model
import pickle
pickle.dump(clf, open("random_forest_model_1.pkl", "wb"))
loaded_model = pickle.load(open("random_forest_model_1.pkl", "rb"))
print(loaded_model.score(x_test, y_test))