
from random import randrange
from typing import Optional

from fastapi import  FastAPI, HTTPException, Response, status,Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import model
from database import engine,get_db
from sqlalchemy.orm import Session


model.Base.metadata.create_all(bind=engine)



while True:
    try:
        conn=psycopg2.connect(
        host='localhost',
        database='fastapi',
        user='postgres',
        password='admin',
        cursor_factory=RealDictCursor)
        cursor =conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Connection to database failed!")
        print("Error:",error)
        time.sleep(2)


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published:bool = True
    


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

@app.get("/sqlalchemy")
def test_db(db: Session = Depends(get_db)):
   posts=db.query(model.Products).all()
   return {"data :":posts}



@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post, db:Session=Depends(get_db)):
    # print(**post.model_dump()) #** means it will automatically transfer the fields to their fields.

    # new_post= model.Post(title=post.title,content=post.content,published=post.published) # so instead of writing this like this we will use **.
    new_post=model.Post(**post.model_dump()) # this way we don't have write every field manually.
    db.add(new_post)
    db.commit()
    db.refresh(new_post) #this is used to get the post data we have sent.
    return {"data":new_post}

@app.get("/posts")
def get_post():
    cursor.execute("SELECT * FROM posts")
    posts=cursor.fetchall()
    return {"data":posts}


@app.get("/posts/latest")
def get_latest():
    post=my_post[len(my_post)-1]
    return{"detail":post}

@app.get("/products")
def get_products():
    cursor.execute("SELECT name, price FROM products")
    products = cursor.fetchall()

    result = []
    for product in products:
        result.append({
            "name": product["name"],
            "price": product["price"]
        })

    return result





#retriving posts from the platform

@app.get("/posts/{id}")
def get_posts(id:int,db:Session=Depends(get_db)):  #id:int. this automatically converts id to an integer.
    post=db.query(model.Post).filter(model.Post.id==id).first()
    # print(post) this print shows us what is query that is generated automatically.
    # cursor.execute("SELECT title FROM posts WHERE id = %s", (str(id),))
    # post=cursor.fetchone()

    if not post:
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found!")
        # or we can write it like this: (first one is better.)
        #response.status_code=status.HTTP_404_NOT_FOUND
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
def delete_post(id:int,db:Session=Depends(get_db)):
    #Old way:

    # index=find_indexed_post(id)
    # if index==None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    # my_post.pop(index)
    # return Response(status_code=status.HTTP_204_NO_CONTENT)

    #ORM way:
    post=db.query(model.Post).filter(model.Post.id==id)
    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not exists!")
    post.delete(synchronize_session=False)   
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)





#update information --put operation

@app.put("/posts/{id}")
def update_info(id:int,post:Post,db:Session=Depends(get_db)):

    #Old way:

    # index=find_indexed_post(id)
    # if index==None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"post with id: {id } not found!")
    # post_dict=post.model_dump()
    # post_dict['id']=id
    # my_post[index]=post_dict
    # return{'Data':post_dict}

    #ORM way:
    updated_posts=db.query(model.Post).filter(model.Post.id==id).update(post.model_dump(exclude_unset=True),synchronize_session=False)
    
    if updated_posts == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail=f"post with id: {id } not found!")
    
    db.commit()
    return {"message":"Updated successfully!"}




#next we will update with sql and we will live database changes compared to the api requests. Fetching and uploading with permanent changes.


#SQL Learning complete after 4 days. Next we will implement sql with pydantic for validation and further process.

