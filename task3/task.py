import numpy as np

def get_chess(l:int) -> np.ndarray:
    chess = np.indices((l, l)).sum(axis=0) % 2
    return chess
# print(get_chess(6))

def get_loto(num:int = 3) -> np.ndarray:
    return np.random.randint(1, 101, size=(num, 5, 5))
# print(get_loto())

def get_unique_loto(num:int = 3) -> np.ndarray:
    return np.array(([
        np.random.choice(np.arange(1, 101), size=(5, 5), replace=False)
        for _ in range(num)
    ]))
# print(get_unique_loto())

# def get_chess(l:int) -> np.ndarray:
#     chess = np.ones(l * l)
#     chess[::2] = 0
#     chess = chess.reshape((l, l))
#     if l%2 == 0:
#         chess[1::2] = 1
#         chess[1::2, 1::2] = 0
#     return chess
#
# def get_loto(num:int = 3) -> np.ndarray:
#     loto = np.array((
#         [np.random.randint(1, 101, size=(num, 5, 5))],
#         [np.random.randint(1, 101, size=(num, 5, 5))],
#         [np.random.randint(1, 101, size=(num, 5, 5))]))
#     return loto.reshape(num, 5, 5)
#
# def get_unique_loto(num:int = 3) -> np.ndarray:
#     loto = np.array((
#         [np.random.choice(np.arange(1, 101), size=(5, 5), replace=False)],
#         [np.random.choice(np.arange(1, 101), size=(5, 5), replace=False)],
#         [np.random.choice(np.arange(1, 101), size=(5, 5), replace=False)]
#     ))
#     return loto.reshape(num, 5, 5)
#
# print(get_unique_loto())