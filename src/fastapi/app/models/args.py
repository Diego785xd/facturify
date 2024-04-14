from pydantic import BaseModel


class Args(BaseModel):
    url: str
    rfc: str
    email: str
    operation: str
    amount: str
    seat: str
    razon_social: str
    regimen: str
    uso: str
    cp: str
    payment: str
