def hsv_to_json(c):
    json_arr = [c[0]]
    if c[1] != 1.0 or c[2] != 1.0:
        json_arr.append(c[1])
    if c[2] != 1.0:
        json_arr.append(c[2])
    return json_arr
