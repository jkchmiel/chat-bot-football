ANSWER_TEMPLATES_MAPPING = {
    "find_top_team": "The top team in {country} is {team}",
    "find_results": "{team} has {value} {result}"
}

MAP_RESULT_TO_COLUMN = {
    "wins": "W",
    "draws": "D",
    "loses": "L"
}


def find_top_team(data, request_info):
    filtered_data = data[data["Div"] == request_info.get("division")]
    final_dict = dict()
    if request_info.get("match_place"):
        pass
    else:
        final_dict = filtered_data.loc[filtered_data['points'].idxmax()].to_dict()

    return ANSWER_TEMPLATES_MAPPING[request_info.get("action")].format(**final_dict)


def find_results(data, request_info):
    index_value = data[data["team"] == request_info.get("team")].index.tolist()[0]
    final_dict = data.loc[index_value].to_dict()
    final_dict["value"] = final_dict.get(MAP_RESULT_TO_COLUMN[request_info.get("result")])
    request_info.update(final_dict)
    return ANSWER_TEMPLATES_MAPPING[request_info.get("action")].format(**request_info)
