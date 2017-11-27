from DialogFlowResponse import DialogFlowResponse
from datetime import datetime


def prepare_response(req):
    resolved_query = req["result"]["resolvedQuery"]
    text = "{} | Test webhook response: {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), resolved_query)
    return DialogFlowResponse().set_text(text).to_json()


if __name__ == "__main__":
    # test response function with example request
    import json
    example_req = json.loads(open("../examples/request.json").read())

    print(prepare_response(example_req))
