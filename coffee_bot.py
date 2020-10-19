from utils import print_message, get_size, order_latte

def coffee_bot():
  print('Welcome to the cafe!')
  order_drink = 'y'
  drinks = []
  while order_drink == 'y':
    size = get_size()  
    drink_type = get_drink_type()
    
    drink = f'{size} {drink_type}'
    print(f'Alright, that\'s a {drink}!')
    while True:
      drinks.append(drink)
      order_drink = input('Would you like to order another drink? (y/n) \n>')
      order_drink = order_drink.lower()
      if order_drink in ['y', 'n']:
        break

  name = input('Can I get your name please? \n> ')
  print(f'Thanks, {name}! Your order will be ready shortly.')
  
  print('Okay, so I have:')
  for drink in drinks:
    print('-', drink)
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  res = res.lower()
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()
  
# Order Mocha
def order_mocha():
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n>')
    res = res.lower()
    if res == 'a':
      return 'peppermint mocha'
    elif res == 'b':
      return 'mocha'
    print_message()
coffee_bot()










