from flask import Flask, render_template, request
from flask_cors import CORS
import recommendation


app = Flask(__name__)
CORS(app) 

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend")
def recommend():
    movie = request.args.get('movie')
    r = recommendation.results(movie)
    movie = movie.upper()
    if type(r)==type('string'):
        return render_template('recommend.html',movie=movie,r=r,t='s')
    else:
        return render_template('recommend.html',movie=movie,r=r,t='l')

if __name__=='__main__':
    app.run(port = 5000, debug = True)