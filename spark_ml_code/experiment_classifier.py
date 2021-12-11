# code from other files
import heuristic_code
import balancer_code
# import csv_to_df_loader

# pandas
import pandas as pd

# Feature engineering
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer

# Classifiers to be tested
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Measures
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score


# df = csv_to_df_loader.read_CSV_to_DF('/FileStore/project/sqlite_dump.csv')
df = pd.read_csv("sqlite_dump.csv")


# Transform the target vector y
label_set = ['-','1','3','4','5','6','7','8']   # Class '2' has been merged into class '1'
labels = [str(x).split(',') for x in df['section_code']]
mlb = MultiLabelBinarizer(classes=label_set)
labels_matrix = mlb.fit_transform(labels)


# Derive TF-IDF features from heading text and content
heading_plus_content_corpus = df['abstracted_heading_plus_content']
tfidf = TfidfVectorizer(ngram_range=(1,1), analyzer='word', stop_words='english')
tfidfX = tfidf.fit_transform(heading_plus_content_corpus)
features_tfidf = pd.DataFrame(tfidfX.todense())
features_tfidf.columns = tfidf.get_feature_names()


# Derive heuristic features from heading text and content
content_corpus = df['content_text_w_o_tags']
heading_text_corpus = df['heading_text']
url_corpus = df['url']
heuristic = heuristic_code.Heuristic_Feature()
derived_features = heuristic.derive_features_using_heuristics(url_corpus, heading_text_corpus, content_corpus)


# Combine the derived features together
features_combined = pd.concat([features_tfidf, derived_features], axis=1)



svm_object = LinearSVC()
classifier = balancer_code.OneVsRestClassifierBalance(svm_object)
classifier.fit(features_combined.values, labels_matrix)
print(classifier.get_params)




# Test different models
classifiers_to_test = [(balancer_code.OneVsRestClassifierBalance(LinearSVC()), 'SVM (Linear)'),
                        (balancer_code.OneVsRestClassifierBalance(RandomForestClassifier()), 'Random Forest'),
                        (balancer_code.OneVsRestClassifierBalance(GaussianNB()), 'Naive Bayes'),
                        (balancer_code.OneVsRestClassifierBalance(LogisticRegression()),'Logistic Regression'),
                        (balancer_code.OneVsRestClassifierBalance(KNeighborsClassifier()), 'k-Nearest Neighbour')
                        ]


for classifier, classifier_name in classifiers_to_test:
    print(f'Running experiment for {classifier_name}')
    print('Getting per-class scores')
    y_pred = cross_val_predict(classifier, features_combined.values, labels_matrix, cv=10)

    print('Computing overall results')
    scores_f1 = cross_val_score(classifier, features_combined.values, labels_matrix, cv=10, scoring='f1_weighted').mean()

    print(classification_report(labels_matrix, y_pred, digits=3))
    print('f1_weighted : {0}'.format(scores_f1))
