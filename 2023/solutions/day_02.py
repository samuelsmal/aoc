from functools import reduce

restriction = {"red": 12, "green": 13, "blue": 14}


def parse_game(line):
    game_id, drawings = line.split(":")
    game_id = int(game_id.split("Game ")[1])
    drawings = reduce(game_aggregator, parse_drawings(drawings.split(";")), {})

    return game_id, drawings


def parse_drawings(drawings):
    for drawing in drawings:
        dices = [d.strip().split(" ") for d in drawing.split(",")]
        yield {v: int(k) for k, v in dices}


def game_aggregator(agg, el):
    for k, v in el.items():
        if agg.get(k, 0) < v:
            agg[k] = v

    return agg


def is_game_valid(drawings, restriction):
    return all(
        drawings[r_color] <= r_color_count
        for r_color, r_color_count in restriction.items()
    )


def part_1(input_file):
    lines = [l.strip() for l in input_file]

    games = dict(map(parse_game, lines))

    return sum(
        game_id
        for game_id, drawings in games.items()
        if is_game_valid(drawings, restriction)
    )


def part_2(input_file):
    lines = [l.strip() for l in input_file]
    games = dict(map(parse_game, lines))
    return sum(
        reduce(lambda agg, el: agg * el, game.values()) for game in games.values()
    )
