# Life Expectancy

### Group Members
- Sanjida Nisha
- Nour Elabbasy
- Cindy Weng Zhu

### Repository Structure
List each file and what it's purpose it. Make sure you indicate where your data cleaning code and data dictionary are! 

For example:
- `data`
  - `Life Expectancy Data.csv`: Raw data from Life Expectancy Dataset
  - `cleaned_Life Expectancy Data.csv`: The cleaned and combined dataset for modeling. 
  - `data_dictionary.csv`: The data dictionary for cleaned dataset. 
- `code`
  - `etl_life.py`: Cleans `Life Expectancy Data.csv`
  - `exploratory_data_analysis.ipynb`: Includes descriptive statistics and charts. 

### Exploratory Analysis
Describe what work you have done so far and include the code. 

We described our dataset and observed if there were any missing values or any values that were out of range. There were missing values in certain columns and those were taken care of in the data cleaning section. We also encoded the object columns: Status and Country columns by using One-Hot encoding and Integer encoding respectively. We dropped certain columns that we will not be using for the modeling section. We also graphed some columns such as the Status column to see the percentage of Developed vs Developing countries in our dataset, the average life expectancy rate throughout the years, and the average life expectancy between developed and developing countries. In addition, we use Seaborn's Heatmap feature to map the correlation levels between our columns of our dataset and wrote down our observations from it.

### Challenges
Describe any challenges you've encountered so far. Let me know if there's anything you need help with!

* Some challenges that we encountered so far was what was the best way to deal with the Null values in our dataset without messing up the data itself, and what features we can use for our modes

### Future Work
Describe what work you are planning to complete for the final analysis.

For the final analysis, we are planning to 
* Build a Linear Regression model
* Discuss the result and the answer to our data science question
* Better understand what diseases cause life expectancy to decrease in developing countries (make use of other columns within the dataframe)

### Contributions
Describe the contributions that each group member made.

Sanjida, Nour, and Cindy worked on the data cleaning and exploratory analysis on Google Collab.
