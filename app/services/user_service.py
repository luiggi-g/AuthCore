from app.models.user_model import get_user_by_email, create_user, user_exists
from app.core.security import hash_password, verify_password
from app.core.security import verify_token, create_access_token
from app.core.security import create_refresh_token, verify_refresh_token
from fastapi import HTTPException

def register_user(email: str, password: str):

    result = user_exists(email)
    
    if result:
        raise HTTPException(status_code=400, detail="cuenta ya creada")

    hashed_password = hash_password(password)
    user = create_user(email, hashed_password)

    return user
    

def login_user(email:str, password:str):
    user = get_user_by_email(email)

    if not user:
        return None
    
    user_id,user_email,hashed_password = user

    if not verify_password(password, hashed_password):
        return None
    
    access_token = create_access_token(
        data={
            "sub": str(user_id),
            "email": user_email
        }
    )

    
    # REFRESH TOKEN
    refresh_token = create_refresh_token(
        data={
            "sub": str(user_id)
        }
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

def refresh_access_token(refresh_token: str):

    payload = verify_refresh_token(refresh_token)

    if not payload:
        return None

    user_id = payload.get("sub")

    new_access_token = create_access_token(
        data={
            "sub": user_id
        }
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }