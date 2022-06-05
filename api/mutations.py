from datetime import date
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.models import Vehicle


@convert_kwargs_to_snake_case
def create_vehicle_resolver(obj, info, manufacturer, model, color, year):
    try:
        today = date.today()
        vehicle = Vehicle(
            manufacturer=manufacturer,
            model=model,
            color=color,
            year=year,
            created_at=today.strftime("%b-%d-%Y")
        )
        db.session.add(vehicle)
        db.session.commit()
        payload = {
            "success": True,
            "vehicle": vehicle.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload


@convert_kwargs_to_snake_case
def update_vehicle_resolver(obj, info, id, manufacturer, model, color, year):
    try:
        vehicle = Vehicle.query.get(id)
        if vehicle:
            vehicle.manufacturer = manufacturer,
            vehicle.model = model,
            vehicle.color = color,
            vehicle.year = year,
        db.session.add(vehicle)
        db.session.commit()
        payload = {
            "success": True,
            "vehicle": vehicle.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload


@convert_kwargs_to_snake_case
def delete_vehicle_resolver(obj, info, id):
    try:
        vehicle = Vehicle.query.get(id)
        db.session.delete(vehicle)
        db.session.commit()
        payload = {
            "success": True,
            "vehicle": vehicle.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload
