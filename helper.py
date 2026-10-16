def get_int(msg, fail = "Invalid."):
  try:
    ans = int(input(msg))
  except:
    print(fail)
    return get_int(fail)
  return ans


def get_float(msg, fail = "Invalid."):
  try:
    ans = float(input(msg))
  except:
    print(fail)
    return get_float(fail)
  return ans