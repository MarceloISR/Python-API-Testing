
import pytest

from utils.config import API_KEY, API_SECRET

from src.requests.api_endpoints import EndPoints
from src.requests.base_request import Base_Request, Methods


"""Scenario 1: Missing Authorization header 
 all the tests are using the fixture stored in conftest.py """
@pytest.mark.authorization
@pytest.mark.search_endpoing
def test_missing_authorization_secret(Req:Base_Request):
    # Send a search request without the Authorization header.
    _headers= {'Authorization': f"Discogs key={API_KEY}, secret=''"}
    response = Req.request(Methods.GET, EndPoints.SEARCH, headers=_headers)

    # Assert that the response status code is 401 Unauthorized.
    assert response.status_code==401, f'the status code should be 401 instead of {response.status_code}'
    # Assert that the response message indicates missing or invalid authorization."""
    assert response.json()["message"] == "Invalid consumer key/secret. Please register an app before making requests."


"""Scenario 2: Invalid Authorization header format """
@pytest.mark.authorization
@pytest.mark.search_endpoing
def test_invalid_authorization_header_format(Req:Base_Request):
    # Send a search request with an incorrectly formatted Authorization header (e.g., wrong format, missing Discogs text).
    _headers= {'Authorization': f"key={API_KEY}, secret={API_SECRET}"}
    response = Req.request(Methods.GET, EndPoints.SEARCH, headers=_headers)
    # Assert that the response status code is 401 Unauthorized.
    assert response.status_code==401, f'the status code should be 401 instead of {response.status_code}'
    # Assert that the response message indicates invalid authorization."""
    assert response.json()["message"] == "You must authenticate to access this resource."


"""Scenario 3: Expired session """
@pytest.mark.authorization
@pytest.mark.search_endpoing
@pytest.mark.skip(reason="Not implemented yet")
def test_expired_session(Req: Base_Request):
    # Send a search request with an expired session.
    # Assert that the response status code is 401 Unauthorized.
    # Assert that the response message indicates invalid authorization.
    None