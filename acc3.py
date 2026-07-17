import matplotlib.pyplot as plt
import pandas as pd

'''# Data for Comparative Balance Sheet (simplified for demonstration)
data_balance_sheet = {
    'Year': ['Mar 24', 'Mar 23', 'Mar 22', 'Mar 21', 'Mar 20'],
    'Total Assets': [7458.08, 8321.12, 5710.07, 5707.07, 5395.09],  # in Rs. Cr
    'Shareholder\'s Funds': [4447.19, 3044.39, 2684.49, 2480.31, 2463.44],
    'Non-Current Liabilities': [1508.15, 4196.57, 4531.27, 2517.48, 2469.69],
    'Current Liabilities': [1502.74, 1044.61, 560.84, 673.73, 539.51]
}

# Data for Comparative Profit & Loss Account (simplified for demonstration)
data_profit_loss = {
    'Year': ['Mar 24', 'Mar 23', 'Mar 22', 'Mar 21', 'Mar 20'],
    'Revenue from Operations (Net)': [11768.88, 7597.70, 3818.27, 2011.80, 3141.09],
    'Other Operating Revenues': [157.68, 117.49, 62.46, 35.73, 36.58],
    'Total Revenue': [12277.49, 8126.89, 4159.70, 2251.77, 3329.43],
    'Profit/Loss Before Tax': [1873.32, 710.51, 323.00, -72.14, 245.52]
}

# Convert the balance sheet and profit & loss data to DataFrames for easier handling
df_balance_sheet = pd.DataFrame(data_balance_sheet)
df_profit_loss = pd.DataFrame(data_profit_loss)

# Plotting Comparative Balance Sheet

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Bar chart for Comparative Balance Sheet
df_balance_sheet.set_index('Year').plot(kind='bar', stacked=True, ax=ax[0], width=0.8)
ax[0].set_title('Comparative Balance Sheet')
ax[0].set_ylabel('Amount (Rs. Cr)')
ax[0].set_xlabel('Year')
ax[0].legend(title='Balance Sheet Components')

# Plotting Comparative Profit & Loss Account

# Line chart for Comparative Profit & Loss
df_profit_loss.set_index('Year').plot(kind='line', ax=ax[1], marker='o')
ax[1].set_title('Comparative Profit & Loss Account')
ax[1].set_ylabel('Amount (Rs. Cr)')
ax[1].set_xlabel('Year')
ax[1].legend(title='P&L Items')

# Display the plots
plt.tight_layout()
plt.show()
'''
'''
import matplotlib.pyplot as plt
import pandas as pd

# Data for Comparative Balance Sheet (simplified for demonstration)
data_balance_sheet = {
    'Year': ['Mar 24', 'Mar 23', 'Mar 22', 'Mar 21', 'Mar 20'],
    'Total Assets': [7458.08, 8321.12, 5710.07, 5707.07, 5395.09],  # in Rs. Cr
    'Shareholder\'s Funds': [4447.19, 3044.39, 2684.49, 2480.31, 2463.44],
    'Non-Current Liabilities': [1508.15, 4196.57, 4531.27, 2517.48, 2469.69],
    'Current Liabilities': [1502.74, 1044.61, 560.84, 673.73, 539.51]
}

# Data for Comparative Profit & Loss Account (simplified for demonstration)
data_profit_loss = {
    'Year': ['Mar 24', 'Mar 23', 'Mar 22', 'Mar 21', 'Mar 20'],
    'Revenue from Operations (Net)': [11768.88, 7597.70, 3818.27, 2011.80, 3141.09],
    'Other Operating Revenues': [157.68, 117.49, 62.46, 35.73, 36.58],
    'Total Revenue': [12277.49, 8126.89, 4159.70, 2251.77, 3329.43],
    'Profit/Loss Before Tax': [1873.32, 710.51, 323.00, -72.14, 245.52]
}

# Convert the balance sheet and profit & loss data to DataFrames for easier handling
df_balance_sheet = pd.DataFrame(data_balance_sheet)
df_profit_loss = pd.DataFrame(data_profit_loss)

# Plotting Comparative Balance Sheet
plt.figure(figsize=(10, 6))
df_balance_sheet.set_index('Year').plot(kind='bar', stacked=True, width=0.8)
plt.title('Comparative Balance Sheet')
plt.ylabel('Amount (Rs. Cr)')
plt.xlabel('Year')
plt.legend(title='Balance Sheet Components')
plt.tight_layout()
plt.show()

# Plotting Comparative Profit & Loss Account
plt.figure(figsize=(10, 6))
df_profit_loss.set_index('Year').plot(kind='line', marker='o')
plt.title('Comparative Profit & Loss Account')
plt.ylabel('Amount (Rs. Cr)')
plt.xlabel('Year')
plt.legend(title='P&L Items')
plt.tight_layout()
plt.show()
'''
'''
import matplotlib.pyplot as plt
import pandas as pd

# Data for Common Size Balance Sheet (simplified for demonstration)
data_balance_sheet = {
    'Year': ['Mar 24', 'Mar 23', 'Mar 22', 'Mar 21', 'Mar 20'],
    'Total Assets': [7458.08, 8321.12, 5710.07, 5707.07, 5395.09],  # in Rs. Cr
    'Shareholder\'s Funds': [4447.19, 3044.39, 2684.49, 2480.31, 2463.44],
    'Non-Current Liabilities': [1508.15, 4196.57, 4531.27, 2517.48, 2469.69],
    'Current Liabilities': [1502.74, 1044.61, 560.84, 673.73, 539.51]
}

# Data for Common Size Profit & Loss Account (simplified for demonstration)
data_profit_loss = {
    'Year': ['Mar 24', 'Mar 23', 'Mar 22', 'Mar 21', 'Mar 20'],
    'Revenue from Operations (Net)': [11768.88, 7597.70, 3818.27, 2011.80, 3141.09],
    'Other Operating Revenues': [157.68, 117.49, 62.46, 35.73, 36.58],
    'Total Revenue': [12277.49, 8126.89, 4159.70, 2251.77, 3329.43],
    'Profit/Loss Before Tax': [1873.32, 710.51, 323.00, -72.14, 245.52]
}

# Convert the balance sheet and profit & loss data to DataFrames for easier handling
df_balance_sheet = pd.DataFrame(data_balance_sheet)
df_profit_loss = pd.DataFrame(data_profit_loss)

# Common Size Calculation for Balance Sheet (relative to Total Assets)
df_balance_sheet_common_size = df_balance_sheet.copy()
df_balance_sheet_common_size.set_index('Year', inplace=True)
df_balance_sheet_common_size = df_balance_sheet_common_size.apply(
    lambda x: x / x['Total Assets'] * 100, axis=1
)

# Common Size Calculation for Profit & Loss Account (relative to Total Revenue)
df_profit_loss_common_size = df_profit_loss.copy()
df_profit_loss_common_size.set_index('Year', inplace=True)
df_profit_loss_common_size = df_profit_loss_common_size.apply(
    lambda x: x / x['Total Revenue'] * 100, axis=1
)

# Plotting Common Size Balance Sheet
plt.figure(figsize=(10, 6))
df_balance_sheet_common_size.plot(kind='bar', stacked=True, width=0.8)
plt.title('Common Size Balance Sheet')
plt.ylabel('Percentage (%)')
plt.xlabel('Year')
plt.legend(title='Balance Sheet Components')
plt.tight_layout()
plt.show()

# Plotting Common Size Profit & Loss Account
plt.figure(figsize=(10, 6))
df_profit_loss_common_size.plot(kind='line', marker='o')
plt.title('Common Size Profit & Loss Account')
plt.ylabel('Percentage (%)')
plt.xlabel('Year')
plt.legend(title='P&L Items')
plt.tight_layout()
plt.show()
'''
'''
import matplotlib.pyplot as plt
import pandas as pd

# Data for Profit & Loss Account for Mar 24 and Mar 23 (simplified)
data_profit_loss_comparison = {
    'Item': [
        'Revenue from Operations (Net)',
        'Other Operating Revenues',
        'Total Revenue',
        'Profit/Loss Before Tax'
    ],
    'Mar 24': [11768.88, 157.68, 12277.49, 1873.32],  # Mar 24 values
    'Mar 23': [7597.70, 117.49, 8126.89, 710.51]     # Mar 23 values
}

# Convert the data to a DataFrame for easier handling
df_profit_loss_comparison = pd.DataFrame(data_profit_loss_comparison)

# Set the 'Item' column as the index
df_profit_loss_comparison.set_index('Item', inplace=True)

# Plotting the comparison of P&L for Mar 23 and Mar 24 using bar chart
df_profit_loss_comparison.plot(kind='bar', width=0.8)
plt.title('Comparison of Profit and Loss Account (Mar 23 vs Mar 24)')
plt.ylabel('Amount (Rs. Cr)')
plt.xlabel('P&L Items')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()
'''
'''
import matplotlib.pyplot as plt
import pandas as pd

# Data for Balance Sheet Comparison for Mar 24 and Mar 23 (simplified)
data_balance_sheet_comparison = {
    'Item': [
        'Total Assets',
        'Shareholder\'s Funds',
        'Non-Current Liabilities',
        'Current Liabilities'
    ],
    'Mar 24': [7458.08, 4447.19, 1508.15, 1502.74],  # Mar 24 values
    'Mar 23': [8321.12, 3044.39, 4196.57, 1044.61]     # Mar 23 values
}

# Convert the data to a DataFrame for easier handling
df_balance_sheet_comparison = pd.DataFrame(data_balance_sheet_comparison)

# Set the 'Item' column as the index
df_balance_sheet_comparison.set_index('Item', inplace=True)

# Plotting the comparison of Balance Sheet for Mar 23 and Mar 24 using bar chart
df_balance_sheet_comparison.plot(kind='bar', width=0.8)
plt.title('Comparison of Balance Sheet (Mar 23 vs Mar 24)')
plt.ylabel('Amount (Rs. Cr)')
plt.xlabel('Balance Sheet Items')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()
'''
import matplotlib.pyplot as plt
import pandas as pd

# Data for Balance Sheet (Mar 23 and Mar 24)
balance_sheet_data = {
    'Item': [
        'Shareholder\'s Funds', 'Non-Current Liabilities', 'Current Liabilities', 
        'Non-Current Assets', 'Current Assets'
    ],
    'Mar 24': [4447.19, 1508.15, 1502.74, 4500.65, 2957.43],  # in Cr
    'Mar 23': [3079.94, 4196.57, 1044.61, 4407.43, 3321.12]   # in Cr
}

# Convert to DataFrame
balance_df = pd.DataFrame(balance_sheet_data)

# Plotting Balance Sheet Comparison (Mar 23 vs Mar 24)
plt.figure(figsize=(10, 6))
plt.plot(balance_df['Item'], balance_df['Mar 24'], label='Mar 24', marker='o')
plt.plot(balance_df['Item'], balance_df['Mar 23'], label='Mar 23', marker='o')
plt.title('Balance Sheet Comparison: Mar 23 vs Mar 24')
plt.xlabel('Balance Sheet Items')
plt.ylabel('Amount (in ₹ Cr)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Data for Profit & Loss (Mar 23 and Mar 24)
pnl_data = {
    'Item': [
        'Revenue from Operations [Net]', 'Other Operating Revenues', 'Total Operating Revenues',
        'Other Income', 'Total Revenue', 'Total Expenses', 'Profit Before Tax', 'Profit After Tax'
    ],
    'Mar 24': [11768.88, 157.68, 11926.56, 350.93, 12277.49, 10947.52, 1873.32, 1435.82],  # in Cr
    'Mar 23': [7597.70, 117.49, 7715.19, 411.70, 8126.89, 7416.38, 710.51, 554.57]   # in Cr
}

# Convert to DataFrame
pnl_df = pd.DataFrame(pnl_data)

# Plotting Profit & Loss Comparison (Mar 23 vs Mar 24)
plt.figure(figsize=(10, 6))
plt.plot(pnl_df['Item'], pnl_df['Mar 24'], label='Mar 24', marker='o')
plt.plot(pnl_df['Item'], pnl_df['Mar 23'], label='Mar 23', marker='o')
plt.title('Profit & Loss Comparison: Mar 23 vs Mar 24')
plt.xlabel('Profit & Loss Items')
plt.ylabel('Amount (in ₹ Cr)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

