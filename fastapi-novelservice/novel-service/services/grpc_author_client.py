"""Grpc Author Client Service"""

import grpc
from ..grpc_author.author_pb2 import GetAuthorRequest
from ..grpc_author.author_pb2_grpc import GrpcAuthorsStub
from ..models.author import AuthorResponse

channel = grpc.insecure_channel('localhost:50051')
client = GrpcAuthorsStub(channel)


def get_author(author_id: int) -> AuthorResponse:
    """Get an author by id."""

    request = GetAuthorRequest(id=author_id)
    response = client.GetAuthor(request)

    return AuthorResponse(
        id=response.id,
        jp_name=response.jp_name,
        romaji_name=response.romaji_name,
        twitter=response.twitter,
    )
