class DectectionBuilder:

    def __init__(
            self,
            detection,
            response_component
    ):
        self.detection = detection
        self.response_component = response_component
    
    def process_receipt(
            self
    ):
        self.raw_response = self.detection.receipt_scan()

    def get_response(
            self
    ):
        return self.response_component.process_response(self.raw_response)