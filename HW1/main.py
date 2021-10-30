import requests as req

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    res = req.get(url)
    print(res.text)