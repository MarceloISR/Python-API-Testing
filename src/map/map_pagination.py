

from enum import Enum
from typing import Optional, List


class Urls:
    first: str
    last: str
    prev: str
    next: str

    def __init__(self, first: str, last: str, prev: str, next: str) -> None:
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next


class Pagination:
    page: int
    pages: int
    per_page: int
    items: int
    urls: Urls

    def __init__(self, page: int, pages: int, per_page: int, items: int, urls: Urls) -> None:
        self.page = page
        self.pages = pages
        self.per_page = per_page
        self.items = items
        self.urls = urls


class Community:
    want: int
    have: int

    def __init__(self, want: int, have: int) -> None:
        self.want = want
        self.have = have


class Name(Enum):
    ALL_MEDIA = "All Media"
    BOX_SET = "Box Set"
    CASSETTE = "Cassette"
    CD = "CD"
    DVD = "DVD"
    VINYL = "Vinyl"


class Format:
    name: Name
    qty: int
    text: Optional[str]
    descriptions: Optional[List[str]]

    def __init__(self, name: Name, qty: int, text: Optional[str], descriptions: Optional[List[str]]) -> None:
        self.name = name
        self.qty = qty
        self.text = text
        self.descriptions = descriptions


class Genre(Enum):
    ELECTRONIC = "Electronic"
    FOLK_WORLD_COUNTRY = "Folk, World, & Country"
    JAZZ = "Jazz"
    ROCK = "Rock"


class Style(Enum):
    ALTERNATIVE_ROCK = "Alternative Rock"
    ELECTRO = "Electro"
    GRUNGE = "Grunge"
    INDIE_ROCK = "Indie Rock"
    PUNK = "Punk"
    SWING = "Swing"


class Title(Enum):
    NIRVANA_NEVERMIND = "Nirvana - Nevermind"
    NIRVANA_NEVERMIND_30_TH_ANNIVERSARY_EDITION = "Nirvana - Nevermind (30th Anniversary Edition)"
    NIRVANA_NEVERMIND_THE_SINGLES = "Nirvana - Nevermind - The Singles"
    TITLE_NIRVANA_NEVERMIND = "Nirvana - Nevermind "
    VARIOUS_NIRVANA_S_NEVERMIND_REVISITED_BY_GREEK_BANDS = "Various - Nirvana's Nevermind - Revisited By Greek Bands"


class TypeEnum(Enum):
    RELEASE = "release"


class Result:
    country: str
    genre: List[Genre]
    format: List[str]
    style: List[Style]
    id: int
    label: List[str]
    type: TypeEnum
    barcode: List[str]
    master_id: int
    master_url: Optional[str]
    uri: str
    catno: str
    title: Title
    thumb: str
    cover_image: str
    resource_url: str
    community: Community
    format_quantity: int
    formats: List[Format]
    year: Optional[int]

    def __init__(self, country: str, genre: List[Genre], format: List[str], style: List[Style], id: int, label: List[str], type: TypeEnum, barcode: List[str], master_id: int, master_url: Optional[str], uri: str, catno: str, title: Title, thumb: str, cover_image: str, resource_url: str, community: Community, format_quantity: int, formats: List[Format], year: Optional[int]) -> None:
        self.country = country
        self.genre = genre
        self.format = format
        self.style = style
        self.id = id
        self.label = label
        self.type = type
        self.barcode = barcode
        self.master_id = master_id
        self.master_url = master_url
        self.uri = uri
        self.catno = catno
        self.title = title
        self.thumb = thumb
        self.cover_image = cover_image
        self.resource_url = resource_url
        self.community = community
        self.format_quantity = format_quantity
        self.formats = formats
        self.year = year


class MAP_Pagination:
    pagination: Pagination
    results: List[Result]

    
    def __init__(self, pagination: Pagination, results: List[Result]) -> None:
        self.pagination = pagination
        self.results = results
