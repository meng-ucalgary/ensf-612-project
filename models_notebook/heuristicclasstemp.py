'''
@author: Michael Lee adapting the code from Gede Artha Azriadi Prana original code

Reference
Gprana, “gprana/READMEClassifier,” GitHub. [Online]. Available: https://github.com/gprana/READMEClassifier. [Accessed: 20-Oct-2021].
'''

import nltk
import re
import pandas
from pandas import DataFrame
import numpy as np
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
from joblib import Parallel
from joblib import delayed
from sklearn.utils import resample
from sklearn.utils.validation import check_is_fitted
from sklearn.base import BaseEstimator, clone

class _ConstantPredictor(BaseEstimator):

    def fit(self, X, y):
        self.y_ = y
        return self

    def predict(self, X):
        check_is_fitted(self, 'y_')

        return np.repeat(self.y_, X.shape[0])

    def decision_function(self, X):
        check_is_fitted(self, 'y_')

        return np.repeat(self.y_, X.shape[0])

    def predict_proba(self, X):
        check_is_fitted(self, 'y_')

        return np.repeat([np.hstack([1 - self.y_, self.y_])],
                         X.shape[0], axis=0)


def _fit_binary(estimator, X, y, classes=None):
    """Fit a single binary estimator."""
    unique_y = np.unique(y)
    if len(unique_y) == 1:
        if classes is not None:
            if y[0] == -1:
                c = 0
            else:
                c = y[0]

        estimator = _ConstantPredictor().fit(X, unique_y)
    else:
        estimator = clone(estimator)
        estimator.fit(X, y)
    return estimator

class OneVsRestClassifierBalance(OneVsRestClassifier):

    def fit(self, X, y):
        self.label_binarizer_ = LabelBinarizer(sparse_output=True)
        Y = self.label_binarizer_.fit_transform(y)
        Y = Y.tocsc()
        self.classes_ = self.label_binarizer_.classes_
        totalIns = Y.shape[0]
        XBal = []
        YBal = []
        for i in range(len(self.label_binarizer_.classes_)):
            if len(y.shape) > 1:
                # Matrix
                curIdxs = Y[:, i].nonzero()[0]
            else:
                curIdxs = Y.nonzero()[0]
            baseX = X[curIdxs, :]
            if len(y.shape) > 1:
                # Matrix
                baseY = y[curIdxs, :]
            else:
                # array, e.g. due to testing classifier performance for single label prediction
                baseY = y[curIdxs]
            tempX = X
            tempY = y
            imbalancedIns = baseX.shape[0]
            numDup = totalIns / imbalancedIns - 1
            for j in range(int(numDup)):
                tempX = np.vstack((tempX, baseX))
                if len(y.shape) > 1:
                    tempY = np.vstack((tempY, baseY))
                else:
                    tempY = np.concatenate((tempY, baseY))
            numAdd = totalIns % imbalancedIns
            tempX = np.vstack((tempX, resample(baseX, n_samples=numAdd, random_state=0)))
            if len(y.shape) > 1:
                tempY = np.vstack((tempY, resample(baseY, n_samples=numAdd, random_state=0)))
            else:
                tempY = np.concatenate((tempY, resample(baseY, n_samples=numAdd, random_state=0)))
            XBal.append(tempX)
            if len(y.shape) > 1:
                YBal.append(tempY[:, i])
            else:
                YBal.append(tempY)
        self.estimators_ = Parallel(n_jobs=self.n_jobs)(delayed(_fit_binary)(
            self.estimator, XBal[i], YBal[i], classes=[
                "not %s" % self.label_binarizer_.classes_[i],
                self.label_binarizer_.classes_[i]])
                                                        for i in range(len(YBal)))
        # for i, column in enumerate(columns))
        return self

class HeurFeat():
    def heur_c_k_001(self,input_text):
        if ('report bugs' in input_text.lower()) or ('reporting bugs' in input_text.lower()):
            return 1
        else:
            return 0

    def heur_c_k_002(self,input_text):
        if ' is a ' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_003(self,input_text):
        if '@abstr_code_section' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_004(self,input_text):
        if 'attempts to' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_005(self,input_text):
        if 'inspired by' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_006(self,input_text):
        if 'install ' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_007(self,input_text):
        if 'reasons' in input_text.lower():
            return 1
        else:
            return 0

    # Do not use lower() because we want to capture "Added" at beginning of sentence
    def heur_c_k_008(self,input_text):
        if 'Added ' in input_text:
            return 1
        else:
            return 0

    def heur_c_k_009(self,input_text):
        if 'copyright' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_010(self,input_text):
        if '@abstr_mailto' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_011(self,input_text):
        if 'you can ' in input_text.lower():
            return 1
        else:
            return 0

    # Check if the text comprises solely of @abstr_code_section
    def heur_c_k_012(self,input_text):
        if '@abstr_code_section' == input_text.lower().strip():
            return 1
        else:
            return 0

    def heur_c_k_013(self,input_text):
        if 'About' in input_text:
            return 1
        else:
            return 0

    def heur_c_k_014(self,input_text):
        if 'be sure to' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_015(self,input_text):
        if 'Download' in input_text:
            return 1
        else:
            return 0

    def heur_c_k_016(self,input_text):
        if 'overview' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_017(self,input_text):
        if 'get started' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_018(self,input_text):
        if 'reasons' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_019(self,input_text):
        if 'dependenc' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_020(self,input_text):
        if 'rerun' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_021(self,input_text):
        if 'you''ll be able' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_022(self,input_text):
        if 'you must' in input_text.lower():
            return 1
        else:
            return 0

    def heur_c_k_023(self,input_text):
        if 'previous version' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_001(self,input_text):
        if 'configur' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_002(self,input_text):
        if 'what' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_003(self,input_text):
        if 'why' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_004(self,input_text):
        if 'approach' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_005(self,input_text):
        if 'bugs' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_006(self,input_text):
        if 'contrib' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_007(self,input_text):
        if 'credit' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_008(self,input_text):
        if 'feature' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_009(self,input_text):
        if 'install' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_010(self,input_text):
        if 'intro' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_011(self,input_text):
        if 'licen' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_012(self,input_text):
        if 'objective' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_013(self,input_text):
        if 'request' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_014(self,input_text):
        if 'requirement' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_015(self,input_text):
        if 'resource' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_016(self,input_text):
        if 'setting' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_017(self,input_text):
        if 'setup' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_018(self,input_text):
        if 'started' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_019(self,input_text):
        if 'usage' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_020(self,input_text):
        if 'version' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_021(self,input_text):
        if 'welcome' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_022(self,input_text):
        if 'what is' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_023(self,input_text):
        if 'overview' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_024(self,input_text):
        if 'basic' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_025(self,input_text):
        if 'roadmap' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_026(self,input_text):
        if 'todo' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_027(self,input_text):
        if 'example' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_028(self,input_text):
        if 'about' in input_text.lower():
            return 1
        else:
            return 0

    def heur_h_k_029(self,input_text):
        if 'reference' in input_text.lower():
            return 1
        else:
            return 0

            # Return 1 if string is single non-English word

    # WARNING: For speed, instantiate the word set outside and pass it as parameter,
    # so that instantiation will be done once for each program run
    # instead of once for each row this heuristic is applied to
    def heur_h_c_001(self,input_text, words=None):
        nltk.download('words')
        lcase_input_text = input_text.lower()
        s = lcase_input_text.split(' ')
        if len(s) != 1:
            return 0
        else:
            if words is None:
                words = set(nltk.corpus.words.words())
            if s[0] in words:
                return 0
            else:
                return 1
        return 0

    # Returns 1 if a word in heading text is in repo name, or the other way around
    def heur_h_c_002(self,heading_text, repo_url):
        nltk.download('words')
        heading_words = heading_text.lower().split(' ')
        repo_name = re.sub(r"http(s)*:\/\/www\.github\.com\/.+\/", '', repo_url)
        repo_name = repo_name.replace('.', ' ').replace('-', ' ')
        repo_name_words = repo_name.lower().split(' ')
        match = [val for val in heading_words if val in repo_name_words]
        if len(match) > 0:
            return 1
        else:
            return 0

    # See whether text comprises entirely of ASCII characters
    def heur_c_s_001(self,input_text):
        try:
            input_text.encode(encoding='utf-8').decode('ascii')
        except UnicodeDecodeError:
            return 0
        else:
            return 1

            # Generate DataFrame of derived features using DataFrames of some initial features

    def derive_features_using_heuristics(self,url_corpus, heading_text_corpus, content_corpus):
        nltk.download('words')
        derived_features = DataFrame()
        derived_features['heur_c_k_001'] = [self.heur_c_k_001(x) for x in content_corpus]
        derived_features['heur_c_k_002'] = [self.heur_c_k_002(x) for x in content_corpus]
        derived_features['heur_c_k_003'] = [self.heur_c_k_003(x) for x in content_corpus]
        derived_features['heur_c_k_004'] = [self.heur_c_k_004(x) for x in content_corpus]
        derived_features['heur_c_k_005'] = [self.heur_c_k_005(x) for x in content_corpus]
        derived_features['heur_c_k_006'] = [self.heur_c_k_006(x) for x in content_corpus]
        derived_features['heur_c_k_007'] = [self.heur_c_k_007(x) for x in content_corpus]
        derived_features['heur_h_k_001'] = [self.heur_h_k_001(x) for x in heading_text_corpus]
        derived_features['heur_h_k_002'] = [self.heur_h_k_002(x) for x in heading_text_corpus]
        derived_features['heur_h_k_003'] = [self.heur_h_k_003(x) for x in heading_text_corpus]
        derived_features['heur_h_k_004'] = [self.heur_h_k_004(x) for x in heading_text_corpus]
        derived_features['heur_h_k_005'] = [self.heur_h_k_005(x) for x in heading_text_corpus]
        derived_features['heur_h_k_006'] = [self.heur_h_k_006(x) for x in heading_text_corpus]
        derived_features['heur_h_k_007'] = [self.heur_h_k_007(x) for x in heading_text_corpus]
        derived_features['heur_h_k_008'] = [self.heur_h_k_008(x) for x in heading_text_corpus]
        derived_features['heur_h_k_009'] = [self.heur_h_k_009(x) for x in heading_text_corpus]
        derived_features['heur_h_k_010'] = [self.heur_h_k_010(x) for x in heading_text_corpus]
        derived_features['heur_h_k_011'] = [self.heur_h_k_011(x) for x in heading_text_corpus]
        derived_features['heur_h_k_012'] = [self.heur_h_k_012(x) for x in heading_text_corpus]
        derived_features['heur_h_k_013'] = [self.heur_h_k_013(x) for x in heading_text_corpus]
        derived_features['heur_h_k_014'] = [self.heur_h_k_014(x) for x in heading_text_corpus]
        derived_features['heur_h_k_015'] = [self.heur_h_k_015(x) for x in heading_text_corpus]
        derived_features['heur_h_k_016'] = [self.heur_h_k_016(x) for x in heading_text_corpus]
        derived_features['heur_h_k_017'] = [self.heur_h_k_017(x) for x in heading_text_corpus]
        derived_features['heur_h_k_018'] = [self.heur_h_k_018(x) for x in heading_text_corpus]
        derived_features['heur_h_k_019'] = [self.heur_h_k_019(x) for x in heading_text_corpus]
        derived_features['heur_h_k_020'] = [self.heur_h_k_020(x) for x in heading_text_corpus]
        derived_features['heur_h_k_021'] = [self.heur_h_k_021(x) for x in heading_text_corpus]
        derived_features['heur_h_k_022'] = [self.heur_h_k_022(x) for x in heading_text_corpus]
        derived_features['heur_c_s_001'] = [self.heur_c_s_001(x) for x in heading_text_corpus]

        # Batch 02
        derived_features['heur_c_k_008'] = [self.heur_c_k_008(x) for x in content_corpus]
        derived_features['heur_c_k_009'] = [self.heur_c_k_009(x) for x in content_corpus]
        derived_features['heur_c_k_010'] = [self.heur_c_k_010(x) for x in content_corpus]
        derived_features['heur_c_k_011'] = [self.heur_c_k_011(x) for x in content_corpus]
        derived_features['heur_c_k_012'] = [self.heur_c_k_012(x) for x in content_corpus]
        derived_features['heur_c_k_013'] = [self.heur_c_k_013(x) for x in content_corpus]
        derived_features['heur_h_k_023'] = [self.heur_h_k_023(x) for x in heading_text_corpus]
        derived_features['heur_h_k_024'] = [self.heur_h_k_024(x) for x in heading_text_corpus]
        derived_features['heur_h_k_025'] = [self.heur_h_k_025(x) for x in heading_text_corpus]
        derived_features['heur_h_k_026'] = [self.heur_h_k_026(x) for x in heading_text_corpus]
        derived_features['heur_h_k_027'] = [self.heur_h_k_027(x) for x in heading_text_corpus]
        words = set(nltk.corpus.words.words())
        derived_features['heur_h_c_001'] = [self.heur_h_c_001(x, words) for x in heading_text_corpus]
        derived_features['heur_h_c_002'] = [self.heur_h_c_002(x, y) for x, y in zip(heading_text_corpus, url_corpus)]

        # Batch 03
        derived_features['heur_c_k_014'] = [self.heur_c_k_014(x) for x in content_corpus]
        derived_features['heur_c_k_015'] = [self.heur_c_k_015(x) for x in content_corpus]
        derived_features['heur_c_k_016'] = [self.heur_c_k_016(x) for x in content_corpus]
        derived_features['heur_c_k_017'] = [self.heur_c_k_017(x) for x in content_corpus]
        derived_features['heur_c_k_018'] = [self.heur_c_k_018(x) for x in content_corpus]
        derived_features['heur_c_k_019'] = [self.heur_c_k_019(x) for x in content_corpus]
        derived_features['heur_c_k_020'] = [self.heur_c_k_020(x) for x in content_corpus]
        derived_features['heur_c_k_021'] = [self.heur_c_k_021(x) for x in content_corpus]
        derived_features['heur_c_k_022'] = [self.heur_c_k_022(x) for x in content_corpus]
        derived_features['heur_c_k_023'] = [self.heur_c_k_023(x) for x in content_corpus]
        derived_features['heur_h_k_028'] = [self.heur_h_k_028(x) for x in heading_text_corpus]
        derived_features['heur_h_k_029'] = [self.heur_h_k_029(x) for x in heading_text_corpus]

        return derived_features