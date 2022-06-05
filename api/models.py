from app import db


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    color = db.Column(db.String)
    year = db.Column(db.String)
    created_at = db.Column(db.Date)

    def to_dict(self):
        return {
            'id': self.id,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "color": self.color,
            "year": self.year,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }
