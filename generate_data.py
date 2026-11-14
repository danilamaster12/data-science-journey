import pandas as pd
import random

n_clients = 100

# Создаем список типов машин
car_types = ["sedan", "SUV", "hatchback"]

data = {
    "client_id": range(1, n_clients + 1),
    "car_year": [random.randint(2005, 2023) for _ in range(n_clients)],
    "car_type": [random.choice(car_types) for _ in range(n_clients)], # <-- НОВАЯ КОЛОНКА
    "visits": [random.randint(1, 10) for _ in range(n_clients)],
    "avg_check": [random.randint(3000, 25000) for _ in range(n_clients)],
    "churn": []
}

for i in range(n_clients):
    year = data["car_year"][i]
    visits = data["visits"][i]
    car_type = data["car_type"][i]
    
    # Новая логика: если машина старая, ИЛИ это хэтчбек с малым числом визитов - уходит
    if year < 2012 or (car_type == "hatchback" and visits < 4):
        data["churn"].append(1)
    else:
        data["churn"].append(0)

df = pd.DataFrame(data)
df.to_csv("auto_service_clients.csv", index=False)
print("База данных обновлена: добавлен тип машины!")
