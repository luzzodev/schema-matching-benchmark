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