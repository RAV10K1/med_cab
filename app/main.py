from flask import Flask, jsonify
from app.model import PredictionBot

API = Flask(__name__)
API.bud_tender = PredictionBot()


@API.route("/")
def index():
    return jsonify("Welcome to Med Cabinet Strain Recommendation API")


@API.route("/recommendations/<web_input>")
def recommendations(web_input):
    rec_strains = API.bud_tender.search(web_input)
    return jsonify(rec_strains)


if __name__ == '__main__':
    API.run(debug=True)
