from flask import Flask, jsonify
import helpers

app = Flask(__name__)


@app.route("/<char_name>")
def get_character(char_name):
        char_details = helpers.getAllDetails(char_name)
        return jsonify(char_details)

app.run(debug=True)
