import requests


#################### Test response 200 ##########################

def test_get_Swager_UI_check_status_code_equals_200():
    response = requests.get('http://localhost:888/')
    assert response.status_code == 200


def test_get_namespace_1_status_code_equals_200():
    response = requests.get('http://localhost:888/VideoGamesSales/')
    assert response.status_code == 200


def test_get_namespace_2and_platform_status_code_equals_200():
    response = requests.get('http://localhost:888/VideoGamesSales/Platform/Wii')
    assert response.status_code == 200


def test_get_Name_check_status_code_equals_200():
    response = requests.get('http://localhost:888/VideoGamesSales/?Genre=Sports')
    assert response.status_code == 200


def test_get_Genre_check_status_code_equals_200():
    response = requests.get('http://localhost:888/VideoGamesSales/?Name=Wii%20Sports')
    assert response.status_code == 200


def test_get_Platform_check_status_code_equals_200():
    response = requests.get('http://localhost:888/VideoGamesSales/?Platform=Wii')
    assert response.status_code == 200


def test_get_Year_check_status_code_equals_200():
    response = requests.get('http://localhost:888/VideoGamesSales/?Year=2006')
    assert response.status_code == 200


def test_get_Year_greater_check_status_code_equals_200():
    response = requests.get(
        'http://localhost:888/VideoGamesSales/?Column_to_filter=Year&Greater_than=2000&Less_than=2006')
    assert response.status_code == 200


def test_get_Na_sales_greater_status_code_equals_200():
    response = requests.get(
        'http://localhost:888/VideoGamesSales/?Column_to_filter=NA_Sales&Greater_than=1&Less_than=10')
    assert response.status_code == 200


def test_get_EU_Sales_greater_status_code_equals_200():
    response = requests.get(
        'http://localhost:888/VideoGamesSales/?Column_to_filter=EU_Sales&Greater_than=1&Less_than=10')
    assert response.status_code == 200


def test_get_JP_sales_greater_status_code_equals_200():
    response = requests.get(
        'http://localhost:888/VideoGamesSales/?Column_to_filter=JP_Sales&Greater_than=1&Less_than=10')
    assert response.status_code == 200


def test_get_Other_sale_greater_status_code_equals_200():
    response = requests.get(
        'http://localhost:888/VideoGamesSales/?Column_to_filter=Other_Sales&Greater_than=1&Less_than=10')
    assert response.status_code == 200


def test_get_Global_sales_greater_status_code_equals_200():
    response = requests.get(
        'http://localhost:888/VideoGamesSales/?Column_to_filter=Global_Sales&Greater_than=1&Less_than=10')
    assert response.status_code == 200


def test_get_sort_status_code_equals_200():
    response = requests.get('http://localhost:888/VideoGamesSales/?Sort=Name')
    assert response.status_code == 200


def test_get_sort_descending_status_code_equals_200():
    response = requests.get('http://localhost:888/VideoGamesSales/?Sort=Name&Descending=True')
    assert response.status_code == 200


def test_get_everything_together_status_code_equals_200():
    response = requests.get(
        'http://localhost:888/VideoGamesSales/?Name=Wii%20Sports&Platform=Wii&Year=2006&Genre=Sports&Publisher=Nintendo&Column_to_filter=Year&Greater_than=1999&Less_than=2010&Sort=Name&Descending=True')
    assert response.status_code == 200


#################### Test responses 400 ##########################


def test_get_ns_2_wrong_platform_status_code_equals_400():
    response = requests.get('http://localhost:888/VideoGamesSales/Platform/ii')
    assert response.status_code == 400


def test_get_no_result_status_code_equals_400():
    response = requests.get('http://localhost:888/VideoGamesSales/?Name=xyz')
    assert response.status_code == 400


def test_get_sorting_params_mising_status_code_equals_400():
    response = requests.get('http://localhost:888/VideoGamesSales/?Descending=True')
    assert response.status_code == 400


def test_get_greater_than_missing_params_status_code_equals_400():
    response = requests.get('http://localhost:888/VideoGamesSales/?Column_to_filter=EU_Sales&Greater_than=4')
    assert response.status_code == 400


#################### Test if data is JSON ##########################

def test_get_check_content_type_equals_json():
    response = requests.get('http://localhost:888/VideoGamesSales/?Year=2006')
    assert response.headers['Content-Type'] == 'application/json'


##################### check lenght of database ######################
def test_get_check_lenght_of_a_database():
    response = requests.get('http://localhost:888/VideoGamesSales/')
    response_body = response.json()

    assert len(response_body) == 16598


##################### check if function desc is working ######################
def test_get_check_if_function_desc_is_working():
    response = requests.get('http://localhost:888/VideoGamesSales/?Genre=Sports&Sort=Year&Descending=True')
    response_body = response.json()
    Year = response_body[0]
    assert Year['Year'] == 2016


##################### check if function greater than, less than is working ######################
def test_get_check_if_function_greater_than_less_than_is_working():
    response = requests.get(
        'http://localhost:888/VideoGamesSales/?Column_to_filter=Year&Greater_than=2000&Less_than=2006&Sort=Year&Descending=True')
    response_body = response.json()
    Name = response_body[0]
    assert Name['Name'] == 'Wii Sports'
