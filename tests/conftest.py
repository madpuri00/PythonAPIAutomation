import pytest
import requests
from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code


@pytest.fixture(scope="session")
def create_token(self):
    response = post_requests(url=APIConstants.url_create_token(), auth=None, payload=payload_create_token(),
                             headers=common_headers_json(), in_json=False)
    print(response)
    verify_http_status_code(response, expect_data=200)
    token = response.json()["token"]
    print(token)
    verify_response_key_should_not_be_none(token)
    return token


@pytest.fixture(scope="class")
def create_booking(self):
    response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                             payload=payload_create_booking(), in_json=False)
    print(response)
    verify_response_key_should_not_be_none(response.json()["bookingid"])
    verify_http_status_code(response, expect_data=200)
    bookingid = response.json()["bookingid"]
    print(bookingid)
    return bookingid
