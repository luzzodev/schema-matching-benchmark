##Progress Bar
def progressBar(count, total, status=''):
    bar_len = 30
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    if count == total:
        print('[%s] %s%s ...%s                      \r\n' % (bar, percents, '%', status), end='')
    else:
        print('[%s] %s%s ...%s                       \r' % (bar, percents, '%', status), end='')


#define Jaccard Similarity function
def jaccard(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    set1.discard("")
    set2.discard("")
    intersection = len(set1.intersection(set2))
    union = (len(set1) + len(set2)) - intersection
    return float(intersection) / union

#input url format *.hostname.root.json.csv
def getHostName(urlSite):
    urltoken = urlSite.split(".")
    try:
        return urltoken[-4]
    except:
        return urltoken[-3]