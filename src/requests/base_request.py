from enum import Enum
import requests

from src.requests.api_endpoints import EndPoints
from utils.config import API_BASE_URL, CONFIG_HEADERS

class Methods(Enum):
    GET="GET"
    POST="POST"
    PUT="PUT"
    DELETE="DELETE"



class Base_Request:

    def set_headers(self, headers=None):
        self._headers = headers or CONFIG_HEADERS

    """store the request values"""
    def set_request(self, url: EndPoints, method: Methods | None= None, headers=None, params=None):
        self._url = f"{API_BASE_URL}/{url.value}"
        if method is not None:
            self._method=method.value
        else:
            self._method=method
        self._headers = headers or CONFIG_HEADERS
        self._params=params

    """generic method for using the request with different methods and endpoints"""
    def request(self,method: Methods,url: EndPoints,   headers=None, params=None):
        self.set_request(url, method, headers, params)
        return requests.request(url=self._url, method=self._method, params=self._params, headers=self._headers)