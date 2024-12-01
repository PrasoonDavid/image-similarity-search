from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Key:
    display: str
    name: str
    kind: str
    logo: str

@dataclass
class Value:
    display: str
    count: int
    is_selected: bool
    value: str

@dataclass
class Filter:
    key: Key
    values: List[Value]

@dataclass
class Logo:
    type: str
    url: str

@dataclass
class Category:
    id: int
    uid: int
    name: str
    logo: Logo
    action: dict
    _custom_json: dict

@dataclass
class Media:
    type: str
    url: str
    alt: str

@dataclass
class Brand:
    type: str
    name: str
    logo: Logo
    action: dict
    _custom_json: dict

@dataclass
class Action:
    page: dict
    type: str

@dataclass
class Price:
    min: float
    max: float
    currency_code: str
    currency_symbol: str

@dataclass
class ItemPrice:
    marked: Price
    effective: Price

@dataclass
class Item:
    type: str
    attributes: dict
    categories: List[Category]
    medias: List[Media]
    name: str
    uid: int
    slug: str
    brand: Brand
    action: Action
    price: ItemPrice
    discount: str
    sellable: bool

@dataclass
class SortOn:
    display: str
    name: str
    logo: str
    value: str
    is_selected: bool

@dataclass
class Page:
    type: str
    next_id: Optional[str]
    has_previous: bool
    has_next: bool
    item_total: int

@dataclass
class B2BAPIResponse:
    filters: List[Filter]
    items: List[Item]
    sort_on: List[SortOn]
    page: Page
