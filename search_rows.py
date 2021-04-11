import bisect
import hashlib


recs = tuple(i for i in open('sorted_recommends.csv'))
index = tuple(int(i) for i in open('index.csv'))
print('Server Loaded')


def sha1(x):
    return int(hashlib.sha1(x.encode("utf-8")).hexdigest(), 16)


def get_rows(sku, ge=None):
    i = bisect.bisect(index, sha1(sku)) - 1
    print('Rows:', i * 50, i * 50 + 50)
    return recs[i * 50: i * 50 + 50]
