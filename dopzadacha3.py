import re
from functools import reduce
from collections import OrderedDict

def addPost(init, post):
    rang = int(post[0])
    oldmaxiter = init['maxitem']
    init.update({'maxitem': rang if rang > init['maxitem'] else init['maxitem']})
    if oldmaxiter < rang:
        init['posts'].append(post[1])
    return init

news = []
file_name = "news.txt"
pattern = re.compile(r'([\d]+)\s*(.*)', re.M)

with open(file_name, 'r') as f:
    news = f.read()
    news = pattern.findall(news)

if news:
    result = reduce(addPost, news, OrderedDict({'maxitem': 0, 'posts': []}))
    [print(i) for i in result['posts']]