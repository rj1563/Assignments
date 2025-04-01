import requests
import logging
import psycopg2
import os
from dotenv import load_dotenv
import schedule
import time

# Load enviornment variables from .env file
load_dotenv()

# 1. Error Handling
# Defining url
url = "https://jsonplaceholder.typicode.com/end-point"

# Configure Logging
logging.basicConfig(
    filename="api_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def fetch_data_from_api(url):
    try:
        print(f"Making request to {url}")
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")

        if response.status_code != 200:
            raise requests.exceptions.HTTPError(f"API returned status code {response.status_code}")
    
        return response.json()

    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: {e}")
        logging.error(f"Timeout Error: {e}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        logging.error(f"Request Error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected Error: {e}")
        logging.error(f"Unexpected Error: {e}")
        raise

# Fetch data and handle errors
try:
    data = fetch_data_from_api(url)
except Exception as e:
    print(f"An error occurred: {e}")

# 2. Database Storage with PostgreSQL
    
# Connect to PostgreSQL
def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),

        )
        print("Database connection successful!")
        return connection
    except Exception as e:
        print(f"Error connecting to databse: {e}")
        return None
    
# Insert Users into PostgreSQL
def insert_users_to_db(users, connection):
    try:
        cursor= connection.cursor()
        for user in users:
            address= f"{user['address']['street']}, {user['address']['suite']}, {user['address']['city']}, {user['address']['zipcode']}" 

            cursor.execute("""
                           INSERT INTO Users (id, name, email, address)
                           VALUES( %s, %s, %s, %s)
                           ON CONFLICT (id) DO NOTHING;""",
                           (user['id'], user['name'], user['email'], address)
                           )
        connection.commit()
        cursor.close()
        print("User data inserted successfully.")
    except Exception as e:
        print(f"Error inserting user data: {e}")
        logging.error(f"Error inserting data: {e}")

# Insert Posts into PostgreSQL
def insert_posts_to_db(posts, connection):
    try:
        cursor= connection.cursor()
        for post in posts:
            cursor.execute("""
                           INSERT INTO Posts (id, user_id, title, body)
                           VALUES( %s, %s, %s, %s)
                           ON CONFLICT (id) DO NOTHING;""",
                           (post['id'], post['userId'], post['title'], post['body'])
                           )
        connection.commit()
        cursor.close()
        print("Post data inserted successfully.")
    except Exception as e:
        print(f"Error inserting post data: {e}")
        logging.error(f"Error inserting data: {e}")

# Scheduled API calls
def scheduled_task():
    try:
        posts = fetch_data_from_api("https://jsonplaceholder.typicode.com/posts")
        if not posts:
            print("No data fetched from the API.")
            return
        connection = connect_to_db()
        if connection is None:
            print("Failed to connect to database.")
            logging.error(f"Error during scheduled task: Failed to connect to the database at {time.ctime()}")
            return
        
        new_posts_count = 0
        cursor = connection.cursor()

        for post in posts:
            print(f"Checking post ID: {post['id']}")
            cursor.execute("SELECT id FROM posts WHERE id = %s", (post['id'],))
            if cursor.fetchone() is None:
                print(f"Post with ID {post['id']} does not exist in the database, inserting...")
                cursor.execute("""
                        INSERT INTO posts (id, user_id, title, body)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (id) DO NOTHING                
                        """, (post['id'], post['userId'], post['title'], post['body']))
                new_posts_count += 1
            else:
                print(f"Post with ID {post['id']} already exists in the database.")
        
        connection.commit()
        cursor.close()
        get_summary_report(connection)
        connection.close()

        print(f"Task completed. {new_posts_count} new posts added.")
        logging.info(f"Scheduled task executed at {time.ctime()} - {new_posts_count} new posts added.")

    except Exception as e:
        print(f"Error during scheduled task: {e}")
        logging.error(f"Error during scheduled task: {e} at {time.ctime()}")

# Scheduler: Run the scheduled task every 10 minutes
def run_scheduler():
    schedule.every(5).seconds.do(scheduled_task)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Summary Report
def get_summary_report(connection):
    try:
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM users;")
        total_users = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM posts;")
        total_posts = cursor.fetchone()[0]
        cursor.close()

        print("\n--- Summary Report ---")
        print(f"Total users in the database: {total_users}")
        print(f"Total posts in the database: {total_posts}")
    
    except Exception as e:
        print(f"Error generating summary report: {e}")
        logging.error(f"Error generating summary report: {e}")
        
# Main function to fetch data and store it
def main():
    try:
        users= fetch_data_from_api("https://jsonplaceholder.typicode.com/users")
        posts= fetch_data_from_api("https://jsonplaceholder.typicode.com/posts")        

        if users and posts:
            connection = connect_to_db()
            if connection:
                insert_users_to_db(users, connection)
                insert_posts_to_db(posts, connection)
                connection.close()
                print("Data successfully inserted into the database.")
            else:
                print("Failed to connect to the database.")
        else:
            print("Failed to fetch data from API")
    except Exception as e:
        print(f"An error occured: {e}")
        logging.error(f"Main function error: {e}")

if __name__ == "__main__":
    main()
    run_scheduler()