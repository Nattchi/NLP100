import pdb
import pprint

import gensim.downloader as api
from gensim.models import KeyedVectors, word2vec

TARGET_FILE = "GoogleNews-vectors-negative300.bin"
LOAD_FILE = "~/NLP100/section07/data/" + TARGET_FILE

# 学習済みモデルのロード
# model = word2vec.Word2Vec(LOAD_FILE)
# KeyedVectors.load_word2vec_format(LOAD_FILE)
# model = KeyedVectors.load_word2vec_format(LOAD_FILE, binary=True)

wv = api.load('word2vec-google-news-300')
# pdb.set_trace()
# 単語ベクトルの表示
pprint.pprint(wv)
