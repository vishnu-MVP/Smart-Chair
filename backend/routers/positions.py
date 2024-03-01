from typing import List, Optional
from fastapi import APIRouter, Request, Body, status, HTTPException
from datetime import date,datetime
#from models import PostBase, PostDB, PostUpdate ,Comment 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()

