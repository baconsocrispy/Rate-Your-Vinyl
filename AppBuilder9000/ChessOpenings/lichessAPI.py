import requests
import json
from itertools import chain
import os
import webbrowser

# Get Personal API Token from https://lichess.org/account/oauth/token
# you only need the puzzle option enabled; see https://en.wikipedia.org/wiki/Principle_of_least_privilege
# Store in Environment Variable for safe keeping (do NOT commit this to source control or others will be able to use it)
startFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq'


def request_lichess(fen):
    api_key = 'lip_q9Y0nx9iRSGx2K6iUAnd'

    # Make GET request to Lichess API
    resp = requests.get(
        'https://explorer.lichess.ovh/masters',
        params={
            'fen': fen,
            'topGames': 5,

        },
        headers={
            'Authorization': f'Bearer {api_key}'  # Need this or you will get a 401: Not Authorized response
        }
    )

    # Parse application/x-ndjson into list of JSON objects

    resp_json = []
    ndjson = resp.content.decode().split('\n')

    for json_obj in ndjson:
        if json_obj:
            resp_json.append(json.loads(json_obj))

    # Get first (most recently completed) puzzle in resp
    games_obj = resp_json[0]
    top_games = games_obj['topGames']
    # Open puzzle in web browser
    games_list = []
    for obj in top_games:
        game_resp = requests.get(
            'https://lichess.org/game/export/{}'.format(obj['id']),
            params={
                'pgnInJson': True,
                'clocks': False,
                'evals': False,

            },
            headers={
                'Authorization': f'Bearer {api_key}'  # Need this or you will get a 401: Not Authorized response
            }

        )

        games_list.append(game_resp.content.decode())
    return games_list





