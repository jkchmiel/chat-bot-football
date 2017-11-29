from answer_generator.GenerateAnswerFunctions import *
from knowledge.DataReader import read_data

GENERATOR_FUNCTION_MAPPING = {
    "find_top_team": find_top_team,
    "find_results": find_results
}


def generate_answer(request_info):
    data = read_data()
    return GENERATOR_FUNCTION_MAPPING[request_info.get("action")](data, request_info)