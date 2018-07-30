from wtforms import DateField,SelectField, FloatField,Form, StringField

class ReservationForm(Form):
	room_choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
	room = SelectField('Room', choices=room_choices)
	checkin = DateField('Check-in', format='%d/%m/%Y')
	checkout = DateField('Check-out', format='%d/%m/%Y')
	value = FloatField('Value')
	client = StringField('Client')


class SpendForm(Form):
	date = DateField('Date', format='%d/%m/%Y')
	value = FloatField('Value')
	item = StringField('Item')