
from random import randrange
from typing import Optional

from fastapi import  FastAPI, HTTPException, Response, status
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

def find_post(id):
    for p in my_post:
        if p['id']== id:
            return p

def find_indexed_post(id):
    for i, p in enumerate(my_post):
        if p.get('id')==id:
            return i

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    post_dict=post.model_dump()
    post_dict['id']=randrange(0,1000000)
    my_post.append(post_dict)
    return {'data':post_dict} 


@app.get("/posts")
def get_post():
    return {"data":my_post}


@app.get("/posts/latest")
def get_latest():
    post=my_post[len(my_post)-1]
    return{"detail":post}


#retriving posts from the platform
@app.get("/posts/{id}")
def get_posts(id:int,response: Response):  #id:int. this automatically converts id to an integer.
    post=find_post(id)
    if not post:
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found!")
        # or we can write it like this: (first one is better.)
        response.status_code=status.HTTP_404_NOT_FOUND
        return{"message":f"Post with {id} was not found!"}
    return{
        "post_details":post
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



#Delete a post:

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index=find_indexed_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    my_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#update information --put operation

@app.put("/posts/{id}")
def update_info(id:int,post:Post):
    index=find_indexed_post(id)

    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id } not found!")

    post_dict=post.model_dump()
    post_dict['id']=id
    my_post[index]=post_dict
    return{'Data':post_dict}

