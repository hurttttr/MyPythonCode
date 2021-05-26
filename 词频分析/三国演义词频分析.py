import jieba
import wordcloud


def show(d):
    font = r'C:/windows/fonts/simfang.ttf'
    wc = wordcloud.WordCloud(
        font_path=font,
        width=500,
        height=400,
        background_color='white',
        font_step=3,
        random_state=False,
    )
    t = wc.generate_from_frequencies(d)
    t.to_image().show()


with open("三国演义.txt", 'r', encoding="utf-8") as f:
    txt = f.read()

words = jieba.lcut(txt)

excludes = ['将军', '二人', '不可', '却说', '荆州', '不能', '如此', '今日', '商议', '如何', '军士', '次日',
            '引兵', '然后', '大败', '不见', '左右', '军马', '大喜', '天下', '东吴', '于是', '不敢', '魏兵',
            '一人', '主公', '都督', '人马', '不知', '汉中', '只见', '陛下', '众将', '后主', '蜀兵', '上马']

d = {}
for w in words:
    if len(w) == 1 or (w in excludes):
        continue
    if w == '诸葛亮' or w == '孔明曰':
        w = '孔明'
    if w == '关公' or w == '云长':
        w = '关羽'
    if w == '玄德' or w == '玄德曰':
        w = '刘备'
    if w == '孟德' or w == '丞相':
        w = '曹操'
    d[w] = d.get(w, 0)+1

lst = sorted(d.items(), key=lambda x: -x[1])
show(d)
# for i in range(15):
#     word, num = lst[i]
#     print('{:<10}{:>5}'.format(word, num))
