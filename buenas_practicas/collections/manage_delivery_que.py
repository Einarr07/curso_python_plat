from collections import deque

def manage_delivery_que() -> deque:

    # Crea una cola para gestionar entregas de productos
    delivery_que = deque(["order_1", "order_2", "order_3"])

    delivery_que.append("order_4")

    delivery_que.appendleft("order_0")

    delivery_que.pop()

    delivery_que.popleft()

    return delivery_que

print(manage_delivery_que())