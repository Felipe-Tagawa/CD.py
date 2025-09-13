import pandas as pd
import numpy as np

ds = pd.read_csv("paises.csv", delimiter=";")

# Exercício 1:

# Procurar qualquer valor que contenha "OCEANIA"
oceania = ds[ds['Region'].str.contains("OCEANIA")]

print(oceania['Country'])
print("Total de países na Oceania:", len(oceania))

# Exercício 2:

biggerPopulation = ds.loc[ds['Population'].idxmax()]
print(biggerPopulation['Country'], biggerPopulation['Region']) # País com a maior população e região

#Exercício 3:

group_region = ds.groupby('Region')
LiteracyMean = group_region['Literacy (%)'].mean()
print(LiteracyMean)

# Exercício 4:

noCoast = ds[ds['Coastline (coast/area ratio)'] == 0]
noCoastCountry = noCoast['Country']
print(noCoastCountry)
noCoastCountry.to_csv('noCoast', sep=";")

# Exercício 5:
def deathFunction(deathrate):
    if deathrate < 9:
        return "Balanced"
    else:
        return "Urgent"
    
df = pd.DataFrame(ds)

df['Humanitarian Help'] = df['Deathrate'].apply(deathFunction)

# Países que precisam de auxílio:
print("Países que precisam de ajuda 'Urgent':")
urgentCountries = df[df['Humanitarian Help'] == 'Urgent']
print(urgentCountries[['Country', 'Deathrate', 'Humanitarian Help']])
print()

# Países que não precisam de auxílio:
print("Países classificados como 'Balanced':")
balanced_countries = df[df['Humanitarian Help'] == 'Balanced']
print(balanced_countries[['Country', 'Deathrate', 'Humanitarian Help']])
print()

print(df) # Mostrando no final pra confirmar que inseriu a tabela.
    


