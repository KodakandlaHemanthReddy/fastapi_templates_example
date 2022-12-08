from pydantic import BaseModel


class UserData(BaseModel):
    name: str
    month: str
    day: str
