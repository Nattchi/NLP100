import pprint

import gensim.downloader as api
from gensim.models import KeyedVectors, word2vec

# 学習済みモデルのロード
model = api.load('word2vec-google-news-300')
# 単語ベクトルの表示
pprint.pprint(model.similarity('United_States', 'U.S.'))