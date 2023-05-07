def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length == None:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    answer = []
    for nums in range(len(series)):
        new_value = series[slice(nums, nums + length)]
        if len(new_value) == length:
            answer.append(new_value)
        
    return answer