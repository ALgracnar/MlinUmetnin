from data_base import db


class Vgsales(db.Model):
    Rank = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(128), nullable=False)
    Platform = db.Column(db.String(128), nullable=False)
    Year = db.Column(db.Integer, nullable=False)
    Genre = db.Column(db.String(128), nullable=False)
    Publisher = db.Column(db.String(128), nullable=False)
    NA_Sales = db.Column(db.Float, nullable=False)
    EU_Sales = db.Column(db.Float, nullable=False)
    JP_Sales = db.Column(db.Float, nullable=False)
    Other_Sales = db.Column(db.Float, nullable=False)
    Global_Sales = db.Column(db.Float, nullable=False)