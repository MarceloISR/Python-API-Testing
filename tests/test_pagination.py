
import pytest

from src.requests.api_endpoints import EndPoints
from src.requests.base_request import Base_Request, Methods

"""Fixture to share accross all the test scenarios a Base_Request object"""
@pytest.fixture
def Req():
    return Base_Request()

"""Scenario 1: Default page size (50)."""
@pytest.mark.pagination
def test_default_page_size(Req: Base_Request):
    #Send a search request without specifying a page size.
    response = Req.request(Methods.GET, EndPoints.SEARCH )
    assert response.status_code == 200, "the request was not successfull"
    pagination = response.json()["pagination"]

    #Assert that the response contains the default number of results per page (as defined in the specs)
    assert pagination["per_page"] == 50, "the default value per page should be 50"

    #Assert that the response includes a link to the last and next pages
    assert len(pagination["urls"]) > 1
    assert "last" in pagination["urls"], "link 'last' does not appear in pagination"
    assert "next" in pagination["urls"], "link 'next' does not appear in pagination"


"""Scenario 2: Custom page size (20) """
@pytest.mark.pagination
def test_custom_page_size(Req: Base_Request):
    #Send a search request with a specified page size.
    response = Req.request(Methods.GET, EndPoints.SEARCH, params={'per_page':'20', 'page':'2'})
    assert response.status_code==200, "the request was not successfull"
    pagination= response.json()["pagination"]

    #Assert that the response contains the requested number of results.
    assert pagination["per_page"] == 20, f"per_page value should be 20, instead of {pagination['per_page']}"
    assert pagination["page"] == 2, f"page value should be 2 instead of {pagination["page"]}"

    #Assert that the response includes a link to the first, last, prev and next page 
    assert "first" in pagination["urls"], "link 'first' does not appear in pagination"
    assert "last" in pagination["urls"], "link 'last' does not appear in pagination"
    assert "prev" in pagination["urls"], "link 'prev' does not appear in pagination"
    assert "next" in pagination["urls"], "link 'next' does not appear in pagination"


"""Scenario 3: Pagination with filtering"""
#test tags
@pytest.mark.pagination
@pytest.mark.search_endpoing
@pytest.mark.filtering
def test_pagination_with_filtering(Req: Base_Request):
    params={"q":"Nirvana", "type":"release", "title":"nevermind", "country":"canada","year":"1991", "genre":"Rock"}

    #Send a search request with artist filtering or other specified filtering options.
    response = Req.request(Methods.GET, EndPoints.SEARCH, params=params)
    assert response.status_code==200, "the request was not successfull"
    pagination=response.json()["pagination"]
    results=response.json()["results"]
   
    #Assertion 1: that the response only includes results matching the filter criteria.
    for index, val in enumerate(results):
        assert val["type"]=="release", f"the item at the possition {index} has a different type value, actual={val['type']} expected 'release'"
        assert val["title"]=="Nirvana - Nevermind" , f"the item at the possition {index} has a different title value, actual={val['title']} expected 'Nirvana - Nevermind'"
        assert val["country"]=="Canada" , f"the item at the possition {index} has a different country value, actual={val['country']} expected 'Canada'"
        assert val["year"]=="1991" , f"the item at the possition {index} has a different year value, actual={val['year']} expected '1991'"
        assert val["genre"][0]=="Rock", f"the item at the possition {index} has a different genre value, actual={val['genre'][0]} expected 'genre'"

    #Assert that pagination works correctly within the filtered results.
    assert pagination["items"] == len(results)
    assert len(pagination["urls"]) == 0, "No pagination links should exists"


"""Scenario 4: Pagination with filtering 2"""
#test tags
@pytest.mark.pagination
@pytest.mark.filtering
def test_pagination_with_filtering2(Req: Base_Request):
    #adding full title
    params={"q":"Nirvana", "type":"release", "title":"Nirvana - Nevermind", "country":"canada","year":"1991", "genre":"Rock"}

    #Send a search request with artist filtering or other specified filtering options.
    response = Req.request(Methods.GET, EndPoints.SEARCH, params=params)
    assert response.status_code==200, "the request was not successfull"
    pagination=response.json()["pagination"]
    results=response.json()["results"]
   
    #Assertion 1: that the response only includes results matching the filter criteria.
    for index, val in enumerate(results):
        assert val["type"]=="release", f"the item at the possition {index} has a different type value, actual={val['type']} expected 'release'"
        assert val["title"]=="Nirvana - Nevermind" , f"the item at the possition {index} has a different title value, actual={val['title']} expected 'Nirvana - Nevermind'"
        assert val["country"]=="Canada" , f"the item at the possition {index} has a different country value, actual={val['country']} expected 'Canada'"
        assert val["year"]=="1991" , f"the item at the possition {index} has a different year value, actual={val['year']} expected '1991'"
        assert val["genre"][0]=="Rock", f"the item at the possition {index} has a different genre value, actual={val['genre'][0]} expected 'genre'"

    #Assert that pagination works correctly within the filtered results.
    assert pagination["items"] == len(results)
    assert len(pagination["urls"]) == 0, "No pagination links should exists"

