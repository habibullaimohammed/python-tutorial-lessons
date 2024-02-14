amazon_url = "https://www.amazon.com/apple-iphone-15-pro-max-128gb-black/dp/803JGSGD7V"

start_index_url = amazon_url.index('com/') + 4
end_index_url = amazon_url.index('/dp')

product_name = amazon_url[start_index_url:end_index_url]
product_name = product_name.replace('-', ' ')
product_name = product_name.title()

print('\nProduct Name:', product_name, '\n')
