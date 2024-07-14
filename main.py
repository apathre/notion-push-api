from fastapi import FastAPI, HTTPException, Depends
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowAuthorizationCode as OAuthFlowAuthorizationCodeModel
from fastapi.openapi.models import OAuthFlowImplicit as OAuthFlowImplicitModel
from fastapi.openapi.models import OAuthFlowPassword as OAuthFlowPasswordModel
from fastapi.openapi.models import OAuthFlowClientCredentials as OAuthFlowClientCredentialsModel
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowAuthorizationCode as OAuthFlowAuthorizationCodeModel


from pydantic import BaseModel, Field
from typing import List, Dict, Any
from notion_client import fetch_from_notion, post_to_notion, patch_to_notion, put_to_notion

app = FastAPI()



@app.get("/")
def read_root():
    return {"message": "Welcome to the Notion API FastAPI app"}

@app.get("/databases")
def get_databases():
    try:
        return fetch_from_notion("databases")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/databases/{database_id}/pages")
def get_database_pages(database_id: str):
    payload = {"page_size":100} 
    try:
        return post_to_notion(f"databases/{database_id}/query", payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class PageData(BaseModel):
    parent: dict
    properties: dict

@app.post("/pages")
def create_page(page_data: PageData):
    try:
        return post_to_notion("pages", page_data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class UpdatePageData(BaseModel):
    properties: dict

@app.patch("/pages/{page_id}")
def update_page(page_id: str, page_data: UpdatePageData):
    try:
        return patch_to_notion(f"pages/{page_id}", page_data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class UpdateDatabaseData(BaseModel):
    title: List[Dict[str, Any]]
    properties: Dict[str, Any] = Field(default_factory=dict)

@app.put("/databases/{database_id}")
def update_database(database_id: str, database_data: UpdateDatabaseData):
    try:
        return patch_to_notion(f"databases/{database_id}", database_data.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))