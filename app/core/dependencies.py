from fastapi import Header, HTTPException
from fastapi import Depends
from app.core.security import verify_access_token
from app.models.user_model import get_user_by_id


def get_token_header(authorization: str = Header(None)):

    print ("autorizacion ",authorization)

    if not authorization:
        raise HTTPException(status_code=401, detail='Authorization header missing')

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="invalid token format")

    token = authorization.split(" ")[1]

    print("token ",token)
    return token

def get_current_user(token: str = Depends(get_token_header)):
    payload = verify_access_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="invalid or expired token")

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=401,detail="invalid token payload")

    user = get_user_by_id(int(user_id))

    if not user:
        raise HTTPException(status_code=401,datail="user not found")
    
    return {
        "id":user[0],
        "email":user[1]
    }



