import requests


url = "https://api-tokyochallenge.odpt.org/api/v4/odpt:Bus?odpt:operator=odpt.Operator:Toei&" \
      "acl:consumerKey=6a294592f92c6adf7c749f4934ace3a23dceeecef46d82f65f01b9218cdacc26"


def res_resize(data):
    route = data["owl:sameAs"]
    note = data["odpt:note"]
    from_time = data["odpt:fromBusstopPoleTime"].replace("T", " ")[:-6]
    from_stop = data["odpt:fromBusstopPole"]
    to_stop = data["odpt:toBusstopPole"]
    id = route + "/" + from_stop + "/" + from_time

    return {
        "id": id,
        "route": route,
        "note": note,
        "from_time": from_time,
        "from_stop": from_stop,
        "to_stop": to_stop
    }


def call_api():
    res = requests.get(url).json()
    res_list = []
    for data in res:
        res_dic = res_resize(data)
        res_list.append(res_dic)
    return res_list


if __name__ == "__main__":
    print(call_api())
