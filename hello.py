from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
app=Flask(__name__)


@app.route('/',methods=['GET','POST'])

def seoyeon_db():

    client=MongoClient('mongodb://localhost:27017')
    db=client.seoyeon_db
    collection=db.Champions
    results=collection.find()
    client.close()
    return render_template('index.html',data=results)

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)
