import numpy as np

mystery = np.array(
    [ 12279., -26024., 28745., np.nan, 31244., -2365., -6974., -9212., np.nan, -17722., 16132., 25933.,
      np.nan, -16431., 29810.],
    dtype=np.float32)

# булевый массив nans_index с информацией о np.nan в массиве mystery:
# True - значение пропущено, False - значение не пропущено
nans_index = np.isnan(mystery)

print(nans_index)

# число пропущенных значений
# n_nan = np.count_nonzero(nans_index == False)
# n_nan = np.count_nonzero(nans_index)
n_nan = np.sum(nans_index)
print(n_nan)

# Скопируйте массив mystery в массив mystery_new.
# Заполните пропущенные значения в массиве mystery_new нулями
mystery_new = np.where(np.isnan(mystery), 0, mystery)

print(mystery_new)

# Поменяйте тип данных в массиве mystery на int32 и сохраните в переменную mystery_int
# mystery_int = np.int32(mystery)
mystery_int = np.nan_to_num(mystery).astype(np.int32) # версия без ошибки

print(mystery_int)

# Отсортируйте значения в массиве mystery по возрастанию и сохраните результат в переменную array
array = np.sort(mystery)

print(array)

# Сохраните в массив table двухмерный массив, полученный из массива array.
# В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть по столбцам!
table = array.reshape(5, 3, order='F')

print(table)
