import pandas as pd

df = pd.read_csv('acs2015_census_tract_data.csv', encoding='latin-1')
df = df[df['State'] != 'Puerto Rico']

print("Name: Sachin Chhetri")

# state with the highest density of each race category
race_categories = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']

print("\nPart 1:")
for race_category in race_categories:
    max_density_state = df.groupby('State')[race_category].sum() / df.groupby('State')['TotalPop'].sum()
    print(f"{race_category}: {max_density_state.idxmax()}")

# state with the highest and lowest unemployment
print("\nPart 2:")
highest_unemployment = df.loc[df['Unemployment'].idxmax(), 'State']
print(f"Highest Unemployment: {highest_unemployment}")
lowest_unemployment = df.loc[df['Unemployment'].idxmin(), 'State']
print(f"Lowest Unemployment: {lowest_unemployment}")

# Income inequality
print("\nPart 3:")
income_inequality = df[(df['Income'] >= 50000) & (df['Poverty'] > 50)]
income_inequality = income_inequality[['CensusTract', 'County', 'State'] + race_categories]
print(income_inequality)

# Mostly feminine
print("\nPart 4:")
feminine = df[(df['Women'] / df['TotalPop'] > 0.57) & (df['TotalPop'] >= 10000)]
feminine = feminine[['CensusTract', 'County', 'State'] + race_categories]
print(feminine)

# Most diverse racially
print("\nPart 5:")
diverse_tracts = df[(df[race_categories] > 0.15).sum(axis=1) >= 4]
diverse_tracts = diverse_tracts[['CensusTract', 'County', 'State'] + race_categories]
print(diverse_tracts)
