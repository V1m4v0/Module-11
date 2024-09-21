import pandas as pd

# Считывание данных из файла
data = pd.read_csv('data.csv')

# Простой анализ: средний возраст и средняя зарплата
average_age = data['Age'].mean()
average_salary = data['Salary'].mean()

# Вывод результатов в консоль
print(f'Средний возраст: {average_age}')
print(f'Средняя зарплата: {average_salary}')