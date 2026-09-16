from pydantic import BaseModel
from typing import Optional

class Member(BaseModel):
    name:str
    mobile:str
    plan:str
    fees:float


class Plan(BaseModel):
    plan_name : str
    duration_months : int
    price : float
    description : str

class Trainer(BaseModel):
    name: str
    mobile: str
    specialization: str
    experience: int
    salary: float

class Attendence(BaseModel):
    member_id: int
    attendence_date: str
    check_in: str
    check_out: Optional[str] = None

class Payment(BaseModel):
    member_id: int
    amount: float
    payment_date: str
    payment_method: str
    status: str


class User(BaseModel):
    name:str
    email:str
    password:str
    role:str

class Login(BaseModel):
    email:str
    password:str