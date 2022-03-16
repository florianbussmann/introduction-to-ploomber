# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = ['1-get']
product = None

# %%
import csv
with open(upstream['1-get']['data'], 'r') as cereals_file:
    lines = cereals_file.read().split("\n")
    cereals = [row for row in csv.DictReader(lines)]

    sorted_by_sugar = sorted(cereals, key=lambda cereal: cereal["sugars"])
    print(f'{sorted_by_sugar[-1]["name"]} is the sugariest cereal')
