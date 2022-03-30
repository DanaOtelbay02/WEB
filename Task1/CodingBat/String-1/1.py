def combo_string(a, b):
    if (len(a) > len(b)):
        ans = b + a + b
    else:
        ans = a + b + a

    return ans
