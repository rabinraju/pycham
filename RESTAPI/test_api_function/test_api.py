# import pytest
# import requests
# from api_function.function import APIFunction
# from api_function.mock_data import testdata
#
# class TestAPIFunction:
#
#     @pytest.fixture
#     def setup(self):
#         self.url = "https://62513902977373573f4567fb.mockapi.io/pizza/pizza_names"
#         self.api_function = APIFunction(self.url)
#
#     def test_api_status(self, setup):
#         assert self.api_function.api_check_status() == 200
#     def test_fetch_headers(self,setup):

#
#     def test_fetch_api_data(self,setup):
#      assert self.api_function.fetch_api_data()== testdata.mock_data
import pytest
import requests
from api_function.function import APIFunction
from api_function.mock_data import testdata

class TestAPIFunction:
    @pytest.fixture
    def setup(self):
        self.url = "https://62513902977373573f4567fb.mockapi.io/pizza/pizza_names"
        self.api_function = APIFunction(self.url)

    def test_api_check_status(self,setup):
        assert self.api_function.api_check_status() == 200

    def  test_fetch_api_data(self,setup):
        assert self.api_function.fetch_api_data() == testdata.mock_data
    def test_fetch_api_header(self,setup):
        headers = self.api_function.fetch_api_header()
        assert headers['Server'] == 'Cowboy'

    def test_fetch_data_by_id(self,setup):
         result = self.api_function.fetch_data_by_id(23)
         assert result == testdata.mock_data23

    def test_insert_data(self,setup):
        data = {"food_name": "noodles", "country": "tamilnadu"}
        assert self.api_function.insert_data(data) == True

    def test_delete_data(self,setup):
        assert self.api_function.delete_data(3) == True






