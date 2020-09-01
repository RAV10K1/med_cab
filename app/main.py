from flask import Flask, jsonify, request, make_response
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


# CORS requirement to access apis - (Courtesy-Jisha Obukwelu & Broken)
@API.before_request
def before_request():
    """ CORS preflight, required for off-server access """

    def _build_cors_prelight_response():
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response

    if request.method == "OPTIONS":
        return _build_cors_prelight_response()


@API.after_request
def after_request(response):
    """ CORS headers, required for off-server access """
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    API.run(debug=True)
