import numpy as np


first_array = np.linspace(1, 50, 25, dtype = int )
re_first_array = first_array.reshape(5,5)

print(f'Первый массив: {first_array}')
print('')
print(f'Максимальный элемент первого массива: {first_array.max()}')
print('')
print(f'Перевод одномерного массива в двумерный: {re_first_array}')
print('')

second_array = np.random.uniform(low = 0,high = 51,size=(5,5))
print(f'Второй массив: {second_array}')
print('')
print(f'Максимальный элемент воторого массива: {second_array.max()}')
print('')
print(f'Максимальное значение в каждом столбце двумерного массива: {second_array.max(axis=0)}')
print('')
print(f'Максимальное значение в каждой строке двумерного массива: {second_array.max(axis=1)}')
print('')


if first_array.max() > second_array.max():
    print(f'Максимальное значение между двух массивов: {first_array.max()}')
else:
    print(f'Максимальное значение между двух массивов: {second_array.max()}')

print('')
#
summ_array = re_first_array + second_array
print(f'Сумма массивов: {summ_array}')
print('')
diff_array = re_first_array - second_array
print(f'разница массивов: {diff_array}')
print('')
mex_array = re_first_array  * second_array
print(f'Произведение двух массивов: {mex_array}')
print('')
