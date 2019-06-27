import requests


API_KEY = "a1998134c52e7e1e04e4dc8a5c0f46cfdf8a5b747357ad3c48ae2903940038d5"
url = "https://api-tokyochallenge.odpt.org/api/v4/odpt:Bus?" \
      "odpt:operator=odpt.Operator:SeibuBus&acl:consumerKey={}".format(API_KEY)


def res_resize(data):
    route = data["owl:sameAs"]
    note = data["odpt:note"]
    try:
        from_time = data["odpt:fromBusstopPoleTime"].replace("T", " ")[:-6]
    except AttributeError:
        from_time = str(data["dc:date"].replace("T", " ")[:-11]) + "00:00"
    from_stop = data["odpt:fromBusstopPole"]
    to_stop = data["odpt:toBusstopPole"]
    # id = str(route) + "/" + str(from_stop) + "/" + str(from_time)

    return {"route": route, "note": note, "from_time": from_time, "from_stop": from_stop, "to_stop": to_stop}


def call_api():
    res = requests.get(url).json()
    res_list = []
    for data in res:
        res_dic = res_resize(data)
        res_list.append(res_dic)
    return res_list


if __name__ == "__main__":
    res = requests.get(url).json()
    # print(res_resize(res[0]))
    res_list = []
    for data in res:
        res_dic = res_resize(data)
        print(res_dic)
        res_list.append(res_dic)
    print(res_list)
