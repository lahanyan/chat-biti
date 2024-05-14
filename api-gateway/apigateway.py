from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

backend_servers = {
    'user': 'http://localhost:8080',
    'standart': 'http://localhost:8081',
    'premium': 'http://localhost:8082'
}

@app.route('/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(subpath):

    if 'v1/user/' in request.path:   
        backend = 'user'
    elif 'v1/standart/' in request.path:
        backend = 'standart'
    elif 'v1/premium/' in request.path:
        backend = 'premium'
    else:
        return jsonify({'error': 'Invalid endpoint'}), 404

    url = backend_servers[backend] + '/' + subpath
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        json=request.json
    )
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
