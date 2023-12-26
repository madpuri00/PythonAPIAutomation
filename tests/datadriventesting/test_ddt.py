# Read the CSV or Excel file
# Create a Function create_token which can take values from the Excel file
# Verify the Expected result
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json
import requests
import pytest

# Read the Excel File - openpyxl
import openpyxl


# Step 1 Read the file and put the content into a []
def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})

    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url=APIConstants.url_create_token(), headers=common_headers_json(), json=payload)
    return response


@pytest.mark.parametrize("user_cred", read_credentials_from_excel("testdata_ddt.xlsx"))
def test_post_create_token(user_cred):
    # make_request_auth -> Run this for however many rows are available in the Excel file
    # file_path = "testdata_ddt.xlsx"
    # credentials = read_credentials_from_excel(file_path)
    # for user_cred in credentials:
    username = user_cred["username"]
    password = user_cred["password"]
    response = make_request_auth(username, password)
    # print(response)
    assert response.status_code == 200
