import pandas as pd
import plotly.graph_objects as go

# Define model nodes (the unique categories in this budget cashflow visualization- with no respect to the category 'levels').
nodes = ["Net Income", "Paycheck Deductions", "Employer-Sponsored Deductions", "Health Insurance", "Retirement Contrubutions", "Taxes", "Gross Income", "Essential Costs", "Housing Costs", "Rent or Mortgage", "Utilities", "Repairs and Maintenance", "Rental or Home Insurance", "Living Costs", "Groceries", "Transportation", "Fuel", "Car Insurance", "Other Insurance", "Life Insurance", "Disability Insurance", "Miscellaneous Essentials", "Personal Care and Health", "Clothing", "Non-essential costs", "Comfort Costs", "Streaming", "Disposable Income", "Miscellaneous Comfort", "Travel Fund", "Short trips and weekends", "Major Vacations", "Education and Professional Development Costs", "Miscellaneous non-essential costs", "Savings and Debts", "Personal Retirement Contrubutions", "Personal Investments", "Emergency Fund", "House Downpayment Fund", "Student Loan Payments"]

# Define model links (define the network visualizations Sources, Targets, and Values).
links = {
    'source': 
        [0, 1, 1, 1, 1, 0, 6, 7, 8, 8, 8, 8, 7, 13, 13, 15, 15, 13, 18, 18, 13, 21, 21, 6, 24, 25, 25, 25, 24, 29, 29, 24, 24, 6, 34, 34, 34, 34, 34],
    'target': 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    'value': 
        [28, 8, 23, 4, 65, 72, 50, 50, 80, 11, 8, 1, 50, 40, 20, 60, 40, 20, 50, 50, 20, 50, 50, 30, 50, 20, 40, 40, 20, 40, 60, 15, 15, 20, 20, 20, 20, 20, 20]
}

# Created the DataFrame for the cashflow visualization by making a data table of the links between categories (sources and targets).
links_df = pd.DataFrame(links)

# Creates the Sankey diagram
fig = go.Figure(data=[go.sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=nodes
    ),
    link=dict(
        source=links_df['source'],
        target=links_df['target'],
        value=links_df['value']
    ))])

# update layout
fig.update_layout(title_text="Budget Cashflow Sankey Diagram", font_size=12)

# Show the diagram
fig.show()