from json import loads

class ResponseComponent:

    def process_response(self, response):
        content = response.get("choices")[0].get("message").get("content")
        data = content.replace("```","").replace("json","")
        json_data = loads(data)

        return json_data