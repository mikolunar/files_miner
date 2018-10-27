from lxml import html
import requests


def getSearch(url_string):
    results=[]

    page=requests.get("https://www.google.com/search?q=%dom")
    result=page.content
    tree=html.fromstring(result)

    return tree

def main():
    print(getSearch('test'))

if __name__=='__main__':
    main()




