# 介绍

爬取kanmeitu的网站数据，通过flask实现api。

# 已实现的功能

## 搜索功能

```
request:
	keyboard        搜索词
	page            搜索第几页
	search_id       搜索词对应的id
response:
    search_id       搜索词对应的id
    result          由图包(pic_package)组成的列表
    count           图包数
    totalPage       搜索总共的页数
```

## 查看图包所有图片功能

```
request:
	url				显示图包图片的网址
response:
	pic_url_list	图包所有的图片
```

