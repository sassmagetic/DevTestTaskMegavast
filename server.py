from flask import Flask, jsonify, request

from api import GamesAPI

app = Flask(__name__)


@app.route('/TEST', methods=['GET'])
def test():
    api = GamesAPI()
    api.save_all_games()
    return jsonify(api.get_json())


@app.route('/', methods=['GET'])
def search():
    api = GamesAPI()
    api.save_all_games()
    result = api.get_game_names()
    results = set(filter(lambda x: request.args.get('search', '').lower() in x.lower(), result))
    return jsonify(list(results))

if __name__ == '__main__':
    app.run('localhost', port=12345, debug=True)