import requests

from MyHTMLParser import MyHTMLParser

if __name__ == '__main__':
    parser = MyHTMLParser()
    # parser.feed('<html><head><title>Test</title></head>'
    #             '<body><h1>Parse me!</h1></body></html>')
    r = requests.get('https://www.udemy.com/course/forex-algorithmic-trading-course-code-a-forex-robot/')
    # print(r.content)
    parser.feed(r.content.decode())
