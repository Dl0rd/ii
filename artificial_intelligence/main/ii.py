from sklearn.naive_bayes import ComplementNB
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


neg = pd.read_csv('negative.csv', encoding='utf8', sep=';', header=None)
pos = pd.read_csv('positive.csv', encoding='utf8', sep=';', header=None)
df = neg.append(pos, ignore_index=True)
df[4] = df[4].map({-1: 0, 1: 1})
vectorizer = CountVectorizer()
vectorizer.fit(df[3])
X_train = vectorizer.transform(df[3])
clf = ComplementNB().fit(X_train, df[4])


def result(text: str, num: bool = False) -> int:
    my_test_df = pd.DataFrame({'x_test': [text]})
    X_test = vectorizer.transform(my_test_df['x_test'])
    if num:
        return clf.predict_proba(X_test)[0]
    return clf.predict(X_test)[0]

if __name__ == '__main__':
    print(result('мне плохо'))