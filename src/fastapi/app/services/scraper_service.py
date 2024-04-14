import sys
import logging

sys.path.append("..")

from facturify.scraper import web_scraper
from app.models.args import Args


# args = Args(
#     url="https://venta.etn.com.mx/FacturacionElectronica/IndexFacturaElec.html",
#     rfc="XXX001213NT5",
#     email="xxx@hotmail.com",
#     operation="191101714",
#     amount="1593",
#     seat="16",
#     razon_social="ACME",
#     regimen="Actividad",
#     uso="Gastos en General",
#     cp="00000",
#     payment="Tarjeta de Crédito",
# )


def scrap(args: Args):
    logging.info(args)
    logging.info("method...")
    if web_scraper(args) == "success":
        return {"message": "success"}
