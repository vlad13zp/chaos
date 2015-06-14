import requests
from messcover.models import CrawlUrl, ParseUrls


def get_start_url():
    r = requests.get(
        'http://localhost:8001/api/route', auth=('admin', 'pro100vlad'))

    local_dict = r.json()

    return str(local_dict['results'][0]['start_route'])


def cut_string(string):
    local_url = string
    local_url = local_url[22:-1]
    if local_url == '':
        local_url = 'home'

    return local_url


def save_crawl(name_me, code_me):
    local_url = cut_string(name_me)
    need_url = CrawlUrl.objects.create(url=name_me,
                                       name=local_url,
                                       code=code_me)

    return need_url


def save_parse(items, items_name, need_url):
    i = 6
    while (i < len(items)):
        ParseUrls.objects.create(id_url=need_url,
                                 urls=items[i],
                                 name=items_name[i])
        i = i + 1
