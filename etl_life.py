# Data Cleaning
import pandas as pd


def get_data():
    """ 
        Reads CSV file into a DataFrame.
    """    
    raw_df = pd.read_csv("Life Expectancy Data.csv")
    return raw_df


def clean_data(raw_df):
    """
        Function that cleans the dataset including renaming, dropping, and filling columns
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

    # We think it makes sense to drop the following columns because these columns won't be necessary help us 
    # predict which country has lower life expectancy rate in order to find out 
    # if densely populated countries do have lower expenctancy rate. 
    # These dropped rows explain more of the reason behind the death
    # The columns we will be working with are Country,Status,Life,Expectancy,Adult Mortality,GDP, Population, Schooling and Country_int. 
    # We also chose the columns that has a high colleration rate to life expectancy based on the heatmap from Exploratory Data Analysis section
    df = df.drop(['Year', 'Infant Deaths', 'Alcohol','Percentage Expenditure', 'Hepatitis B', 'Measles','BMI', 'under-five deaths ','Polio', 'Total expenditure', 'Diphtheria', ' HIV/AIDS', 'Thinness 1-19 years', 'Thinness 5-9 years','Income composition of resources'], axis=1)


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
    df.drop(columns="Country", inplace=True)

    return df


def main():
    """
        Main function that gets and cleans data
    """
    raw_df = get_data()
    df = clean_data(raw_df)
    df.to_csv('cleaned_Life Expectancy Data.csv', index=False)


if __name__ == "__main__":
    main()