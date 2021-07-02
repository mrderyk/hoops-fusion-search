from www.features.player_search.resources import PlayerSearch
from www.global_dependencies import global_dependencies

global_dependencies.api.add_resource(PlayerSearch, '/search/player/<search_string>')