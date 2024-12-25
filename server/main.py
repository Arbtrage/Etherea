from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

DYNAMODB_TABLE_NAME = "YourTableName"

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

dynamodb = boto3.resource(
    "dynamodb",
    region_name=AWS_DEFAULT_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

class User(BaseModel):
    user_name: str
    user_email: str
    preferences: dict

@app.post("/add-user")
async def add_user(user: User):
    try:
        table.put_item(
            Item={
                "user_name": user.user_name,
                "user_email": user.user_email,
                "preferences": user.preferences,
            }
        )
        return {"message": "User added successfully"}
    except (BotoCoreError, ClientError) as e:
        raise HTTPException(status_code=500, detail=str(e))
