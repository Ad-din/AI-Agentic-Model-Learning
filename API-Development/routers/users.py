from fastapi import  FastAPI, HTTPException, Response, status,Depends,APIRouter
import model,schema,util
from sqlalchemy.orm import Session
from database import get_db


router=APIRouter()


@router.post("/users",status_code=status.HTTP_201_CREATED,response_model=schema.UserOut)
def created_user(user:schema.UserCreate,db:Session=Depends(get_db)):
    
    #hash the passsword - user.password
    user_dict = user.model_dump()
    user_dict["password"] = util.hash(user.password)
    
    new_user = model.User(**user_dict)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user





#next we will update with sql and we will live database changes compared to the api requests. Fetching and uploading with permanent changes.


#SQL Learning complete after 4 days. Next we will implement sql with pydantic for validation and further process.

@router.get("/users/{id}",response_model=schema.UserOut)
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(model.User).filter(model.User.id==id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id:{id} doesn't exist!")
    return user