page = ('........<a href = "www.facebook.com"> </a>........)

start_link =(page.find('<a href'))#here be use find operator we do this for find acheive "postions
start_quote = (page.find('"',start_link))
start_quote = (page.find('"',start_link+1))    
url = (page[start_quote +1:end_quote])
print(url)
