# %% tags=["parameters"]
upstream = None
product = None

# %%
import requests
response = requests.get("https://docs.dagster.io/assets/cereal.csv")
with open(product['data'], 'wb') as out_file:
    out_file.write(response.content)
