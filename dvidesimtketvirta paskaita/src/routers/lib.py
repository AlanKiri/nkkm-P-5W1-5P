from fastapi import APIRouter
from schemas import lib


lib_router = APIRouter()

games:list[lib.Game] = []

@lib_router.post('/')
def create_game(new_game:lib.Game):
    games.append(new_game)
    return games

@lib_router.get('/')
def get_games():
    return games

@lib_router.delete('/{game_index}')
def delete_game(game_index:int):
    del games[game_index]
    return games

@lib_router.put('/{game_index}')
def update_game(game_index:int, updated_game:lib.Game):
    games[game_index] = updated_game
    return games