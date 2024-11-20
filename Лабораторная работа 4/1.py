import json

FILENAME = "input.json"

def task() -> float:
    # Открываем файл и десериализуем содержимое в объект Python
    with open(FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Вычисляем сумму произведений "score" * "weight" для каждого словаря
    total_sum = sum(item["score"] * item["weight"] for item in data)

    # Возвращаем результат, округленный до 3 знаков после запятой
    return round(total_sum, 3)

if __name__ == '__main__':
    print(task())

