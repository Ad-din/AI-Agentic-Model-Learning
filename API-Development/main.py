
from typing import Optional

from fastapi import  FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published:bool = True
    rating: Optional[int]=None


@app.get("/")
def read_root():
    return {"Hello": "World"}




#retriving posts from the platform
@app.get("/posts/{user_id}")
def get_posts(user_id):
    return {"User ID":user_id,
            "Name":"Abdullah",
            "Age":6,
            "expertise":"None",
            "Saved?":"YES"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/createpost")
def createPost(post:Post):
    print(post.published,post.rating)
    convertedToDict=post.model_dump()
    print(convertedToDict)
    return{ "data":convertedToDict}

