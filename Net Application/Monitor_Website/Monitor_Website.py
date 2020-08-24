from urllib.request import urlopen

# Monitor Website

try:
        #raise BaseException("....")   # raise ErrorType(" Error Message ")
        html = urlopen("http://192.168.1.228")
        print(html)

except Exception as e:
        print(e)
