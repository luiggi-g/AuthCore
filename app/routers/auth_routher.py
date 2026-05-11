from fastapi import APIRouter
from fastapi import Depends
from app.schemas.user_schema import UserCreate, UserLoggin
from app.services.user_service import register_user, login_user
from app.core.dependencies import get_current_user
from app.schemas.user_schema import RefreshTokenRequest
from app.services.user_service import refresh_access_token

router = APIRouter(
    prefix= "/auth",
    tags=["Auth"]
    )

@router.post("/register")
def register(user: UserCreate):
    return register_user(user.email,user.password)
    return {"mesaje":"prueba"}

@router.post("/login")
def login(data: UserLoggin):
    user = login_user(data.email,data.password)

    if not user:
        raise HTTPException(status_code=401,detail="invalidid credentials")
    
    return user

@router.get("/profile")
def profile(current_user: dict = Depends(get_current_user)):
    return current_user

@router.post("/refresh")
def refresh_token(data: RefreshTokenRequest):

    new_token = refresh_access_token(data.refresh_token)

    if not new_token:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    return new_token