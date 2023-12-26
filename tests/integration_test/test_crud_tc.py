from src.constants.api_constants import BASE_URL, APIConstants, base_url

import requests


def test_crud():
    print(BASE_URL)

    url = APIConstants.base_url()
    print(url)

    url_direct_func = base_url()
    print(url_direct_func)
