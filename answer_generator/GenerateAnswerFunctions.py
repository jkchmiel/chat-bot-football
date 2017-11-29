ANSWER_TEMPLATES_MAPPING = {
    "find_top_team": "The top {match_place} team in {country} is {team}",
    "find_results": "{team} has {value} {match_place} {result}"
}

MAP_RESULT_TO_COLUMN = {
    "overall": {
        "wins": "W",
        "draws": "D",
        "loses": "L"
    },
    "home": {
        "wins": "HW",
        "draws": "HD",
        "loses": "HL"
    },
    "away": {
        "wins": "AW",
        "draws": "AD",
        "loses": "AL"
    }
}


def find_top_team(data, request_info):
    print request_info
    filtered_data = data[data["Div"] == request_info.get("division")]

    if request_info.get("match_place") == "home":
        final_dict = filtered_data.loc[filtered_data['home_points'].idxmax()].to_dict()
    elif request_info.get("match_place") == "away":
        final_dict = filtered_data.loc[filtered_data['away_points'].idxmax()].to_dict()
    else:
        final_dict = filtered_data.loc[filtered_data['points'].idxmax()].to_dict()
    request_info.update(final_dict)
    return ANSWER_TEMPLATES_MAPPING[request_info.get("action")].format(**request_info)


def find_results(data, request_info):
    index_value = data[data["team"] == request_info.get("team")].index.tolist()[0]
    final_dict = data.loc[index_value].to_dict()
    if request_info.get("match_place"):
        final_dict["value"] = final_dict.get(MAP_RESULT_TO_COLUMN[request_info.get("match_place")][request_info.get("result")])
        request_info.update(final_dict)
    else:
        final_dict["value"] = final_dict.get(MAP_RESULT_TO_COLUMN["overall"][request_info.get("result")])
        request_info.update(final_dict)
    return ANSWER_TEMPLATES_MAPPING[request_info.get("action")].format(**request_info)
