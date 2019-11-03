from flask import Flask, jsonify, request, g
import requests
import os

app = Flask(__name__)

BASE_URL= 'https://apiv2.apifootball.com/'
API_KEY = os.getenv('API_KEY')
EPL_ID = 148

@app.before_request
def league_id():
  g.league_id = request.args.get('league_id') or EPL_ID

@app.route('/standings', methods=['GET'])
def standings():
  url = '%s?action=get_standings&league_id=%s&APIkey=%s' % (BASE_URL, g.league_id, API_KEY)
  details = requests.get(url)
  return jsonify([details.json() for info in details])

@app.route('/teams', methods=['GET'])
def teams():
  url = '%s?action=get_teams&league_id=%s&APIkey=%s' % (BASE_URL, g.league_id, API_KEY)
  teams = requests.get(url)
  return jsonify([teams.json() for team in teams])

if __name__ == '__main__':
  app.run(debug = True)
