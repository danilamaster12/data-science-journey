import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Загрузка данных
df = pd.read_csv("auto_service_clients.csv")

# 2. Статистика оттока
churn_rate = df["churn"].mean() * 100
print(f"Процент ушедших клиентов: {churn_rate:.2f}%")

print("\nСредний чек (0 - остался, 1 - ушел):")
print(df.groupby("churn")["avg_check"].mean())

# 3. Визуализация
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="churn", palette=["green", "red"])
plt.title("Отток клиентов автосервиса")
plt.xlabel("Статус (0 - остался, 1 - ушел)")
plt.ylabel("Количество клиентов")
plt.show()