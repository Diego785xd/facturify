"""
This is a scraper file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         facturify = facturify.scraper:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``facturify`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from facturify import __version__
from facturify.utils.strings import contains_normalized

__author__ = "Oscar Santos"
__copyright__ = "Oscar Santos"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from facturify.scraper import web_scraper`,
# when using this Python module as a library.


def get_driver():
    """Returns a selenium driver"""
    _logger.info("Getting driver")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options, service=service)
    return driver


def _continue(driver):
    """Find and click the submit button"""
    submit_button = driver.find_element(By.ID, "continuar")
    submit_button.click()
    # Optionally, you can wait for some time to see the result before closing the browser
    # For example, wait for 3 seconds
    driver.implicitly_wait(3)


def form1(driver, args):
    # Wait for the page to load
    time.sleep(2)  # Adjust as needed

    # Find the RFC input field and fill it with your RFC
    rfc_input = driver.find_element("name", "RS_RFC")
    rfc_input.clear()  # Clear any existing text
    rfc_input.send_keys(args.rfc)

    time.sleep(1)  # Adjust as needed

    # Find the EMAIL input field and fill it with your email address
    email_input = driver.find_element("name", "RS_Correo")
    email_input.clear()  # Clear any existing text
    email_input.send_keys(args.email)

    time.sleep(1)  # Adjust as needed

    _continue(driver)


def form2(driver, args):
    # Wait for the page to load
    time.sleep(2)  # Adjust as needed

    operacion_input = driver.find_element("name", "RS_Operacion")
    operacion_input.clear()
    operacion_input.send_keys(args.operation)

    time.sleep(1)  # Adjust as needed

    importe_input = driver.find_element("name", "RS_Importe")
    importe_input.clear()
    importe_input.send_keys(args.amount)

    time.sleep(1)  # Adjust as needed

    asiento_input = driver.find_element("name", "RS_Asiento")
    asiento_input.clear()
    asiento_input.send_keys(args.seat)

    time.sleep(1)  # Adjust as needed

    _continue(driver)


def form3(driver, args):
    # Wait for the page to load
    time.sleep(2)  # Adjust as needed

    razon_social_input = driver.find_element("name", "RS_Social")
    razon_social_input.clear()
    razon_social_input.send_keys(args.razon_social)

    time.sleep(1)  # Adjust as needed

    regimen_dropdown = driver.find_element(By.XPATH, value='//*[@id="RegimenFiscal"]')
    for option in regimen_dropdown.find_elements(By.TAG_NAME, "option"):
        _logger.debug(option.text)
        if contains_normalized(args.regimen, option.text):
            option.click()
            break

    time.sleep(1)

    uso_dropdown = driver.find_element(By.XPATH, value='//*[@id="RS_CFDI"]')
    for option in uso_dropdown.find_elements(By.TAG_NAME, "option"):
        _logger.debug(option.text)
        if contains_normalized(args.uso, option.text):
            option.click()
            break

    time.sleep(1)

    cp_input = driver.find_element("name", "RS_CP")
    cp_input.clear()
    cp_input.send_keys(args.cp)

    time.sleep(1)  # Adjust as needed

    email2_input = driver.find_element("name", "RS_Correo-2")
    email2_input.clear()
    email2_input.send_keys(args.email)

    time.sleep(1)  # Adjust as needed

    payment_input = driver.find_element(By.XPATH, value='//*[@id="FormaPago"]')
    for option in payment_input.find_elements(By.TAG_NAME, "option"):
        _logger.debug(option.text)
        if contains_normalized(args.payment, option.text):
            option.click()
            break
    # payment_input = driver.find_element(
    #     By.XPATH, value='//*[@id="FormaPago"]/option[3]'
    # )
    # payment_input.click()

    time.sleep(1)  # Adjust as needed

    _continue(driver)


def web_scraper(args):
    """Scrapes an url and returns the data"""
    _logger.info(f"Scraping URL: {args.url}")
    driver = get_driver()
    driver.get(args.url)
    # do stuff
    _logger.info(f"First form: {args.rfc} {args.email}")
    form1(driver, args)
    _logger.info(f"Second form")
    form2(driver, args)
    _logger.info(f"Third form")
    form3(driver, args)
    # simulate ops with time
    time.sleep(5)
    driver.quit()


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Web scraping for billing information."
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"facturify {__version__}",
    )
    parser.add_argument(
        dest="url", help="URL from billing web page", type=str, metavar="URL"
    )
    parser.add_argument(dest="rfc", help="RFC from customer", type=str, metavar="RFC")
    parser.add_argument(
        dest="email", help="email from customer", type=str, metavar="EMAIL"
    )
    parser.add_argument(
        dest="operation",
        help="Operation number from ticket",
        type=str,
        metavar="OPERATION",
    )
    parser.add_argument(
        dest="amount",
        help="Amount from ticket",
        type=str,
        metavar="AMOUNT",
    )
    parser.add_argument(
        dest="seat",
        help="Seat from ticket",
        type=str,
        metavar="SEAT",
    )
    parser.add_argument(
        dest="razon_social",
        help="Razon social from customer",
        type=str,
        metavar="RAZON SOCIAL",
    )
    parser.add_argument(
        dest="regimen",
        help="Regimen fiscal from customer",
        type=str,
        metavar="REGIMEN FISCAL",
    )
    parser.add_argument(
        dest="uso",
        help="Uso de CFDI from customer",
        type=str,
        metavar="USO CFDI",
    )
    parser.add_argument(
        dest="cp",
        help="CP from customer",
        type=str,
        metavar="C.P.",
    )
    parser.add_argument(
        dest="payment",
        help="Payment method from ticket",
        type=str,
        metavar="PAYMENT METHOD",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """Wrapper allowing :func:`scraper` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`scraper`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "https://venta.etn.com.mx/FacturacionElectronica/IndexFacturaElec.html", "XXX001213NT5", "xxx@hotmail.com", "191101714", "1593", "16", "Razon Social", "Actividad", "Gastos en General", 00000, "Tarjeta de crédito"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.info("Starting scraping...")
    print(f"URL: {args.url}")
    web_scraper(args)
    _logger.info("Script ends here")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m facturify.scraper -v https://venta.etn.com.mx/FacturacionElectronica/IndexFacturaElec.html XXX001213NT5 xxx@hotmail.com 191101714 1593 16 "Razon Social" "Actividad" "Gastos en General" 00000 "Tarjeta de crédito"
    #
    run()
