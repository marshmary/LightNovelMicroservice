from .camel_model import CamelModel


class AuthorResponse(CamelModel):
    """For serializing the response of the API."""

    id: int
    jp_name: str
    romaji_name: str
    twitter: str
