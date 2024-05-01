import numpy as np
import pandas as pd

from sklearn.datasets import fetch_california_housing
from sqlalchemy import create_engine


# Получим датасет California housing
data = fetch_california_housing()

# Объединим фичи и таргет в один np.array
dataset = np.concatenate([data['data'], data['target'].reshape([data['target'].shape[0],1])],axis=1)

# Преобразуем в dataframe.
dataset = pd.DataFrame(dataset, columns = data['feature_names']+data['target_names'])

# Создадим подключение к базе данных postgres. Поменяйте на свой пароль yourpass
engine = create_engine('postgresql://postgres:yourpass@localhost:5432/postgres')

# Сохраним датасет в базу данных
dataset.to_sql('california_housing', engine)

# Для проверки можно сделать:
print(pd.read_sql_query("SELECT * FROM california_housing", engine))