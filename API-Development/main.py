
from random import randrange
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

my_post=[{"id":1,"title":"title of post1",
          "content":"content of post 1"
          },{"title":"favourits food","content":"I love burger","id":2}]
my_post2=[{"id":1,"title":"title of post1",
          "content":"content of post 1"
          },{"title":"favourits food","content":"I love burger","id":2}]



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts")
def get_post():
    return {"data":my_post2}

#retriving posts from the platform
@app.get("/posts/{id}")
def get_posts(id):
    print(id)
    return{
        "post_details":f"Here is a post id:{id}"
    }



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/createpost")
def createPost(post:Post):
    print(post.published,post.rating)
    convertedToDict=post.model_dump()
    print(convertedToDict)
    return{ "data":convertedToDict}

@app.post("/posts")
def create_posts(post:Post):
    post_dict=post.model_dump()
    post_dict['id']=randrange(0,1000000)
    my_post2.append(post_dict)
    return {'data':post_dict} 

@app.get("/posts/latest")
def get_latest():
    print()