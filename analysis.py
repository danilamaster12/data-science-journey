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
sns.countplot(data=df, x="churn", hue="churn", palette=["green", "red"], legend=False)
plt.title("Отток клиентов автосервиса")
plt.xlabel("Статус (0 - остался, 1 - ушел)")
plt.ylabel("Количество клиентов")

# 1. Сколько денег теряет сервис из-за ушедших?
# Берем строки, где churn == 1, суммируем их avg_check
lost_money = df[df["churn"] == 1]["avg_check"].sum()
print(f"Сумма потерянной выручки из-за ушедших клиентов: {lost_money} руб.")

# 2. Кто уходит чаще: владельцы седанов, внедорожников или хэтчбеков?
print("\n--- Отток по типам машин (в %) ---")
# Группируем по типу и считаем среднее значение churn (долю ушедших)
print(df.groupby("car_type")["churn"].mean() * 100)
# 4. График 2 Отток клиентов по типам машин
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="car_type", y="churn", palette="viridis")
plt.title("Доля ушедших клиентов по типу машины")
plt.xlabel("Тип машины")
plt.ylabel("Доля ушедших (1 = 100%)")
plt.show()
