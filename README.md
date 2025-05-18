# Video Game Database

## Overview

This project involves building a video game database using the **ETL (Extract, Transform, Load)** process. The data was sourced by web scraping from [Metacritic](https://www.metacritic.com/), a popular website for game reviews and ratings.

## Technologies and Libraries

- **Python Libraries:** `requests`, `BeautifulSoup`, `pandas`, `datetime`, `CSV`, `time`
- **Database Management System:** PostgreSQL
- **Database Interface:** PG Admin

## Process

1. **Extract:** Data was scraped using `requests` and `BeautifulSoup` libraries.
2. **Transform:** Data was cleaned, formatted, and structured using `pandas` and `datetime`.
3. **Load:** The transformed data was loaded into a PostgreSQL database using PG Admin.

## ERD Diagram

Below is the ERD diagram for the database structure:

![ERD Diagram](./db_images/ERD_diagram.png)

## Sample Queries

- Example queries demonstrating data retrieval and aggregation are below:

![Top 5 Games Query](./db_images/top_5_games_query.png)

![Top 5 Games](./db_images/top_5_games_output.png)

![Top 3 Publishers Query](./db_images/top_3_publishers_query.png)

![Top 3 Publishers](./db_images/top_3_publishers_output.png)

![Average Scores by Genre Query](./db_images/average_score_genre_query.png)

![Average Scores by Genre ](./db_images/average_score_by_genre.png)

![After Release Date Query](./db_images/after_release_date_query.png)

![After Release Date](./db_images/after_release_date_condition.png)

![Total Sales by Region Query](./db_images/total_sales_regions_query.png)

![Total Sales by Region](./db_images/total_sales_regions_output.png)