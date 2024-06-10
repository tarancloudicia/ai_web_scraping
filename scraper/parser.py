def parse_product_page(soup):
    products = []
    for product in soup.select('.product'):
        name = product.select_one('.product-name').text
        price = product.select_one('.product-price').text
        review = product.select_one('.product-review').text
        products.append({
            'name': name,
            'price': price,
            'review': review
        })
    return products
