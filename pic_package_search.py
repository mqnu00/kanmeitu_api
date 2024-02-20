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
            'url': pic_package_url
        })
    pic_package_info_list = {
        'searchid': search_id,
        'result': res
    }
    return pic_package_info_list


if __name__ == '__main__':
    print(pic_package_search('女仆'))
