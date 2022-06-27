import json

def time2str(t):
    ms = int(round(t % 1, 3) * 1000)
    s = int(t)
    m = s // 60
    h = m // 60
    m = m % 60
    s = s % 60
    t_str = '{:0>2}:{:0>2}:{:0>2},{:0>3}'.format(h, m, s, ms)
    return t_str


def bcc2srt(bcc_filename, srt_filename):
    bcc_file = open(bcc_filename, 'r', encoding='utf8')
    text = bcc_file.read()
    jsonsub = json.loads(text)
    numjsonsub = len(jsonsub['body'])
    srt_file = open(srt_filename, 'w', encoding='utf8')
    for i in range(0,numjsonsub):
        tfrom = jsonsub['body'][i]['from']
        tto = jsonsub['body'][i]['to']
        sub = jsonsub['body'][i]['content']
        srt_file.write('{}\n'.format(i + 1))
        srt_file.write('{} --> {}\n'.format(time2str(tfrom), time2str(tto)))
        srt_file.write('{}\n\n'.format(sub))
    srt_file.close()
    bcc_file.close()

if __name__ == '__main__':
    bcc2srt('test.bcc','test.srt')
