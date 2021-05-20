# def merge(sea, fresh):
#     result = list.new
#     while not (sea.empty and fresh.empty):
#         if sea.top_item > fresh.top_item:
#             fish = sea.remove_top_item
#         else:
#             fish = fresh.remove_top_item
#         result.append(fish)
        
#     return result

# print(merge(["삼치","메기","상어","붕어","정어리","잉어","피라미"]))

sea = ["삼치","상어","정어리"]
fresh = ["메기","붕어","잉어","피라미"]

result = []
while not (sea.empty and fresh.empty):
    if sea.top_item > fresh.top_item:
        fish = sea.remove_top_item
    else:
        fish = fresh.remove_top_item
    result.append(fish)

print(result)