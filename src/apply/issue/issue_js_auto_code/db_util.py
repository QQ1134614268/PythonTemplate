def res_to_dict(response):
    return [dict(zip(item.keys(), item)) for item in response]
