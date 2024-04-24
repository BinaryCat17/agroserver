from pydantic import BaseModel
from uuid import UUID

class Entity(BaseModel):
    id: UUID
    name: str
    type: str

class Organization(BaseModel):
    id: UUID
    name: str
    parent: UUID

class User(BaseModel):
    id: UUID
    