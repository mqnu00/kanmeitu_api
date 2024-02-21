import bs4
from urllib.parse import urljoin
from utils.requests_utils import requests_util
from bs4 import BeautifulSoup
import base_data


def pic_package_search(keyboard=None, page=0, search_id=None):
    response = None

    if search_id is None:
        data = base_data.search_data
        data['keyboard'] = keyboard
        # 爬取搜索结果
        response = requests_util.requests_method(
            url=base_data.search_post_url,
            method='post',
            cnt=3,
            data=data
        )
        # 搜索结果链接
        search_res_url = response.headers['Location']
        # 获取search_id
        search_id = search_res_url[search_res_url.find('searchid=') + len('searchid='):]

    # 已知道page和search_id，可以直接获取搜索结果
    search_res_url = base_data.search_get_url.format(page, search_id)
    response = requests_util.requests_method(
        url=search_res_url,
        method='get',
        cnt=3
    )

    response = BeautifulSoup(response.content, 'html.parser')

    # 获取图包个数
    pic_package_count = response.find('div', class_='b')
    pic_package_count = str(pic_package_count.text)
    pic_package_count = pic_package_count[pic_package_count.find('（')+1:pic_package_count.find('组图')]
    pic_package_count = int(pic_package_count)
    # 获取总页数
    pic_package_total_page = int(pic_package_count / 20)
    if pic_package_count % 20 > 0:
        pic_package_total_page = pic_package_total_page + 1

    # 获取当前页的图包网址列表 pic_package_info_list
    pic_package_info_list = response.find('div', id='list')
    pic_package_info_list = pic_package_info_list.ul
    res = []
    for pic_package_info in pic_package_info_list:

        if type(pic_package_info) is bs4.element.NavigableString:
            continue

        # 获取图包名称
        pic_package_name = pic_package_info.a.get('title')
        # 获取图包封面图链接
        pic_package_preview_url = urljoin('https://', pic_package_info.a.img.get('src'))
        # 获取图包链接
        pic_package_url = str(pic_package_info.a.get('href'))
        pic_package_url = urljoin(base_data.base_url, pic_package_url)

        res.append({
            'name': pic_package_name,
            'preview': pic_package_preview_url,
            'url': pic_package_url,
        })
    pic_package_info_list = {
        'searchid': search_id,
        'result': res,
        'count': pic_package_count,
        'totalPage': pic_package_total_page
    }
    print(pic_package_count, pic_package_total_page)
    return pic_package_info_list


def pic_package_total_url(pic_package_url):

    pic_package_url = pic_package_url

    response = requests_util.requests_method(
        url=pic_package_url,
        method='get'
    )

    response = BeautifulSoup(response.content, 'html.parser')

    # 图包图片数
    pic_package_count = response.findAll('div', class_='pagelist')[1].p.b.span.text
    pic_package_count = str(pic_package_count)
    pic_package_count = pic_package_count.split('/')[1]
    pic_package_count = int(pic_package_count)
    print(pic_package_count)

    # 将图包网址修改成可遍历
    pic_package_url = pic_package_url.replace('.html', '_{}.html')

    for i in range(2, pic_package_count + 1):

        now_url = pic_package_url.format(i)
        print(now_url)
        response = requests_util.requests_method(
            url=now_url,
            method='get'
        )
        response = BeautifulSoup(response.content, 'html.parser')
        # 获取第i张图片的网址
        pic_url = response.find('img').get('src')

        print(pic_url)


if __name__ == '__main__':
    print(pic_package_total_url('https://www.sfjpg.net/mm/59489.html'))
