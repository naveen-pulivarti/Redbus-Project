# REDBUS_PROJECT - Data Scraping and Filtering Application

## Overview

This project focuses on extracting real-time bus route data using Selenium, followed by data processing with pandas and storage in a MySQL database. A dynamic Streamlit web application is then developed to allow users to filter and view bus route information based on various criteria, providing an interactive and user-friendly experience.


## Features
- **Data Scraping:** Automatically extracts bus route details, including pricing, availability, and ratings.
- **Data Cleaning:** Processes and cleans the scraped data to ensure accuracy and usability.
- **Data Storage:** Stores cleaned data in a MySQL database.
- **Interactive Web Application:** Provides a web-based interface for users to filter and view bus data.

## How It Works
1. **Data Extraction:**
   - **Routes Extraction:** Extracts routes and links for buses from multiple states.
   - **Bus Details Extraction:** Scrapes detailed information about buses from the extracted routes.

2. **Data Processing:**
   - **DataFrame Creation and Cleaning:** Combines and cleans the data into a structured format using pandas.
   - **Data Storage:** Saves the processed data into a MySQL database for persistence and easy retrieval.

3. **Web Application:**
   - **Streamlit Application:** Develops an interactive web application using Streamlit for users to filter and view bus information.

## Technologies Used
- **Python:** Core programming language.
- **Selenium:** Web scraping tool.
- **Pandas:** Data manipulation and cleaning.
- **MySQL:** Database for storing the bus data.
- **Streamlit:** Framework for building the web application.




## Directory Structure
- `streamlit app/`: Contains the Streamlit application code.
- `SCRAPE_CLEAN_STORE_code.ipynb`: Jupyter Notebook for data scraping and cleaning.
- `requirements.txt`: Project dependencies.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: Project overview and instructions (this file).

## Installation
1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
3. Install Dependencies from requirements.txt
4. Run the codes in SCRAPE_CLEAN_STORE_code.ipynb and populate the database:
- 	Extract bus route data.
- 	Clean and process the data.
- 	Store the data in the MySQL database.
5. Run the Streamlit Application:
  	streamlit run path/to/your/Home.py

