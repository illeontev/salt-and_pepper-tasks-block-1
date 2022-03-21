class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players):
    """Метод rps_game_winner принимает на вход список игроков:
    [ ["player1", "P"], ["player2", "S"] ], где P - бумага, S - ножницы, R - камень, и
    должен функционировать следующим образом:
    • если количество игроков больше 2, необходимо вызывать исключение
    WrongNumberOfPlayersError
    • если ход игроков отличается от ‘R’, ‘P’ или ‘S’, необходимо вызывать
    исключение NoSuchStrategyError
    • в иных случаях необходимо вернуть имя и ход победителя. Если оба
    игрока походили одинаково - выигрывает первый игрок."""

    if len(players) != 2:
        raise WrongNumberOfPlayersError('There should be only 2 players')

    # win-dict показывает для каждого хода побивающий его ход
    win_dict = {'P': 'S', 'S': 'R', 'R': 'P'}
    possible_moves = win_dict.keys()

    player1, player2 = players[0], players[1]
    if player1[1] not in possible_moves:
        raise NoSuchStrategyError('Player1 made impossible move')
    if player2[1] not in possible_moves:
        raise NoSuchStrategyError('Player2 made impossible move')

    winner_move = win_dict.get(player1[1])
    # если player2 сделал победный ход, то он победил )
    if player2[1] == winner_move:
        winner = player2
    else:
        winner = player1

    return f'{winner[0]} {winner[1]}'

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
    # => WrongNumberOfPlayersError
except Exception as ex:
    print(ex)

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
    # => NoSuchStrategyError
except Exception as ex:
    print(ex)

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
    # => 'player2 S'
except Exception as ex:
    print(ex)

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
    # => 'player1 P'
except Exception as ex:
    print(ex)
