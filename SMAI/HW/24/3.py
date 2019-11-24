import gensim.downloader as api
wv = api.load('word2vec-google-news-300')

print(wv.most_similar(positive=['woman', 'king'], negative=['man'])[0])

print(wv.most_similar(positive=['cricket', 'federer'], negative=['tennis'])[0])

print(wv.most_similar(positive=['america', 'football'], negative=['india'])[0])

print(wv.most_similar(positive=['daughter', 'man'], negative=['woman'])[0])

