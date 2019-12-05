from flask import Flask, escape, request, abort
import db_controller as db

app = Flask(__name__)

@app.route('/')
def test():
  res = db.getTest()
  return res

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000,debug=True)