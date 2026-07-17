import matplotlib.pyplot as plt

# Data for Interest Coverage Ratios
years = ['March 2023', 'March 2024']
interest_coverage_ratios = [18.7, 29.5]  # Replace these values with actual data if available

# Create the bar chart
plt.figure(figsize=(8, 7))
plt.bar(years, interest_coverage_ratios, color=['blue', 'red'])

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Interest Coverage Ratio')
plt.title('Comparison of Interest Coverage Ratio (March 2023 vs March 2024)')

# Display the value on top of each bar
for i in range(len(interest_coverage_ratios)):
    plt.text(i, interest_coverage_ratios[i] + 1, str(round(interest_coverage_ratios[i], 1)), ha='center')

# Show the plot
plt.tight_layout()
plt.show()
