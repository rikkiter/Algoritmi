def backpack(max_weight=0, stuff=None):
    stuff_list = sorted(stuff.values(), key=lambda x: x["weight"])
    k = 0
    bank = 0
    while True:
        if stuff_list[k]["weight"] < 0:
            max_weight += abs(stuff_list[k]["weight"])
            bank += stuff_list[k]["price"]
            k += 1
        else:
            stuff_list = stuff_list[k:]
            break
    dp = [[0]*max_weight for _ in range(len(stuff_list))]
    for item in range(len(stuff_list)):
        for weight in range(max_weight):
            if stuff_list[item]["weight"] <= weight + 1:
                r = weight + 1 - stuff_list[item]["weight"]
                price = stuff_list[item]["price"] + (dp[item-1][r-1], 0)[r == 0]
                if price > dp[item-1][weight]:
                    dp[item][weight] = price
                else:
                    dp[item][weight] = dp[item - 1][weight]
            else:
                dp[item][weight] = dp[item-1][weight]
    return dp[-1][-1] + bank


test_stuff = {'banana': {"price": 10, "weight": 10}, 'balloons': {"price": 10, "weight": -10},
              'dope': {"price": 5000, "weight": 5}, 'iphone': {"price": 10000, "weight": 100},
              'bmw': {"price": 100000, "weight": 5000}, 'magic_item': {"price": 3999, "weight": -17}}

test_stuff2 = {'gitara': {"price": 1500, "weight": 1}, 'notebook': {"price": 2000, "weight": 3},
               'magnitofon': {"price": 3000, "weight": 4}}

print(backpack(max_weight=70, stuff=test_stuff))
print(backpack(max_weight=4, stuff=test_stuff2))
