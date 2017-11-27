import json


class DialogFlowResponse(object):
    def __init__(self):
        self.displayText = str()
        self.speech = str()
        self.contextOut = None
        self.data = None
        self.source = "webhook"

    def set_text(self, text=str()):
        self.displayText = text
        self.speech = text
        return self

    def set_context(self, context):
        self.contextOut = context

    def to_dict(self):
        output_dict = dict()
        for k, v in self.__dict__.items():
            if v is not None:
                output_dict[k] = v
        return output_dict

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
