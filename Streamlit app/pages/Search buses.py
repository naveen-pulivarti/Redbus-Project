import streamlit as st
import mysql.connector
import pandas as pd

# Function to establish a connection to the MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="redbus_project"
    )

# Function to retrieve distinct city names from 'from' and 'to' columns in the database
def get_city_list(con):
    df_locations = pd.read_sql("SELECT DISTINCT `from`, `to` FROM the_bus_data", con)
    city_list = list(df_locations['from']) + list(df_locations['to'])
    return list(set(city_list))  # Remove duplicates

# Function to build the SQL query dynamically based on user filters
def build_query(min_seats, min_rating, min_price, max_price, from_location, to_location, categories, ac_checkbox, non_ac_checkbox, sort_options):
    query = "SELECT * FROM the_bus_data WHERE 1=1"
    
    # Adding conditions based on user inputs
    if min_seats > 0:
        query += f" AND seats_available >= {min_seats}"
    if min_rating > 1:
        query += f" AND star_rating >= {min_rating}"
    if min_price > 0 or max_price < 15000:
        query += f" AND price BETWEEN {min_price} AND {max_price}"
    if from_location:
        query += f" AND LOWER(`from`) LIKE CONCAT('%', LOWER('{from_location}'), '%')"
    if to_location:
        query += f" AND LOWER(`to`) LIKE CONCAT('%', LOWER('{to_location}'), '%')"
    if categories:
        if "Seater" in categories:
            query += " AND LOWER(bus_type) LIKE '%seater%' AND NOT LOWER(bus_type) LIKE '%sleeper%'"
        if "Sleeper/Semi Sleeper" in categories:
            query += " AND (LOWER(bus_type) LIKE '%sleeper%' OR LOWER(bus_type) LIKE '%semi sleeper%')"
    if ac_checkbox and not non_ac_checkbox:
        query += " AND LOWER(bus_type) NOT LIKE '%non%'"
    if non_ac_checkbox and not ac_checkbox:
        query += " AND LOWER(bus_type) LIKE '%non%'"

    # Adding sorting options
    if sort_options:
        if "Price: Low to High" in sort_options:
            query += " ORDER BY price ASC"
        if "Price: High to Low" in sort_options:
            query += " ORDER BY price DESC"
        if "Rating" in sort_options:
            query += " ORDER BY star_rating DESC"
    
    return query

# Function to format time columns and column names for better display
def format_time_columns(df):
    df['departing_time'] = df['departing_time'].apply(lambda x: str(x)[-8:-3])
    df['reaching_time'] = df['reaching_time'].apply(lambda x: str(x)[-8:-3])
    df.columns = [col.title().replace('_', ' ') for col in df.columns]
    return df

# Main function to render the Streamlit app
def main():
    st.sidebar.header("Filter")

    # Sidebar widgets for filtering options
    col1, col2 = st.sidebar.columns(2)
    ac_checkbox = col1.checkbox("AC")
    non_ac_checkbox = col2.checkbox("Non-AC")
    categories = st.sidebar.multiselect("Seating type", ["Sleeper/Semi Sleeper", "Seater"])
    min_seats = st.sidebar.slider("Minimum Seats Available", 0, 75, 0)
    min_rating = st.sidebar.slider("Minimum Star Rating", 1, 5, 0)
    min_price = st.sidebar.slider("Minimum Price", 0, 5000, 0)
    max_price = st.sidebar.slider("Maximum Price", 0, 15000, 15000)
    
    # Database connection and city list retrieval
    con = connect_to_database()
    city_list = get_city_list(con)

    # Dropdowns for selecting 'from' and 'to' locations
    from_location = st.sidebar.selectbox("From", options=[""] + city_list, index=0)
    to_location = st.sidebar.selectbox("To", options=[""] + city_list, index=0)

    # Multiselect for sorting options
    sort_options = st.sidebar.multiselect("Sort By", ["Price: Low to High", "Price: High to Low", "Rating"])

    # Build and execute the SQL query based on filters
    query = build_query(min_seats, min_rating, min_price, max_price, from_location, to_location, categories, ac_checkbox, non_ac_checkbox, sort_options)
    df = pd.read_sql(query, con)

    # Format and display the filtered data in the app
    df = format_time_columns(df)
    st.dataframe(df, height=550, width=1033)

# Run the app
main()
