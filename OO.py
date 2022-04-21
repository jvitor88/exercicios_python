import pyshorteners

url = str(input('Copie a URL aqui'))
link = pyshorteners.Shortener(api_key='9680bd484401249a93f854ac4fa163906eab49f2')
result = link.tinyurl.short(link)
print(result)