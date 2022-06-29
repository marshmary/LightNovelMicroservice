from typing import Optional
from .author import AuthorResponse
from .camel_model import CamelModel


class LightNovel(CamelModel):
    id: int = 0
    jp_name: str
    romaji_name: str
    volumes: int
    extras: int
    author_id: int
    author: Optional[AuthorResponse]


class LightNovelRequest(CamelModel):
    jp_name: str
    romaji_name: str
    volumes: int
    extras: int
    author_id: int


class LightNovelResponse(CamelModel):
    """For serializing the response of the API."""

    id: int
    jp_name: str
    romaji_name: str
    volumes: int
    extras: int
    author: Optional[AuthorResponse]
