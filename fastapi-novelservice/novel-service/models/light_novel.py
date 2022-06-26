from typing import Optional
from pydantic import BaseModel
from .author import AuthorResponse


class LightNovel(BaseModel):
    id: int = 0
    jp_name: str
    romaji_name: str
    volumes: int
    extras: int
    author_id: int
    author: Optional[AuthorResponse]


class LightNovelRequest(BaseModel):
    jp_name: str
    romaji_name: str
    volumes: int
    extras: int
    author_id: int


class LightNovelResponse(BaseModel):
    """For serializing the response of the API."""

    id: int
    jp_name: str
    romaji_name: str
    volumes: int
    extras: int
    author: Optional[AuthorResponse]
