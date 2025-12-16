from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
  title ='Home Page'
  return render_template('index.html',title=title)

@app.route('/about')
def about():
  title = 'About Page'
  name = 'Rapeepat'
  email = 'ztingmike@email.com'
  mobile = '088888888'
  age = 24
  return render_template(
    'about.html',
    title=title,
    name=name,
    email=email,
    mobile=mobile
)
@app.route('/favorite/food')
def favorite_food():
  title = 'Favorite Food Page'
  food = ['Pizza','Sushi','Ice Cream','KFC','Pasta']
  return render_template('favorite_food.html'
                        ,title=title,
                        food=food)

@app.route('/favorite/sport')
def favorite_sport():
  title = 'Favorite Sport Page'
  sport = ['Football','Basketball','Tennis','Swimming','Volleyball']
  return render_template('favorite_sport.html'
                        ,title=title,
                        sport=sport)