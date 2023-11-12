import pandas as pd

# get input and exit when type 'exit'
def get_input():
    user_inputs = []
    while True:
        user_input = input('Enter a menu (type "exit" to finish): ')
        if user_input.lower() == 'exit':
            break
        else:
            user_inputs.append(user_input)
    return user_inputs

# try to read csv file
try:
    df = pd.read_csv('menu.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=['name_menu'])

# get input
if df.empty:
    df['name_menu'] = get_input()
else:
    new_inputs = get_input()
    df = pd.concat([df, pd.DataFrame(new_inputs, columns=['name_menu'])], ignore_index=True)

# drop duplicates
df = df.drop_duplicates()

# save to csv
df.to_csv('menu.csv', index=False)
