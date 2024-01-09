
"""Scenario 1: Default page size
Send a search request without specifying a page size or offset.
Assert that the response contains the default number of results per page (as defined in the specs).
Assert that the response includes a link to the next page or indicates no more results if applicable."""

"""Scenario 2: Custom page size
Send a search request with a specified page size.
Assert that the response contains the requested number of results.
Assert that the response includes a link to the next page or indicates no more results if applicable."""

"""Scenario 3: Pagination with filtering
Send a search request with artist filtering or other specified filtering options.
Assert that the response only includes results matching the filter criteria.
Assert that pagination works correctly within the filtered results.
note: test different filtering combinations to ensure pagination handles them accurately."""