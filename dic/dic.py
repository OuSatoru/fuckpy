dic = {"AAA": 111, "BBB": 222}


def do_with(dic: dict):
    if "AAA" in dic:
        dic["AAA"] = 333

print(dic)
do_with(dic)
print(dic)
