from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
import requests
import pytest


class TestCreateBooking(object):

    def test_create_booking_tc1(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, expect_data=200)
        bookingid = response.json()["bookingid"]
        print(bookingid)

    def test_create_booking_tc2(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload={}, in_json=False)
        verify_http_status_code(response, expect_data=500)
