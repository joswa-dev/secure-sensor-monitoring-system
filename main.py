from fastapi import WebSocket
import asyncio
from fastapi import FastAPI, HTTPException, Depends
from database import engine, Base, SessionLocal
from sensor_simulator import generate_sensor_data
from models import SensorData, User, UserCreate, UserLogin
from auth import (
    hash_password,
    verify_password,
    create_access_token
)

# ADD THESE HERE 👇
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from auth import SECRET_KEY, ALGORITHM
from pydantic import BaseModel
import threading

app = FastAPI()

Base.metadata.create_all(bind=engine)

security = HTTPBearer

def verify_token(Credentials:
HTTPAuthorizationCredentials =
Depends(security)):
    token = Credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        
        return username
    
    except JWTError:
        raise HTTPException(
        status_code=401,
        detail='Invalid token'
        )
    
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Sensor Monitoring System Running"}


@app.get("/sensors")
def get_sensor_data():

    db = SessionLocal()

    data = db.query(SensorData).order_by(
        SensorData.timestamp.desc()
    ).limit(20).all()

    db.close()

    return data

app = FastAPI()

Base.metadata.create_all(bind=engine)

# PASTE HERE 👇
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")
        return username

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
def verify_admin(username: str = Depends(verify_token)):
    db = SessionLocal()

    user = db.query(User).filter(
        User.username == username
    ).first()

    db.close()

    if user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access only"
        )

    return username

@app.websocket("/ws/sensors")
async def websocket_sensor(websocket: WebSocket):

    await websocket.accept()

    while True:
        db = SessionLocal()

        data = db.query(SensorData).order_by(
            SensorData.timestamp.desc()
        ).limit(10).all()

        sensor_list = []

        for sensor in data:
            sensor_list.append({
                "sensor_name": sensor.sensor_name,
                "sensor_value": sensor.sensor_value,
                "timestamp": str(sensor.timestamp)
            })

        await websocket.send_json(sensor_list)

        db.close()

        await asyncio.sleep(2)

# THEN YOUR ROUTE 👇
@app.get("/protected-sensors")
def protected_sensors(username: str = Depends(verify_admin)):
    db = SessionLocal()

    data = db.query(SensorData).order_by(
        SensorData.timestamp.desc()
    ).limit(20).all()

    db.close()

    return {
        "logged_in_user": username,
        "sensor_data": data
    }

@app.get("/protected-sensors")
def protected_sensors(username: str = Depends(verify_token)):

    db = SessionLocal()

    data = db.query(SensorData).order_by(
        SensorData.timestamp.desc()
    ).limit(20).all()

    db.close()

    return {
        "logged_in_user": username,
        "sensor_data": data
    }


@app.on_event("startup")
def start_sensor():

    thread = threading.Thread(target=generate_sensor_data)

    thread.daemon = True

    thread.start()

@app.post("/register")
def register(user: UserCreate):
    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = User(
        username=user.username,
        password=hash_password(user.password), role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: UserLogin):

    db = SessionLocal()

    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }