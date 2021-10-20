import configparser
import logging
import pandas
from pandas import DataFrame
import numpy as np
import sqlite3
from sqlite3 import Error
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score

# Classifiers to be tested
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
# Measures

from script.helper import heuristic2
from script.helper import balancer
import time
import operator

from script.heuristicclasstemp import HeurFeat, OneVsRestClassifierBalance


class run_algorithms():
    df = None
    db_filename = "../database/data.db"
    rng_seed = 100
    log_filename = '../log/experiment_classifier_validation.log'

    logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w+', 'utf-8')], level=20)
    logging.getLogger().addHandler(logging.StreamHandler())

    def __init__(self):
        self.conn = sqlite3.connect(self.db_filename)
        self.analysis_preparation()



    def analysis_preparation(self):
        #self.load_df_sql()
        self.load_df_csv()

        self.prepare_data()
        print("Ready for classify. Run test_classifier with model of your choice.")

    def load_df_csv(self):
        self.df = pandas.read_csv('raw_data.csv')

    def test_classifier(self, classifier):
        ca = OneVsRestClassifierBalance(classifier)
        print(f'Running experiment for {classifier}')
        print('Getting per-class scores')


        logging.info(f"labels matrix type: {type(self.labels_matrix)}")
        logging.info(f"labels matrix shape: {self.labels_matrix.shape}")
        y_pred = cross_val_predict(ca, self.features_combined.values, self.labels_matrix, cv=10)

        print('Computing overall results')
        scores_f1 = cross_val_score(classifier, self.features_combined.values, self.labels_matrix, cv=10,
                                    scoring='f1_weighted').mean()

        print(classification_report(self.labels_matrix, y_pred, digits=3))
        print('f1_weighted : {0}'.format(scores_f1))

    def load_df_sql(self):
        try:
            sql_text = """
                SELECT t1.file_id, t1.section_id, t1.url, t1.heading_text, t2.content_text_w_o_tags, 
                t1.abstracted_heading_text || ' ' || t2.content_text_w_o_tags AS abstracted_heading_plus_content, 
                t1.section_code
                FROM section_overview_75pct t1 
                JOIN section_content_75pct t2 ON t1.file_id=t2.file_id AND t1.section_id=t2.section_id
                """
            self.df = pandas.read_sql_query(con=self.conn, sql=sql_text)
        except Error as e:
            logging.exception(e)
        except Exception as e:
            logging.exception(e)
        finally:
            self.conn.close()

    def prepare_data(self):
        df_randomized_order = self.df.sample(frac=1, random_state=self.rng_seed)
        heading_plus_content_corpus = df_randomized_order['abstracted_heading_plus_content']
        content_corpus = df_randomized_order['content_text_w_o_tags']
        heading_text_corpus = df_randomized_order['heading_text']
        url_corpus = df_randomized_order['url']
        label_set = ['-', '1', '3', '4', '5', '6', '7', '8']
        labels = [str(x).split(',') for x in df_randomized_order['section_code']]
        mlb = MultiLabelBinarizer(classes=label_set)
        self.labels_matrix = mlb.fit_transform(labels)

        tfidf = TfidfVectorizer(ngram_range=(1, 1), analyzer='word', stop_words='english')
        tfidfX = tfidf.fit_transform(heading_plus_content_corpus)
        ca = HeurFeat()
        logging.info('tfidf matrix shape: ')
        logging.info(tfidfX.shape)
        derived_features = ca.derive_features_using_heuristics(url_corpus, heading_text_corpus, content_corpus)
        logging.info('Derived features shape:')
        logging.info(derived_features.shape)
        features_tfidf = pandas.DataFrame(tfidfX.todense())
        # Assign column names to make it easier to print most useful features later
        features_tfidf.columns = tfidf.get_feature_names()
        self.features_combined = pandas.concat([features_tfidf, derived_features], axis=1)
        logging.info('Combined features shape:')
        logging.info(self.features_combined.shape)



starter = run_algorithms()
pandas.set_option('display.max_columns', None)
#print(starter.df.head())
starter.test_classifier(LinearSVC())
#starter.df.to_csv('raw_data.csv', encoding='utf-8', index=False)
print("Finish output")
