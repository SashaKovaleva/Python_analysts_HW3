'''
Задача 3: Составьте несколько сводных таблиц

1. Составьте несколько сводных таблиц.
Данные находятся в файле kc_house_data.csv.
2. среднюю стоимость домов в зависимости от количества спален и сохраните в avg.
Отсортируйте от меньшей стоимости к большей.
3. Найдите минимальную min, среднюю mean и максимальную max стоимости домов в зависимости от состояния дома и сохраните в price.
4. Постройте таблицу с подсчетом количества домов в данных в зависимости от вида на набережную waterfront и оценкой вида view и 
сохраните ее в view_waterfront.
5. Каких домов в зависимости от этажности и количества спален больше? Постройте эту таблицу, содержащую в себе информацию о 
спальнях и этажности, и сохраните ее в bedrooms_floors.
6. Постройте таблицу с подсчетом медианной стоимости домов в данных в зависимости от состояния дома и оценки дома и сохраните 
в 'median_price'.
'''

# Введите ваше решение ниже
import pandas as pd
df = pd.read_csv('kc_house_data.csv', sep=',')

# 1. Средняя стоимость домов в зависимости от количества спален (отсортирована от меньшей к большей)
avg = df.groupby('bedrooms').agg({'price':'mean'}).sort_values('price')

# 2. Минимальная, средняя и максимальная стоимости домов в зависимости от состояния дома
price = df.groupby('condition').agg({'price':['min', 'mean', 'max']})

# 3. Таблица с подсчетом количества домов в зависимости от видов на набережную и оценок вида
view_waterfront = df.pivot_table(index='waterfront', columns='view', values='condition', aggfunc='count', fill_value=0)

# 4. Таблица с подсчетом количества домов в зависимости от этажности и количества спален
bedrooms_floors = pd.crosstab(index=df['floors'], columns=df['bedrooms'])

# 5. Таблица с медианной стоимостью домов в зависимости от состояния дома и оценки дома
median_price = df.pivot_table(index='condition', columns='grade', values='price', aggfunc='median', fill_value=0)

'''
Идеальное решение совпадает
'''