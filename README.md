# **REDBUS Project**


## Overview
This project focuses on extracting real-time bus route data using Selenium, followed by data processing with pandas and storage in a MySQL database. A dynamic Streamlit web application is then developed to allow users to filter and view bus route information based on various criteria, providing an interactive and user-friendly experience. This project focuses on providing real-time bus route information through a comprehensive process:

1. **Data Extraction:** Utilizes Selenium to scrape real-time bus route data from various sources.
2. **Data Processing:** Employs pandas to process and clean the extracted data, ensuring accuracy and relevance.
3. **Database Storage:** Saves the processed data into a MySQL database for efficient retrieval and management.
4. **Interactive Application:** Develops a dynamic web application that allows users to filter and view bus route information based on different criteria.
5. **Streamlit App:** The application is named **EASYBUS - Data Scraping and Filtering Application**, designed to offer an intuitive and interactive user experience.
<img src="images/logo.png" width="100" height="auto" />




## How It Works
1. **Data Extraction:**
   - **Routes Extraction:** Extracts routes and links for buses from multiple states.
   - **Bus Details Extraction:** Scrapes detailed information about all the buses from each and every extracted route.

2. **Data Processing:**
   - **DataFrame Creation and Cleaning:** Combines and cleans the data into a structured format using pandas by integrating sources and data cleaning.
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
- `bus_data_pipeline.ipynb`: Jupyter Notebook for data scraping and cleaning.
- `prescraped_bus_data.csv`: CSV file containing pre-scraped data.
- `requirements.txt`: Project dependencies.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: Project overview and instructions (this file).

## How to Run
1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
3. Install Dependencies from requirements.txt
4. You have two options for preparing the database:
   
   Run the codes in bus_data_pipeline.ipynb and populate the database:
- 	Extract bus route data.
- 	Clean and process the data.
- 	Store the data in the MySQL database.

   Option 2: Use the Provided CSV File**
-  Download the CSV file `prescraped_bus_data.csv` from the project directory.
-  Import the CSV file into your MySQL database.
  
5. Run the Streamlit Application:
  	```bash
   streamlit run path/to/your/Home.py
   
Notes:
Ensure that the database name is redbusschema and the table name is easy_bus_data for the Streamlit application to work correctly.

## Screenshots
### Home Page
![Home Page](./screenshots/Home_page.png)

### Search Bus Page
![Search Bus Page](./screenshots/Searchbus_page.png)

### All filters
<img src="./screenshots/Filters.png" alt="Filters" width="400" height="300">
