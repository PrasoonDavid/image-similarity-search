from pydantic import BaseModel
from typing import List, Optional


class ActionPage(BaseModel):
    type: str
    query: dict


class Action(BaseModel):
    type: str
    page: ActionPage


class Category(BaseModel):
    uid: int
    name: str
    action: Action


class CategoryMap(BaseModel):
    l1: Optional[Category]
    l2: Optional[Category]
    l3: Optional[Category]


class Media(BaseModel):
    url: str
    type: str


class BrandLogo(BaseModel):
    url: str


class Brand(BaseModel):
    uid: int
    logo: Optional[BrandLogo]
    name: str


class Product(BaseModel):
    rating_bucket: Optional[int]
    objectID: str
    # uid: int
    # custom_order: dict
    # sizes: List[str]
    # category_map: CategoryMap
    # tags: List[str]
    # item_type: str
    # description: str
    medias: List[Media]
    item_code: str
    name: str
    # short_description: str
    # attributes: dict
    # variants: List[str]
    slug: str
    # is_dependent: bool
    # brand: Optional[Brand]
    # wl_channels: List[str]
    # rank: int
    # out_of_stock: bool


class FilterValue(BaseModel):
    value: str
    is_selected: bool
    display: str
    count: int


class FilterKey(BaseModel):
    logo: Optional[str]
    name: str
    kind: str
    display: str


class Filter(BaseModel):
    values: List[FilterValue]
    key: FilterKey


class SortOption(BaseModel):
    logo: Optional[str]
    is_selected: bool
    name: str
    value: str
    display: str


class Page(BaseModel):
    item_total: int
    has_previous: bool
    has_next: bool
    current: int
    type: str


class APIResponse(BaseModel):
    items: List[Product]
    # filters: List[Filter]
    # sort_on: List[SortOption]
    page: Page
