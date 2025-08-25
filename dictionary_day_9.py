# scores={
#     "jaweria": [90,93,98,97], # list inside a dictionary
#     "hamna": 89,
#     "farwa": 80
# }
# print(scores["jaweria"])
# print(scores["jaweria"][0])

# nested_list=[1,2,3,4,[5,6,6]]
# print(nested_list[4][1])

scores={
    "jaweria": {
        "physics":89,
        "bio":97
    },
    "hamna": {
        "physics":87,
        "bio":79
    },
    "farwa": 80
}
print(scores["jaweria"]["bio"])

