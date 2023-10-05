import pandas as pd
import yfinance as yf
import numpy as np

# Download historical data for the NASDAQ index from 2000 to 2023
data = yf.download('^IXIC', start='2000-01-01', end='2023-09-30')

# Create a DataFrame with the required columns
df = pd.DataFrame(index=data.index)
df['date'] = data.index
df['cost_of_sales'] = data['Close'] * 0.75  # Assuming cost is 75% of closing price

# Add random noise to 'cost_of_sales'
noise = np.random.normal(0, 100, len(df))
df['cost_of_sales'] = df['cost_of_sales'] + noise

df['selling_price'] = data['Close']
df['net_profit'] = df['selling_price'] - df['cost_of_sales']

# Round the values to two decimal places
df = df.round(2)

# Define project names, categories and project status
project_names = ['Proj1', 'Proj2', 'Proj3','Proj4', 'Proj5', 'Proj6', 'Proj7','Proj8', 'Proj9']
project_categories = ['Category1', 'Category1', 'Category1','Category2', 'Category2', 'Category2', 'Category3','Category3', 'Category3']
project_status = ['In - Progress', 'In - Progress', 'In - Progress','In - Progress', 'On - hold', 'On - hold', 'On - hold','Completed', 'Completed']

# Assign project names, categories and project status to the DataFrame
df['project_name'] = np.random.choice(project_names, len(df))
df['project_category'] = df['project_name'].map(dict(zip(project_names, project_categories)))
df['project_status'] = df['project_name'].map(dict(zip(project_names, project_status)))

# Adjust the cost of sales based on project name
cost_adjustments = {'Proj9': 2.5, 'Proj5': 1.8}
for project, adjustment in cost_adjustments.items():
    df.loc[df['project_name'] == project, 'cost_of_sales'] *= adjustment

# Adjust the selling price based on project name
selling_price_adjustments = {'Proj9': 1.7, 'Proj5': 1.2}
for project, adjustment in selling_price_adjustments.items():
    df.loc[df['project_name'] == project, 'selling_price'] *= adjustment

# Save the DataFrame as a CSV file
df.to_csv('NASDAQ_data.csv', index=False)