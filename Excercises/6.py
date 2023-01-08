import json


class GSM:
    def __init__(self, available_quantity, unit_price, produce_date, producer, model):
        self.available_quantity = available_quantity
        self.unit_price = unit_price
        self.produce_data = produce_date
        self.producer = producer
        self.model = model

    def __repr__(self):
        return f"{self.available_quantity} {self.unit_price} {self.produce_data} {self.producer} {self.model}"

    def __lt__(self, other):
        return self.available_quantity < other.available_quantity


gsm = [
    GSM(56, 1500, 2021, "Apple Iphone", "13"),
    GSM(32, 2800, 2022, "Apple Iphone", "14 Pro"),
    GSM(75, 1350, 2021, "Samsung", "S22"),
    GSM(43, 2000, 2022, "Apple Iphone", "14"),
    GSM(10, 700, 2020, "Huawei", "P30")
]

dict_models = dict()


def sort():
    print(sorted(gsm, reverse=False))


def save_json(producer):
    with open("phones_by_1producer.json", "w") as j:
        counter = 0
        for model in gsm:
            if model.producer == producer:
                key = counter
                value = str(model)
                dict_models[key] = value
                counter += 1

        js = json.dumps(dict_models)
        j.write(js)


save_json("Apple Iphone")
sort()
