from fastapi import APIRouter
from typing import List
from ..services import grpc_author_client
from ..models.light_novel import LightNovelResponse, LightNovel, LightNovelRequest

light_novels = [
    {
        "id": 1,
        "jp_name": "終末なにしてますか？忙しいですか？救ってもらっていいですか？",
        "romaji_name": "Shuumatsu Nani Shitemasu ka? Isogashii Desu ka? Sukutte Moratte Ii Desu ka?",
        "volumes": 5,
        "extras": 1,
        "author_id": 1
    },
    {
        "id": 2,
        "jp_name": "魔女の旅々",
        "romaji_name": "Majo no Tabitabi",
        "volumes": 18,
        "extras": 0,
        "author_id": 2
    },
    {
        "id": 3,
        "jp_name": "リリエールと祈りの国",
        "romaji_name": "Riviere to Inori no Kuni",
        "volumes": 1,
        "extras": 0,
        "author_id": 2
    },
    {
        "id": 4,
        "jp_name": "86-エイティシックス-",
        "romaji_name": "86",
        "volumes": 11,
        "extras": 0,
        "author_id": 3
    },
    {
        "id": 5,
        "jp_name": "キノの旅",
        "romaji_name": "Kino no Tabi",
        "volumes": 21,
        "extras": 0,
        "author_id": 4
    }
]

router = APIRouter(
    prefix="/lightnovel",
    tags=["Light Novels"],
)


@router.get("/", response_model=List[LightNovelResponse])
def get_light_novels():

    light_novels_response = [get_author_of_novel(
        LightNovel(**light_novel)) for light_novel in light_novels]

    return light_novels_response


@router.get("/{id}")
def get_light_novel(id: int):

    match = next((ln for ln in light_novels if ln['id'] == id), None)

    if match is None:
        return {"message": "Light Novel not found", "status": 404}

    light_novel = get_author_of_novel(LightNovel(**match))

    return light_novel


@router.post("/")
def create_light_novel(new_light_novel: LightNovelRequest):

    appendable_light_novel = LightNovel(**new_light_novel.dict())
    appendable_light_novel.id = len(light_novels) + 1

    light_novel_with_author = get_author_of_novel(appendable_light_novel)

    if light_novel_with_author.author is None:
        return {"message": "Author not found", "status": 404}

    light_novels.append(appendable_light_novel.dict())

    return appendable_light_novel


@router.delete("/{id}")
def delete_light_novel(id: int):

    match = next((ln for ln in light_novels if ln['id'] == id), None)

    if match is None:
        return {"message": "Light Novel not found", "status": 404}

    light_novels.remove(match)

    return {"message": "Light Novel deleted", "status": 200}


def get_author_of_novel(ln: LightNovel) -> LightNovel:
    """Call the GRPC service to get the author of the novel."""

    try:
        author = grpc_author_client.get_author(ln.author_id)
    except Exception as e:
        author = None

    ln.author = author

    return ln
