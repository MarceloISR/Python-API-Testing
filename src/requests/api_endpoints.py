
from enum import Enum

"""List all the endpoints"""
class EndPoints(Enum):
    SEARCH = "/database/search"
    ARTIST = "/artists/"
    LISTING= "/marketplace/listings/"