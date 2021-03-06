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

                    print('???' + str(cnt+1) + '???\t' + poem_name)
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


# ????????????????????????n??????pi
def get_pi(number):
    number1 = number+10  # ?????????10?????????????????????????????????
    b = 10**number1  # ??????????????????number1???
    x1 = b*4//5  # ??????4/5?????????
    x2 = b // -239  # ??????1/239?????????
    he = x1+x2  # ???????????????
    number *= 2  # ??????????????????????????????????????????n???
    for i in range(3, number, 2):  # ????????????=3?????????2n,??????=2
        x1 //= -25  # ????????????1/5???????????????
        x2 //= -57121  # ????????????1/239???????????????
        x = (x1+x2) // i  # ???????????????
        he += x  # ?????????
        pai = he*4  # ????????
    pai //= 10**10  # ???????????????
    paistring = str(pai)
    result = paistring[0]+str('.')+paistring[1:len(paistring)]
    return result


def fhl():
    poem_lst = [[] for _ in range(10)]
    zi = ['???', '???', '???', '???', '???', '???', '???', '???', '???', '???']
    with open("poem.json", 'r', encoding="utf-8") as f:
        lst = f.readlines()
        for i in lst:
            poem = dict(json.loads(i))['poem']
            # ????????????
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
    n = int(input('????????????????????????:'))
    ling = get_pi(n).replace('.', '')
    for i in ling:
        print('%s : %s' % (i, poem_lst[int(i)][0]))
        del poem_lst[int(i)][0]


if __name__ == "__main__":
    # get_poem()
    fhl()
