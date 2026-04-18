import numpy as np

# np.random.seed(2030)
# simple = np.random.randint(0, 2)
# randoms = np.random.randint(-150, 2022, 120)
# table = np.random.choice(np.arange(1, 101), size=(3, 2))
# even = np.arange(2, 17, 2)
# mix = even.copy()
# np.random.shuffle(mix)
# select = np.random.choice(even, 3,  replace=False)
# triplet = select.copy()
# np.random.shuffle(triplet)

# print(randoms)

rng = np.random.default_rng(2023)
simple = rng.integers(0, 2)
randoms = rng.integers(-150, 2022, 120)
# table = rng.choice(np.arange(0, 101), (3, 2), )
table = rng.integers(1, 101, (3, 2))
even = np.arange(2, 17, 2)
mix = even.copy()
rng.shuffle(mix)
select = rng.choice(even, 3, replace=False)
triplet = select.copy()
rng.shuffle(triplet)

print(table)
