import sqlalchemy
from flask import Blueprint, request, render_template, redirect
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

from forms.create_client import CreateClientForm
from forms.create_order import CreateOrderForm
from forms.login import LoginForm
from models import AlchemyEncoder, Employee, Client, EmployeeOrder, ClientOrder
from models import Order, create_session
import json
# from flask_login import current_user

router = Blueprint("",
                   __name__,
                   template_folder="/server/templates")


@router.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        session = create_session()
        employee = session.query(Employee).\
            filter(Employee.email == login_form.email.data).first()
        if employee and employee.check_password(login_form.password.data):
            login_user(employee)
            session.close()
            return redirect("/")
        else:
            session.close()
            return redirect("/site/login")
    return render_template("login.html", title="Авторизация", form=login_form)


@router.route("/create_client", methods=["GET", "POST"])
@login_required
def create_client():
    create_client_form = CreateClientForm()
    if create_client_form.validate_on_submit():
        session = create_session()
        client = Client(full_name=create_client_form.full_name.data,
                        age=create_client_form.age.data,
                        phone=create_client_form.phone.data,
                        email=create_client_form.email.data)
        session.add(client)
        try:
            session.commit()
            session.close()
            return redirect("/")
        except IntegrityError:
            create_client_form.email.errors.append("Email уже используется")
            session.close()
            return render_template("create_client.html", title="Создание клиента", form=create_client_form)

    return render_template("create_client.html", title="Создание клиента", form=create_client_form)

@router.route("/create_order", methods=["GET", "POST"])
@login_required
def create_order():
    create_order_form = CreateOrderForm()
    if create_order_form.validate_on_submit():
        session = create_session()

@router.route("/create_order", methods=["GET", "POST"])
@login_required
def create_order():
    create_order_form = CreateOrderForm()
    if create_order_form.validate_on_submit():
        client = create_order_form.client_list.data
        session = create_session()
        order = Order(price=create_order_form.price.data,
                      title=create_order_form.price.data,
                      describtion=create_order_form.describtion.data)
        # чтобы получить order_id сначала добавим в базу
        session.add(order)
        session.commit()

        # связываем M:M
        employee_order = EmployeeOrder(id_employee=current_user.id,
                                       id_order=order.id)
        client_order = ClientOrder(id_client=client.id,
                                   id_order=order.id)

        session.add(client_order)
        session.add(employee_order)
        session.commit()
        session.close()
        return redirect("/")
    return render_template("create_order.html", title="Создание заказа", form=create_order_form)


    return render_template("create_order.html", title="Создание zakaza", form=create_order_form)
@router.route("/logout")
def logout():
    logout_user()
    return redirect("/")