import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import pickle
import os
import pandas as pd
import numpy as np
import sys
import sklearn
import spacy
import re
import multiprocessing
from gensim.models import Word2Vec
import keras
from keras import backend as K
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Dropout
from keras.utils import to_categorical
from keras import optimizers
from gensim.test.utils import get_tmpfile
from utils.UtilWordEmbedding import MeanEmbeddingVectorizer, DocPreprocess


def app_callbacks(app):

    @app.callback(
        Output('output-state', 'children'),
        [Input('submit-button', 'n_clicks')],
        [State('doc', 'value'),
        State('average_ratings', 'value'),
        State('total_reviews', 'value'),
        State('cuisine', 'value')],
        )
    def update_output(n_clicks, doc, average_ratings, total_reviews, cuisine):
        word_model = Word2Vec.load("./utils/word2vec.model")
        mlb = pickle.load(open("./utils/cuisine_encoding", 'rb'))
        model = load_model('./utils/keras_model.h5')

        brief_cleaning = re.sub("[^A-Za-z']+", ' ', str(doc)).lower()
        nlp = spacy.load('en', disable=['ner', 'parser']) # disabling Named Entity Recognition for speed
        stop_words = spacy.lang.en.stop_words.STOP_WORDS
        all_docs = DocPreprocess(nlp, stop_words, [doc],1)
        mean_vec_tr = MeanEmbeddingVectorizer(word_model)
        doc_vec = mean_vec_tr.transform(all_docs.doc_words)
        res = mlb.transform([cuisine])
        res = pd.DataFrame(res, columns = mlb.classes_)
        df = pd.DataFrame([[total_reviews,average_ratings]], columns=['reviews', 'avg_ratings'])
        df = df.join(res)
        mean_embedding_df = df.join(pd.DataFrame(doc_vec))
        y_pred = model.predict(np.array(mean_embedding_df, dtype=np.float32))
        K.clear_session()
        print(round(y_pred[0][0], 2)*100)
        return "Restaurant is "+str(round(y_pred[0][0], 2)*100) +"% hygiene"
    return app
