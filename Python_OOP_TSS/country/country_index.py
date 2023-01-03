import os

with open('country_name.txt', 'r') as f:
    countries = f.readlines()

for country in countries:
    first_l = country[0].lower()

    if os.path.exists(f'{first_l}.txt'):
        with open(f'{first_l}.txt', 'a') as f:
            f.write(country)

    else:
        with open(f'{first_l}.txt', 'w') as f:
            f.write(country)
