import pandas as pd
import random

df = pd.read_csv('menu.csv')
df = df.drop_duplicates()

# Please enter the number of menu
num_menu = int(input('Enter the number of menu: '))

food = []
quantity = []
price = []
total = 0  # Initialize total

# Random menu
for i in range(num_menu):
    selected_food = random.choice(df['name_menu'].values)
    food.append(selected_food)
    
    selected_quantity = random.randint(1, 10)
    quantity.append(selected_quantity)
    
    selected_price = random.randint(50, 300)
    price.append(selected_price)
    
    total += selected_price * selected_quantity
    
    print(f'{i+1}. {selected_food} {selected_quantity} x {selected_price} = {selected_price * selected_quantity}')

print(f'Total: {total}')
