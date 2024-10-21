current_price = float(input('Current product price: '))
previous_price = float(input('Previous product price: '))

reduction = (previous_price-current_price)*100/previous_price

if reduction>10:
    print('Buy the product!!')
    print(f'Product price reduced by {reduction}%')
else:
    print(f'Reduction only {reduction}%, dont buy!')