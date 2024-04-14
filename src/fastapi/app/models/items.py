from pydantic import BaseModel


class Items(BaseModel):
    rfc: str
    nombre_razon_social: str
    codigo_postal_domicilio_fiscal: int
    uso_fiscal_factura: str
    regimen_fiscal: str
    correo_electronico: str
