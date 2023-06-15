from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Mozilla provides good references for Access Control at:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control

@app.route('/get_customers', methods=['GET'])
def get_customers():
    customer_list = [
        {"id": 1, "name": "John Smith", "balance": "$2000"},
        {"id": 2, "name": "Ronald Alberts", "balance": "$500"},
        {"id": 3, "name": "Raymond Sparks", "balance": "$250"},
        {"id": 4, "name": "Amy Salvador", "balance": "$890"}
    ]
    response = make_response(jsonify({'customers': customer_list}))
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    return response
