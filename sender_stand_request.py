# Верголасов АА 12-я когорта - ФИнальный проект. Инженер по тестированию плюс
import configuration
import data
import requests
# Создание заказа
def post_new_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_ODERS_PATCH,
                         json=body)
# Получение номера заказа
def get_order(track):
        get_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track}"
        response = requests.get(get_url)
        return response

# Автотест
def test():
        response = post_new_order(data.order_body)
        track = response.json()["track"]
        print("Заказ создан. Номер трека-заказа:", track)
        # Получение данных заказа по трек-номеру
        order_response = get_order(track)
        assert order_response.status_code == 200, f"Ошибка {order_response.status_code}"
        order_data = order_response.json()
        print("Данные заказа")
        print(order_data)