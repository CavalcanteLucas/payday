from flask_table import Table, Col, LinkCol

class ReservationsTable(Table):
	id = Col('Id', show=False)
	room = Col('Room')
	checkin = Col('Check-in')
	checkout = Col('Check-out')
	value = Col('Value')
	client = Col('Client')
	edit = LinkCol('Edit', 'edit_res', url_kwargs=dict(id='id'))
	delete = LinkCol('Del', 'del_res', url_kwargs=dict(id='id'))

class SpendsTable(Table):
	id = Col('Id', show=False)
	date = Col('Date')
	value = Col('Value')
	item = Col('Item')
	edit = LinkCol('Edit', 'edit_spe', url_kwargs=dict(id='id'))
	delete = LinkCol('Del', 'del_spe', url_kwargs=dict(id='id'))
