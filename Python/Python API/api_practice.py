import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    content = response.json()

    if content["success"] and "data" in content:
        user_data = content["data"]
        user_gender = user_data["data"][0]["gender"]
        first_name = user_data["data"][0]["name"]["first"]
        last_name = user_data["data"][0]["name"]["last"]
        return user_gender, first_name, last_name
    else:
        raise Exception("Failed to fetch the uer data.")
    
def main():
    try:
        user_gender, first_name, last_name = fetch_random_user()
        print(f"Gender: {user_gender} \nName: {first_name} {last_name}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()