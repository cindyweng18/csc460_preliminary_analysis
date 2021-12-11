# Data Cleaning
import pandas as pd
import numpy as np


def get_data():
    """ 
        Reads CSV file into a DataFrame.
    """    
    raw_df = pd.read_csv("Life Expectancy Data.csv")
    population_df = pd.read_csv("world_population.csv",  index_col='Country Name')
    return raw_df, population_df


def clean_population_data(population_df):
    """
        Cleans population dataset with what we need for life expectations dataset by
        dropping unneccessary columns, and renaming countries to match our dataset
    """
    # Drop all columns except data from 2000-2015
    population_df.drop(['Country Code', 'Indicator Name', 'Indicator Code','1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
                    '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977','1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
                    '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995','1996', '1997', '1998', '1999','2016', '2017', '2018', '2019', '2020'], axis=1, inplace=True)

    # Rename country names
    population_df.rename(index={
    'Bahamas, The': 'Bahamas',
    'Bolivia': 'Bolivia (Plurinational State of)',
    "Cote d'Ivoire": "Côte d'Ivoire",
    'Czech Republic': 'Czechia',
    "Korea, Dem. People's Rep.": "Democratic People's Republic of Korea",
    'Congo, Dem. Rep.':'Democratic Republic of the Congo',
    'Congo, Rep.': 'Congo',
    'Egypt, Arab Rep.': 'Egypt',
    'Iran, Islamic Rep.':'Iran (Islamic Republic of)',
    'Kyrgyz Republic': 'Kyrgyzstan',
    'Lao PDR': "Lao People's Democratic Republic",
    'Micronesia, Fed. Sts.': 'Micronesia (Federated States of)',
    'Korea, Rep.':'Republic of Korea',
    'St. Kitts and Nevis':'Saint Kitts and Nevis',
    'St. Lucia': 'Saint Lucia',
    'Moldova':'Republic of Moldova',
    'St. Vincent and the Grenadines':'Saint Vincent and the Grenadines',
    'Slovak Republic':'Slovakia',
    'North Macedonia':'The former Yugoslav republic of Macedonia',
    'United States': 'United States of America',
    'United Kingdom': 'United Kingdom of Great Britain and Northern Ireland',
    'Venezuela, RB': 'Venezuela (Bolivarian Republic of)',
    'Vietnam': 'Viet Nam',
    'Yemen, Rep.': 'Yemen',
    'Tanzania': 'United Republic of Tanzania',
    'Gambia, The': 'Gambia'
    }, inplace=True)

    # Reset index to numbers than country names
    population_df.reset_index(inplace=True)

    return population_df


def clean_data(raw_df, population_df):
    """
        Function that cleans the dataset including renaming, dropping, and filling columns
        and updates population values from the population_df
    """

    # Rename columns 
    df = raw_df.rename(columns={
    "Life expectancy ": "Life Expectancy",
    "infant deaths": "Infant Deaths",
    "percentage expenditure": "Percentage Expenditure",
    "Measles ": "Measles",
    " BMI ": "BMI",
    "under-five deaths": "Under-five Deaths",
    "Diphtheria ":"Diphtheria",
    " thinness  1-19 years": "Thinness 1-19 years",
    " thinness 5-9 years": "Thinness 5-9 years"
    })

    # Create list of countries and years
    countries = df['Country'].unique()
    years = df['Year'].unique()

    # Replace population value to the one from population_df
    for country in countries:
        for year in years:
            try:
                row = population_df.loc[population_df['Country Name'] == country]
                ind = row.index[0]
                population = int(row[str(year)][ind])
                df.loc[(df['Country'] == country) & (df['Year'] == year), 'Population'] = population
            except:
                df.loc[(raw_df['Country'] == country) & (df['Year'] == year), 'Population'] = np.NaN

        # We think it makes sense to drop the following columns because these columns won't be necessary help us 
    # predict which country has lower life expectancy rate in order to find out 
    # if densely populated countries do have lower expenctancy rate. 
    # These dropped rows explain more of the reason behind the death
    # The columns we will be working with are Country,Status,Life,Expectancy,Adult Mortality,GDP, Population, Schooling and Country_int. 
    # We also chose the columns that has a high colleration rate to life expectancy based on the heatmap from Exploratory Data Analysis section
    df.drop(['Year', 'Infant Deaths', 'Alcohol','Percentage Expenditure', 'Hepatitis B', 'Measles','BMI', 'under-five deaths ','Polio', 'Total expenditure', 'Diphtheria', ' HIV/AIDS', 'Thinness 1-19 years', 'Thinness 5-9 years','Income composition of resources'], axis=1, inplace=True)
    
    # Fill null values with mean values
    for column in df.columns:
        if df[column].isnull().any() == True:
            df[column].fillna(value=df[column].mean(), inplace=True)
    
    # One-Hot Encode 'Status' columns. Set developing to 0 and developed to 1
    df['Status'] = df['Status'].replace(['Developing'],'0')
    df['Status'] = df['Status'].replace(['Developed'],'1')

    # Integer encoding for countries column where every country gets a different number, assigned the encoded variable to a new column 'Country_int' using the cat.codes accessor.
    # We converted the Country column to a category, then use those category values for your label encoding
    df["Country"] = df["Country"].astype('category')
    df["Country_int"] = df["Country"].cat.codes
    countries_codes = df[['Country','Country_int']]
    df.drop(columns="Country", inplace=True)

    return df, countries_codes


def main():
    """
        Main function that gets and cleans data
    """
    raw_df, raw_population_df = get_data()
    population_df = clean_population_data(raw_population_df)
    df, countries_codes = clean_data(raw_df, population_df)
    df.to_csv('cleaned_Life Expectancy Data.csv', index=False)
    countries_codes.to_csv('countries_codes.csv', index=False)


if __name__ == "__main__":
    main()