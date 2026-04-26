from typing import List

from fastapi import  FastAPI, HTTPException, Response, status,Depends,APIRouter
import model,schema,util
from sqlalchemy.orm import Session
from database import get_db
from schema import PostCreate,Post
import oauth2


router=APIRouter(
    prefix="/posts",
    tags=['Posts']
)



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

# @router.get("/")
# def read_root():
#     return {"Hello": "World"}



@router.post("/",status_code=status.HTTP_201_CREATED,response_model=Post)
def create_posts(post:PostCreate, db:Session=Depends(get_db),current_user: int=Depends(oauth2.get_current_user)):
    # print(**post.model_dump()) #** means it will automatically transfer the fields to their fields.

    # new_post= model.Post(title=post.title,content=post.content,published=post.published) # so instead of writing this like this we will use **.
    print(current_user.id)
    new_post=model.Post(user_id=current_user.id,**post.model_dump()) # this way we don't have write every field manually.
    db.add(new_post)
    db.commit()
    db.refresh(new_post) #this is used to get the post data we have sent.
    return new_post

@router.get("/",response_model=List[schema.Post])
def get_post(db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    posts=db.query(model.Post).filter(model.Post.id == current_user.id).all()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"posts from db not found!")
    
    return posts


@router.get("/latest")
def get_latest():
    post=my_post[len(my_post)-1]
    return post

# @router.get("/products")
# def get_products():
#     # # cursor.execute("SELECT name, price FROM products")
#     # # products = cursor.fetchall()

#     # result = []
#     # for product in products:
#     #     result.routerend({
#     #         "name": product["name"],
#     #         "price": product["price"]
#     #     })

#     return result





#retriving posts from the platform

@router.get("/{id}")
def get_posts(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):  #id:int. this automatically converts id to an integer.
    post=db.query(model.Post).filter(model.Post.id==id).first()
    

    if not post:
        return{"message":f"Post with {id} was not found!"}
    return  post
    





@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@router.post("/createpost")
def createPost(post:PostCreate):
    print(post.published,post.rating)
    convertedToDict=post.model_dump()
    print(convertedToDict)
    return convertedToDict



#Delete a post:

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #Old way:

    # index=find_indexed_post(id)
    # if index==None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    # my_post.pop(index)
    # return Response(status_code=status.HTTP_204_NO_CONTENT)

    #ORM way:
    
    post=db.query(model.Post).filter(model.Post.id==id).first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} does not exists!")
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"You don't have permission to delete this post")

    db.delete(post)  
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)





#update information --put operation

@router.put("/{id}")
def update_info(id:int,post:PostCreate,db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):

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
    if post.user_id != oauth2.get_current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"You don't have permission to delete this post")


    updated_posts=db.query(model.Post).filter(model.Post.id==id).update(post.model_dump(exclude_unset=True),synchronize_session=False)
    
    if updated_posts == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail=f"post with id: {id } not found!")
    
    
    db.commit()
    return {"message":"Updated successfully!"}


