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

                poem_lst.append(dic)
            except:
                gushi_total_list.pop()
