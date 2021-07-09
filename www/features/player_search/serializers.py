def compile_search_results_from_player_data(player_data=[]):
  return [{
    'first_name': p.first_name,
    'last_name': p.last_name,
    'team_code': p.team_code,
    'key': p.key,
    'img_url': p.img_url,
  } for p in player_data if p.team_code]