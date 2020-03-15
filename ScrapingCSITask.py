import requests
from lxml import html, etree, xpath


def load_task_page():
    r = requests.get(url)
    f = open(task_id + '.html', 'w', encoding='cp1251')
    f.write(r.text)
    return task_id, url


def parse_task():
    results = {}
    file = open(task_id + '.html', 'r')
    parser = etree.HTMLParser()
    #tree = html.fromstring(file)
    for item in html.xpath('.//td/b/../following-sibling::td'):
        result[item.xpath('preceding-sibling::td')[0].text_content().strip()] = item.text_content().strip()

    # print(task_info)


task_id = '1638125'  # input('Input Task number')
url = 'https://support.crystals.ru/SelfService/Claim/' + task_id + '?guid=569296a7-c02f-45cb-9edd-2ae8be68fba4'
#load_task_page()
parse_task()
