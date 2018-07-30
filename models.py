from app import db

class Reservation(db.Model):
	__tablename__ = "reservations"

	id = db.Column(db.Integer, primary_key=True)
	room = db.Column(db.String)
	checkin = db.Column(db.Date)
	checkout = db.Column(db.Date)
	value = db.Column(db.Float)
	client = db.Column(db.String)

	def __repr__(self):
		str_out = "<Room: {}>, \
				   <Check-in: {}>, \
				   <Check-out: {}>, \
				   <Value: {}>, \
				   <Client: {}>\n".format(str(self.room),
									  str(self.checkin),
									  str(self.checkout),
									  str(self.value),
									  str(self.client),)
		return str_out

class Spend(db.Model):
	__tablename__ = "spends"

	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date)
	value = db.Column(db.Float)
	item = db.Column(db.String)

	def __repr__(self):
		str_out = "<Date: {}>, \
				   <Value: {}>, \
				   <Item: {}>\n".format(str(self.date),
									  str(self.value),
									  str(self.item),)
		return str_out
