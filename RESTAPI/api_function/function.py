import requests

class APIFunction:
    def __init__(self, url):
        self.url = url

    def api_check_status(self):
        response = requests.get(self.url)
        return response.status_code

    def fetch_api_data(self):
        if self.api_check_status() == 200:
            return requests.get(self.url).json()
        else:
            return None

    def fetch_api_header(self):
        if self.api_check_status() == 200:
            response = requests.get(self.url)
            return response.headers
        else:
            return None

    def fetch_data_by_id(self, id):
        if self.api_check_status() == 200:
            user_id = str(id)
            for data in self.fetch_api_data():
                if data["id"] == user_id:
                    return (data["id"], data["food_name"], data["country"])
            else:
                return None

    def insert_data(self, data):
        if self.api_check_status() == 200:
            response = requests.post(self.url, json=data)
            return response.status_code == 201
        return False

    def delete_data(self, id):
        if self.api_check_status() == 200:
            delete_url = f"{self.url}/{id}"
            response = requests.delete(delete_url)
            return response.status_code == 201
        return False



url = "https://62513902977373573f4567fb.mockapi.io/pizza/pizza_names"
my_api = APIFunction(url)
# data = {"food_name":"noodles","country":"tamilnadu"}
# print(my_api.api_check_status())
# print(my_api.fetch_api_data())
# print(my_api.fetch_api_header())
print(my_api.fetch_data_by_id(23))
# print(my_api.insert_data(data))
print(my_api.delete_data(2))