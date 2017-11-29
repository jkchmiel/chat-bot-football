from response.DialogFlowResponse import DialogFlowResponse
from answer_generator import GenerateAnswer


def read_request_info(req):
    request_info = dict()
    request_info["action"] = req.get("result").get("action")
    request_info["team"] = req.get("result").get("parameters").get("team", '')
    request_info["division"] = req.get("result").get("parameters").get("division", '')
    request_info["match_place"] = req.get("result").get("parameters").get("match_place", '')
    request_info["result"] = req.get("result").get("parameters").get("result", '')
    return request_info


def prepare_response(req):
    request_info = read_request_info(req)
    text = GenerateAnswer.generate_answer(request_info)
    return DialogFlowResponse().set_text(text).to_json()


if __name__ == "__main__":
    # test response function with example request
    import json
    example_req = json.loads(open("../examples/request.json").read())

    print(prepare_response(example_req))