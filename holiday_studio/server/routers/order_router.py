from flask import Blueprint, request
from models import AlchemyEncoder
from models import Order, create_session
import json


router = Blueprint("order_api",
                   __name__,
                   template_folder="/server/templates",
                   url_prefix="/order")


@router.route("/<int:order_id>", methods=["GET"])
def get_order(order_id):
    session = create_session()
    order = session.query(Order).get(order_id)  # аналогично session.query(Employee).where(Employee.id == employee_id)
    if order:
        result = json.dumps(order, cls=AlchemyEncoder, ensure_ascii=False)
    else:
        result = json.dumps(None)
    session.close()
    return result


@router.route("/", methods=["GET"])
def get_employees():
    session = create_session()
    orders = session.query(Order).all()
    result = json.dumps(orders, cls=AlchemyEncoder, ensure_ascii=False)
    session.close()
    return result


@router.route("/", methods=["POST"])
def create_employee():
    session = create_session()
    json_data = request.json
    new_order = Order(**json_data)
    session.add(new_order)
    session.commit()
    result = json.dumps(new_order, cls=AlchemyEncoder, ensure_ascii=False)
    session.close()
    return result


@router.route("/<int:order_id>", methods=["PUT"])
def put_employee(order_id):
    session = create_session()
    order = session.query(Order).get(order_id)  # аналогично session.query(Employee).where(Employee.id == employee_id)
    if order:
        json_data = request.json  # пример: {"fullname": "Роман", login: "grm"} - означает, что нужно изменить только 2 поля. Как распарсить?

        # лучше:
        for key, value in json_data.items():
            setattr(order, key, value)  # задаем в order полю key значение value
        session.commit()
        result = json.dumps(order, cls=AlchemyEncoder, ensure_ascii=False)
    else:
        result = json.dumps({})
    session.close()
    return result


@router.delete("/<int:order_id>")
def delete_employee(order_id):
    session = create_session()
    order = session.query(Order).get(order_id)
    if order:
        session.delete(order)
        session.commit()
        result = json.dumps(True)
    else:
        result = json.dumps(False)
    session.close()
    return result