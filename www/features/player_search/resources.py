from flask import jsonify
from flask_restful import Resource
from hfdb.queries import get_players_by_search_string
from . serializers import compile_search_results_from_player_data


class PlayerSearch(Resource):
  def get(self, search_string=None):
    players = get_players_by_search_string(search_string) if search_string else []

    return jsonify({
      'results': compile_search_results_from_player_data(players)
    })


class PlayerInfo():
  def __init__(self, json):
      parsed = self._parse_json(json)

  def _parse_json(self, json):
      player_data = json['activeplayers']['playerentry'][0]['player']
      player_team_data = json['activeplayers']['playerentry'][0]['team']

      print({
          'last_name': player_data['LastName'],
          'first_name': player_data['FirstName']
      })