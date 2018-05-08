from flask import Flask, render_template, request
import records
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
	db = records.Database('postgresql://rublan01:@localhost:2345/world')
	res = db.query('select distinct continent from country')
	return render_template('index.html', res=res)

@app.route('/procContForm')
def getData():
	db = records.Database('postgresql://rublan01:@localhost:2345/world')
	continent = request.args.get('cont')
	contCountries = db.query('select * from country where continent=:continent', continent=continent)
	return render_template('data.html', continent=continent, contCountries=contCountries), continent

@app.route('/procCountry')
def country():
	db = records.Database('postgresql://rublan01:@localhost:2345/world')
	country = request.args.get('country')
	continent = getData()
	countryList = ('select distinct name from country where continent=:continent')
	return render_template('country.html')


@app.route('/procLang')
def language():
	db = records.Database('postgresql://rublan01:@localhost:2345/world')


@app.route('/procCity')
def city():
	db = records.Database('postgresql://rublan01:@localhost:2345/world')


if __name__ == '__main__':
	app.run(debug=True)