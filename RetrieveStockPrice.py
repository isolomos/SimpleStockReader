import urllib.request
import re



while (True):
    number=input("Enter the number of stocks you want to search for ")
    number=int(number)
    symbols=[]
    for i in range(number):
        symbol=input("Enter the stocks you want ")
        symbols.append(symbol)


    
    i=0
    while (i<len(symbols)):

        url=symbols[i]
    
        htmlfile=urllib.request.urlopen('http://finance.yahoo.com/q?s='+url+'&fr=uh3_finance_web&uhb=uhb2')

        htmltext = htmlfile.read()

        codec = htmlfile.info().get_param('charset', 'utf8')
    
        htmltext = htmltext.decode(codec)

        regex = '<span id="yfs_l84_'+symbols[i]+'"(.+?)</span>'

        pattern = re.compile(regex)

        price = re.findall(pattern, htmltext)

        print(url, "price today is: ", price)

        i+=1

    query=input("Do you want to search for more prices? y/n ")
    if query in "yY":
        continue
    else:
        break





