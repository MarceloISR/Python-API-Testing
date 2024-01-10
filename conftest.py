"""Fixture to share accross all the test scenarios a Base_Request object"""
import pytest

from src.requests.base_request import Base_Request


@pytest.fixture
def Req():
    return Base_Request()
