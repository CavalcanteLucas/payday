from app import app
from db_setup import init_db, db_session
from forms import ReservationForm, SpendForm
from flask import flash, render_template, request, redirect
from models import Reservation, Spend
from tables import ReservationsTable, SpendsTable
import os

from utils import *

import json

init_db()

date_handler = lambda obj: (
    obj.isoformat()
    if isinstance(obj, (datetime.datetime, datetime.date))
    else None
)

@app.route('/', methods=['GET','POST'])
def index():

	total_gain = 0
	total_spend = 0

	qry_res = db_session.query(Reservation)
	reservations = qry_res.all()
	pd = PayDay(start_date, final_date)
	for reservation in reservations:
		pd.update(reservation)
		total_gain += reservation.value
	pd_Table = pd.get()
	pd_Table_context = reversed(pd_Table)


	qry_spe = db_session.query(Spend)
	spends = qry_spe.all()
	pm = PayMonth(pd)
	for spend in spends:
		pm.update(spend)
		total_spend += spend.value
	pm_Table = pm.get()
	pm_Table_asList = [line for line in pm_Table]
	pm_Table_context = reversed(pm_Table)


	# get YEAR-MONTH list as String
	year_month_List = []
	gain_List = []
	spend_List = []
	balance_List = []
	balanceCum_List = []
	for i in range(0,len(pm_Table)):
		s = "%s-%s" % (pm_Table[i][0].year, pm_Table[i][0].strftime('%b'))
		year_month_List.append(s)
		gain_List.append(pm_Table[i][6])
		spend_List.append(-pm_Table[i][7])
		balance_List.append(pm_Table[i][6] - pm_Table[i][7])
		if i==0:
			balanceCum_List.append( balance_List[i])
		else:
			balanceCum_List.append( balanceCum_List[i-1] + balance_List[i])

	return render_template('index.html', 
						   pd_Table = pd_Table_context,
						   pm_Table = pm_Table_context,
						   total_balance = (total_gain - total_spend),

						   year_month_List = year_month_List,
						   gain_List = gain_List,
						   spend_List = spend_List,
						   balance_List = balance_List,
						   balanceCum_List = balanceCum_List)

# reservations

def save_res(reservation, form, new=False):

	reservation.room = form.room.data
	reservation.checkin = form.checkin.data
	reservation.checkout = form.checkout.data
	reservation.value = form.value.data
	reservation.client = form.client.data

	if new:
		db_session.add(reservation)			        

	db_session.commit()

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

@app.route('/res', methods=['GET','POST'])
def res():
	form = ReservationForm(request.form)

	if request.method == 'POST' and form.validate():
		reservation = Reservation()
		save_res(reservation, form, new=True)
		flash('Reservation created successfully!')
		return redirect('/res')

	qry = db_session.query(Reservation)
	reservations = qry.all()

	reservationsTable = ReservationsTable(reversed(reservations))
	reservationsTable.border = True

	return render_template('res.html', 
						   form=form, 
						   reservations=reservations,
						   reservationsTable=reservationsTable)

@app.route('/res/<int:id>', methods=['GET','POST'])
def edit_res(id):
	qry = db_session.query(Reservation).filter(Reservation.id==id)
	reservation = qry.first()

	if reservation:
		form = ReservationForm(formdata=request.form,obj=reservation)
		if request.method == 'POST':
			save_res(reservation, form)
			flash('Reservation updated successfully!')
			return redirect('/res')
		return render_template('edit_res.html', form=form)

	else:
		return 'Error loaging #{id}'.format(id=id)

@app.route('/del_res/<int:id>', methods=['GET','POST'])
def del_res(id):
	qry = db_session.query(Reservation).filter(Reservation.id==id)
	reservation = qry.first()

	db_session.delete(reservation)
	db_session.commit()
		
	flash('Reservation deleted successfully!')
	return redirect('/res')


# spends

@app.route('/spe', methods=['GET','POST'])
def spe():
	form = SpendForm(request.form)

	if request.method == 'POST' and form.validate():
		spend = Spend()
		save_spe(spend, form, new=True)
		flash('Spend created successfully!')
		return redirect('/spe')

	qry = db_session.query(Spend)
	spends = qry.all()

	spendsTable = SpendsTable(reversed(spends))
	spendsTable.border = True

	return render_template('spe.html', 
						   form=form, 
						   spends=spends,
						   spendsTable=spendsTable)

def save_spe(spend, form, new=False):

	spend.date = form.date.data
	spend.value = form.value.data
	spend.item = form.item.data

	if new:
		db_session.add(spend)			        

	db_session.commit()

@app.route('/spe/<int:id>', methods=['GET','POST'])
def edit_spe(id):
	qry = db_session.query(Spend).filter(Spend.id==id)
	spend = qry.first()

	if spend:
		form = SpendForm(formdata=request.form,obj=spend)
		if request.method == 'POST':
			save_spe(spend, form)
			flash('Spend updated successfully!')
			return redirect('/spe')
		return render_template('edit_spe.html', form=form)

	else:
		return 'Error loaging #{id}'.format(id=id)

@app.route('/del_spe/<int:id>', methods=['GET','POST'])
def del_spe(id):
	qry = db_session.query(Spend).filter(Spend.id==id)
	spend = qry.first()

	db_session.delete(spend)
	db_session.commit()
		
	flash('Spend deleted successfully!')
	return redirect('/spe')
