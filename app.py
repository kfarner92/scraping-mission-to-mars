# import necessary libraries
from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data_entries


@app.route("/scrape")
def scrape():
    db.collection.remove({})
    mars_data = scrape_mars.scrape()
    db.collection.insert_one(mars_data)
    return  render_template('scrape.html')

#  create route that renders index.html template
@app.route("/")
def index():
#if there is there is an error running because mongo is empty run this code first without the [0] index. Add it back after running once.
    mars_data = list(db.collection.find())[0]
    return render_template("index.html", mars_data=mars_data)



if __name__ == "__main__":
    app.run(debug=True)