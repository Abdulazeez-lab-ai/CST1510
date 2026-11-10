# %%
# CST1440 Assessment 1 - Climate Data Analysis
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Abdul\Downloads\climate_data.csv")

# Keep only the columns we need for the assignment
keep_cols = ["geoAreaName", "timePeriodStart", "EN_ATM_GHGT_WLU", "EG_FEC_RNEW"]
df = df[keep_cols]

# Show what type of data is in each column
print("—— Data Types ——")
print(df.dtypes)

# Count any empty/missing values in each column
print("\n—— Missing Values ——")
print(df.isnull().sum())


# Question 1: UK renewable energy percentage in 2022
uk_data = df[(df["geoAreaName"] == "United Kingdom of Great Britain and Northern Ireland") & 
             (df["timePeriodStart"] == 2022)]
uk_renewable = uk_data["EG_FEC_RNEW"].values[0]
print(f"\nUK renewable energy in 2022: {uk_renewable:.2f}%")

# Question 2: Mauritius greenhouse gas emissions in 2020
mauritius_data = df[(df["geoAreaName"] == "Mauritius") & 
                    (df["timePeriodStart"] == 2020)]
mauritius_emissions = mauritius_data["EN_ATM_GHGT_WLU"].values[0]
print(f"Mauritius emissions in 2020: {mauritius_emissions:.4f} Mt CO2")

# Question 3: Which country had the highest renewable energy in 2023?
data_2023 = df[df["timePeriodStart"] == 2023]
data_2023_clean = data_2023.dropna(subset=["EG_FEC_RNEW"])
highest_row = data_2023_clean.loc[data_2023_clean["EG_FEC_RNEW"].idxmax()]
print(f"Highest renewable energy in 2023: {highest_row['geoAreaName']} at {highest_row['EG_FEC_RNEW']:.2f}%")



# Graph 1: Histogram of renewable energy percentages in 2020
plt.figure(figsize=(8, 5))
data_2020 = df[df["timePeriodStart"] == 2020]["EG_FEC_RNEW"]
data_2020_clean = data_2020.dropna()
plt.hist(data_2020_clean, bins=15, color="green", edgecolor="black")
plt.title("Distribution of Renewable Energy Share — 2020")
plt.xlabel("Percentage of Energy from Renewable Sources")
plt.ylabel("Number of Countries")
plt.show()

# Graph 2: Bar chart of top 10 emitting countries in 2021
plt.figure(figsize=(10, 6))
emissions_2021 = df[df["timePeriodStart"] == 2021].dropna(subset=["EN_ATM_GHGT_WLU"])
top_10_emitters = emissions_2021.nlargest(10, "EN_ATM_GHGT_WLU")
plt.bar(top_10_emitters["geoAreaName"], top_10_emitters["EN_ATM_GHGT_WLU"], color="red")
plt.title("Top 10 Countries by Greenhouse Gas Emissions — 2021")
plt.ylabel("Emissions (Megatonnes CO2)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Graph 3: Line chart showing renewable energy over time for selected countries
countries_list = [
    "United Kingdom of Great Britain and Northern Ireland",
    "Mauritius",
    "United Arab Emirates",
    "China",
    "Brazil",
    "Germany"
]

plt.figure(figsize=(10, 6))
for country_name in countries_list:
    country_data = df[df["geoAreaName"] == country_name].dropna(subset=["EG_FEC_RNEW"])
    plt.plot(country_data["timePeriodStart"], country_data["EG_FEC_RNEW"], 
             marker="o", label=country_name)
plt.title("Renewable Energy Percentage Over Time")
plt.xlabel("Year")
plt.ylabel("Percentage Renewable")
plt.legend(loc="best")
plt.grid(True, alpha=0.3)
plt.show()


# Get all the emissions data and remove any empty values first
all_emissions = df["EN_ATM_GHGT_WLU"].dropna()

print("\n—— Emissions Statistics ——")
print(f"Mean: {all_emissions.mean():.2f}")
print(f"Median: {all_emissions.median():.2f}")
print(f"Standard Deviation: {all_emissions.std():.2f}")
print(f"Minimum: {all_emissions.min():.4f}")
print(f"Maximum: {all_emissions.max():.2f}")
print(f"25th Percentile: {all_emissions.quantile(0.25):.2f}")
print(f"75th Percentile: {all_emissions.quantile(0.75):.2f}")
iqr = all_emissions.quantile(0.75) - all_emissions.quantile(0.25)
print(f"Interquartile Range (IQR): {iqr:.2f}")
# %%
