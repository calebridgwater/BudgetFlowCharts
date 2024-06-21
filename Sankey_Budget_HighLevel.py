# This is a high-level copy of the more detailed Sankey diagram of budget cashflow. This diagram stops at 4 levels (nodes) of depth (only sub-category detail for major budget buckets). This less complex diagram will alllow me to play around more with the project without accidentally bugging the diagram because of unequal index match-ups for source, target, and values.

import pandas as pd
import plotly.graph_objects as go

# Define model nodes (the unique categories in this budget cashflow visualization- with no respect to the category 'levels').
nodes = ["Net Income", "Paycheck Deductions", 
         "Gross Income", "Essential Costs", 
         "Housing Costs",  "Living Costs",  
         "Non-essential costs", "Comfort Costs", 
         "Travel Fund", "Miscellaneous costs", 
         "Savings and Debts"]

# Define model links (define the network visualizations Sources, Targets, and Values).
links = {
    'source': 
        [0, 0, 2, 3, 3, 2, 6, 6, 6, 2],
    'target': 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'value': 
        [28, 72, 50, 50, 50, 30, 75, 10, 5, 20]
}

# Define the colors of nodes
node_colors = ["blue", "blue", "red", "orange", "orange", "green", "lime", "lime", "lime", "pink"]

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