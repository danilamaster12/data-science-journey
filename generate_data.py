import pandas as pd
import random

# Генерация данных
n_clients = 100
data = {
    "client_id": range(1, n_clients + 1),
    "car_year": [random.randint(2005, 2023) for _ in range(n_clients)],
    "visits": [random.randint(1, 10) for _ in range(n_clients)],
    "avg_check": [random.randint(3000, 25000) for _ in range(n_clients)],
    "churn": []
}

for i in range(n_clients):
    year = data["car_year"][i]
    visits = data["visits"][i]
    if year < 2012 and visits < 3:
        data["churn"].append(1)
    else:
        data["churn"].append(0)

df = pd.DataFrame(data)
df.to_csv("auto_service_clients.csv", index=False)
print("База данных создана: auto_service_clients.csv")