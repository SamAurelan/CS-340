# CS-340

GRAZIOSO SALVARE – Austin Animal Center Rescue Dashboard
Project Documentation & Professional Reflection
1. PROJECT OVERVIEW AND ARCHITECTURE
This application was built for Grazioso Salvare, an international search-and-rescue organization, to identify and track dogs from the Austin Animal Center (AAC) dataset that are eligible for rescue training

An interactive web dashboard with data filtering tools, a data table, an analytics pie chart, and an interactive geographic map that was created using Plotly Dash.
The data access layer is a bespoke Python class (CRUD_Python_Module.py) that converts user interface filters into programmatic PyMongo database queries.

The ProjectTwoDashboard ipynb configures the layout using Dash HTML which defines the visual grid and interactive inputs.

1. SYSTEM SETUP AND CONFIGURATION
Prerequisites and Dependency Setup:
To deploy this application within your environment, install the required frameworks and database drivers via terminal shell commands:
pip install dash pandas plotly dash-leaflet pymongo

