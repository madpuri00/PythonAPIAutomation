from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import requests
import pytest
import json
import os


class TestCreateBooking(object):

    def load_schema(self, schema_file):
        with open(schema_file, 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    def test_create_booking_jsonschema(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, expect_data=200)
        response_json = response.json()

        # Use this to get current directory and then add the copy of the path from content root
        # dir_schema = os.getcwd()
        # print(dir_schema)
        # json_schema = dir_schema + "/schema.json"
        schema = self.load_schema("/Users/Owner/PycharmProjects/pythonPy1xAPIAutomation/tests/json_schema/schema.json")

        try:
            validate(instance=response.json(), schema=schema)
        except ValidationError as e:
            print(e.message)
