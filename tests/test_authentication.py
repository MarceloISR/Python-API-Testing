"""Scenario 1: Missing Authorization header
        Send a search request without the Authorization header.
        Assert that the response status code is 401 Unauthorized.
        Assert that the response message indicates missing or invalid authorization."""

"""Scenario 2: Invalid Authorization header format
        Send a search request with an incorrectly formatted Authorization header (e.g., wrong token type, invalid token value).
        Assert that the response status code is 401 Unauthorized.
        Assert that the response message indicates invalid authorization."""

"""Scenario 3: Expired or revoked token
        Send a search request with an expired or revoked token.
        Assert that the response status code is 401 Unauthorized.
        Assert that the response message indicates invalid authorization."""