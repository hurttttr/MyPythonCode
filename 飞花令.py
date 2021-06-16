import requests
import re
import json


def get_poem():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    url = 'https://so.gushiwen.org/shiwens/'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    div = re.findall(r'<div class="cont">(.*?)</div>', html, re.S)[11]
    chapter_info_list = re.findall(r'<a href="(.*?)">(.*?)</a>', div)
    gushi_total_list = []
    cnt = n = 0
    for index in chapter_info_list:
        if cnt > 1500:
            break
        part_url, title = index
        gushigroup_url = 'https://so.gushiwen.org'+part_url
        gushigroup_response = requests.get(gushigroup_url, headers=headers)
        gushigroup_response.encoding = 'utf-8'
        gushigroup_html = gushigroup_response.text
        gushigroup_info_list = re.findall(
            r'<span><a href="(.*?)" target="_blank">(.*?)</a>\((.*?)\)</span>', gushigroup_html)
        poem_lst = []
        for group_index in gushigroup_info_list:
            gushi_part_url, gushi_name, gushi_author = group_index
            gushi_part_url = re.findall(
                'shiwenv_(.*?)\.aspx', gushi_part_url)[0]
            gushi_url = 'https://so.gushiwen.org/shiwenv_{}.aspx'.format(
                gushi_part_url)
            if gushi_url not in gushi_total_list:
                gushi_total_list.append(gushi_url)
                poem = gushi_total_list[cnt]
                poem_url, poem_name, poem_author = poem, gushi_name, gushi_author
                poem_response = requests.get(poem_url, headers=headers)
                poem_response.encoding = 'utf-8'
                poem_html = poem_response.text
                dic = {}
                try:
                    _, poem_body = re.findall(
                        r'<div class="contson" id="contson(.*?)">(.*?)</div>', poem_html, re.S)[0]
                    yizuo = re.compile('.*(\(.*?\)).*').findall(
                        poem_body)
                    if yizuo:
                        poem_body = poem_body.replace(yizuo[0], '')
                    poem_body = poem_body.replace('\n', '')
                    poem_body = poem_body.replace('<br />', '\n')
                    poem_body = poem_body.replace('<p>', '')
                    poem_body = poem_body.replace('</p>', '')

                    print('第' + str(cnt+1) + '首\t' + poem_name)
                    cnt += 1

                    dic['name'] = poem_name
                    dic['author'] = poem_author
                    dic['poem'] = poem_body
                    poem_lst.append(dic)
                except:
                    gushi_total_list.pop()
        with open("poem.json", 'a', encoding='utf-8') as f:
            for i in poem_lst:
                f.write(json.dumps(i, ensure_ascii=False))
                f.write('\n')


# 利用马青公式计算n位的pi
def get_pi(number):
    number1 = number+10  # 多计算10位，防止尾数取舍的影响
    b = 10**number1  # 算到小数点后number1位
    x1 = b*4//5  # 求含4/5的首项
    x2 = b // -239  # 求含1/239的首项
    he = x1+x2  # 求第一大项
    number *= 2  # 设置下面循环的终点，即共计算n项
    for i in range(3, number, 2):  # 循环初值=3，末值2n,步长=2
        x1 //= -25  # 求每个含1/5的项及符号
        x2 //= -57121  # 求每个含1/239的项及符号
        x = (x1+x2) // i  # 求两项之和
        he += x  # 求总和
        pai = he*4  # 求出π
    pai //= 10**10  # 舍掉后十位
    paistring = str(pai)
    result = paistring[0]+str('.')+paistring[1:len(paistring)]
    return result


def fhl():
    poem_lst = [[] for _ in range(10)]
    zi = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    with open("poem.json", 'r', encoding="utf-8") as f:
        lst = f.readlines()
        for i in lst:
            poem = dict(json.loads(i))['poem']
            # 去掉一作
            yizuo = re.compile('.*(\(.*?\)).*').findall(
                poem)
            try:
                poem = poem.replace(yizuo[0], '')
            except:
                pass
            if '\u3000' in poem:
                poem = poem.replace("\u3000", '')
            poem = poem.split('\n')
            for p in poem:
                for j in range(10):
                    if zi[j] in p:
                        poem_lst[j].append(p)
                        break
    n = int(input('请输入飞花令长度:'))
    ling = get_pi(n).replace('.', '')
    for i in ling:
        print('%s : %s' % (i, poem_lst[int(i)][0]))
        del poem_lst[int(i)][0]


if __name__ == "__main__":
    # get_poem()
    fhl()
