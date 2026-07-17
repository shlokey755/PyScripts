'''import matplotlib.pyplot as plt
import numpy as np

# Data for the ratios in 2023 and 2024
ratios_2024 = [44.5, 11.3, 11.7, 1.58, 4.51]
ratios_2023 = [44.46, 9.3, 6.8, 0.91, 3.22]
ratios_labels = ['Gross Profit Margin (%)', 'Operating Profit Margin (%)', 'Net Profit Margin (%)', 
                 'Asset Turnover Ratio', 'Inventory Turnover Ratio']

# Create a bar chart to compare the ratios for 2023 and 2024
x = np.arange(len(ratios_labels))  # Label positions
width = 0.35  # Width of the bars

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, ratios_2024, width, label='2024', color='b')
rects2 = ax.bar(x + width/2, ratios_2023, width, label='2023', color='r')

# Add labels, title, and custom x-axis tick labels
ax.set_xlabel('Ratios')
ax.set_ylabel('Values')
ax.set_title('Comparison of Financial Ratios for 2023 and 2024')
ax.set_xticks(x)
ax.set_xticklabels(ratios_labels, rotation=45, ha="right")
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
'''
'''import matplotlib.pyplot as plt
import numpy as np

# Liquidity Ratios Data for 2023 and 2024
ratios_2024 = [1.76, 1.02]  # Current Ratio and Quick Ratio for 2024
ratios_2023 = [1.68, 0.92]  # Current Ratio and Quick Ratio for 2023
ratios_labels = ['Current Ratio', 'Quick Ratio']

# Create a bar chart to compare the ratios for 2023 and 2024
x = np.arange(len(ratios_labels))  # Label positions
width = 0.35  # Width of the bars

# Plotting
fig, ax = plt.subplots(figsize=(8, 5))
rects1 = ax.bar(x - width/2, ratios_2024, width, label='2024', color='b')
rects2 = ax.bar(x + width/2, ratios_2023, width, label='2023', color='r')

# Add labels, title, and custom x-axis tick labels
ax.set_xlabel('Liquidity Ratios')
ax.set_ylabel('Values')
ax.set_title('Comparison of Liquidity Ratios for 2023 and 2024')
ax.set_xticks(x)
ax.set_xticklabels(ratios_labels)
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
'''
'''
import matplotlib.pyplot as plt

# Debt to Equity Ratio Data for 2023 and 2024
debt_to_equity_ratio_2024 = 0.21
debt_to_equity_ratio_2023 = 0.22

# Labels for pie chart
labels = ['2023', '2024']
sizes = [debt_to_equity_ratio_2023, debt_to_equity_ratio_2024]
colors = ['#ff9999', '#66b3ff']  # Colors for each section

# Create a pie chart
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax.set_title('Debt to Equity Ratio Comparison (2023 vs 2024)')

# Display the plot
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

# Data for profit margins in 2023 and 2024
gross_profit_margin_2024 = 44.5  # in percentage
operating_profit_margin_2024 = 11.3  # in percentage
net_profit_margin_2024 = 11.7  # in percentage

gross_profit_margin_2023 = 44.46  # in percentage
operating_profit_margin_2023 = 9.3  # in percentage
net_profit_margin_2023 = 6.8  # in percentage

# Labels for the profit margin categories
labels = ['Gross Profit Margin (%)', 'Operating Profit Margin (%)', 'Net Profit Margin (%)']

# Values for 2023 and 2024
ratios_2024 = [gross_profit_margin_2024, operating_profit_margin_2024, net_profit_margin_2024]
ratios_2023 = [gross_profit_margin_2023, operating_profit_margin_2023, net_profit_margin_2023]

# Bar chart positioning
x = np.arange(len(labels))  # Label positions
width = 0.35  # Width of the bars

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, ratios_2024, width, label='2024', color='b')
rects2 = ax.bar(x + width/2, ratios_2023, width, label='2023', color='r')

# Adding titles and labels
ax.set_xlabel('Profit Margins')
ax.set_ylabel('Percentage (%)')
ax.set_title('Profit Margin Comparison for 2023 and 2024')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

# Data for activity turnover ratios in 2023 and 2024
inventory_turnover_2024 = 7.55
asset_turnover_2024 = 1.7

inventory_turnover_2023 = 7.02
asset_turnover_2023 = 1.5

# Labels for the activity turnover categories
labels = ['Inventory Turnover', 'Asset Turnover']

# Values for 2023 and 2024
ratios_2024 = [inventory_turnover_2024, asset_turnover_2024]
ratios_2023 = [inventory_turnover_2023, asset_turnover_2023]

# Bar chart positioning
x = np.arange(len(labels))  # Label positions
width = 0.35  # Width of the bars

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, ratios_2024, width, label='2024', color='b')
rects2 = ax.bar(x + width/2, ratios_2023, width, label='2023', color='r')

# Adding titles and labels
ax.set_xlabel('Activity Turnover Ratios')
ax.set_ylabel('Ratio Values')
ax.set_title('Inventory and Asset Turnover Ratios Comparison for 2023 and 2024')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()
'''
import matplotlib.pyplot as plt

# Data for Interest Coverage Ratios
years = ['March 2023', 'March 2024']
interest_coverage_ratios = [18.7, 29.5]  # Replace these values with actual data if available

# Create the bar chart with adjusted figure size
plt.figure(figsize=(8, 6))  # Increase figure size for better spacing
plt.bar(years, interest_coverage_ratios, color=['blue', 'red'])

# Add labels and title
plt.xlabel('Year', fontsize=14)
plt.ylabel('Interest Coverage Ratio', fontsize=14)
plt.title('Comparison of Interest Coverage Ratio (March 2023 vs March 2024)', fontsize=16)

# Display the value on top of each bar


# Increase the spacing between the x-axis labels to avoid congestion
plt.xticks(rotation=0, ha='center', fontsize=12)

# Adjust layout to prevent overlap between labels and title
 # Increase the padding to give more space on top

# Show the plot
plt.show()

