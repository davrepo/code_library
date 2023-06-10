# implementation 1
def lgN(n: int) -> int:
    """
    input: n as integer
    return: largest integer not greater than lg(n)
    """
    lg = 0
    while n > 0:
        n = n // 2
        lg += 1
    return lg - 1

# def lgN(n: int) -> int:
#     """calculate lg of n as integer"""
#     lg = 0
#     temp = 0
#     while temp < n:
#         lg += 1
#         temp = 2**lg
#     return lg - 1