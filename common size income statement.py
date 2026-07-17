import matplotlib.pyplot as plt

# Data for Mar 24 and Mar 23
categories = [
    'Revenue From Operations (Gross)', 
    'Less: Excise/Service Tax/Other Levies', 
    'Revenue From Operations (Net)', 
    'Other Operating Revenues', 
    'Total Operating Revenues', 
    'Other Income', 
    'Total Revenue', 
    'Purchase of Stock-In-Trade', 
    'Changes in Inventories of FG, WIP, and Stock-In-Trade', 
    'Employee Benefit Expenses', 
    'Finance Costs', 
    'Depreciation and Amortisation Expenses', 
    'Other Expenses', 
    'Total Expenses', 
    'Profit Before Exceptional Items and Tax', 
    'Exceptional Items', 
    'Profit Before Tax', 
    'Tax Expenses', 
    'Profit After Tax'
]

# Percentages for Mar 24 and Mar 23
percentages_mar24 = [
    103.18, 7.63, 100.00, 1.34, 101.34, 2.98, 104.30, 57.04, 0, 7.97, 2.63, 
    5.42, 21.42, 92.99, 11.30, 4.62, 15.91, 3.72, 12.19
]

percentages_mar23 = [
    108.06, 8.09, 100.00, 1.55, 101.55, 5.42, 106.96, 62.23, 0, 7.64, 4.70, 
    6.10, 23.70, 97.60, 9.34, 0.00, 9.34, 2.05, 7.30
]

# Create a figure with two subplots


# Pie chart for Mar 24
ax1.pie(percentages_mar24, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
ax1.set_title('Mar 24: Common Size Income Statement (%)')

# Pie chart for Mar 23
ax2.pie(percentages_mar23, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
ax2.set_title('Mar 23: Common Size Income Statement (%)')

# Display the pie charts
plt.tight_layout()
plt.show()
