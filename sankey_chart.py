import pandas as pd
import plotly.graph_objects as go

# Define model nodes (the unique categories in this budget cashflow visualization- with no respect to the category 'levels').
nodes = ["Net Income", "Paycheck\nDeductions", "Employer\nDeductions", "Health Insurance", "Retirement\nContrubutions", "Taxes", "Gross Income", "Essential Costs", "Housing Costs", "Rent or Mortgage", "Utilities", "Maintenance", "Rental\nInsurance", "Living Costs", "Groceries", "Transportation", "Fuel", "Car Insurance", "Other\nInsurance", "Life\nInsurance", "Disability\nInsurance", "Miscellaneous\nEssentials", "Personal Care", "Clothing", "Non-essential\ncosts", "Comfort Costs", "Streaming", "Disposable Income", "Miscellaneous\nComfort", "Travel Fund", "Short trips\nand weekends", "Major Vacations", "Education and\nProfessional Development", "Miscellaneous\nnon-essential costs", "Savings and Debts", "Personal Retirement\nContrubutions", "Personal\nInvestments", "Emergency\nFund", "House\nDownpayment", "Student Loan\nPayments"]

# Define model links (define the network visualizations Sources, Targets, and Values).
links = {
    'source': 
        [0, 1, 1, 1, 1, 0, 6, 7, 8, 8, 8, 8, 7, 13, 13, 15, 15, 13, 18, 18, 13, 21, 21, 6, 24, 25, 25, 25, 24, 29, 29, 24, 24, 6, 34, 34, 34, 34, 34],
    'target': 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    'value': 
        [28, 8, 23, 4, 65, 72, 50, 50, 80, 11, 8, 1, 50, 40, 20, 60, 40, 20, 50, 50, 20, 50, 50, 30, 50, 20, 40, 40, 20, 40, 60, 15, 15, 20, 20, 20, 20, 20, 20]
}

# Define the colors of nodes
node_colors = ["grey", "blue", "teal", "teal", "teal", "teal", "grey", "red", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "orange", "green", "lime", "lime", "lime", "lime", "lime", "lime", "lime", "lime", "lime", "plum", "pink", "pink", "pink", "pink", "pink"]

# Created the DataFrame for the cashflow visualization by making a data table of the links between categories (sources and targets).
links_df = pd.DataFrame(links)

# Creates the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=25, #determine padding between nodes, vertically
        thickness=10, #sets thickness of the nodes themselves
        line=dict(color="black", width=0.5), #color and width of the node borders
        label=nodes,
        color=node_colors
    ),
    link=dict(
        source=links_df['source'],
        target=links_df['target'],
        value=links_df['value'],
        color="grey"
    ),
    arrangement="snap" # adjusts the arrangement of nodes to better group nodes in the same budget category. 
    )])

# update layout
fig.update_layout(
    title_text="Budget Cashflow Sankey Diagram",
    font_size=12,
    width=1200,
    height=800
    )

# Show the diagram
fig.show()