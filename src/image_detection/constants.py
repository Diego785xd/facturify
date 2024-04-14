PROMPT = """
Provide a JSON formatted output containing the detailed information extracted from the following receipt details: 
    (1) merchant_name 
    (2) operation_number 
    (3) list_of_items_or_services_purchased (with quantity and price)
    (4) subtotal
    (5) taxes
    (6) total cost
    (7) seat
Only sent the JSON, nothing more
"""