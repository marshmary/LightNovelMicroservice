from lib2to3.pytree import Base
from pydantic import BaseModel


class AuthorResponse(BaseModel):
    """For serializing the response of the API."""

    id: int
    jp_name: str
    romaji_name: str
    twitter: str
