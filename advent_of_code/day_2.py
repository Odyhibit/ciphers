def count_score(win, draw, lose, score, part):
    with open("input/day_2_input.txt", "r") as games:
        while game := games.readline().strip():
            if game in win:
                score += 6
                score += win.index(game) + 1
            if game in draw:
                score += 3
                score += draw.index(game) + 1
            if game in lose:
                score += lose.index(game) + 1
    print(part)
    print(f"Score is {score}")
    print()


def part_one():
    win =  ["C X", "A Y", "B Z"]
    draw = ["A X", "B Y", "C Z"]
    lose = ["B X", "C Y", "A Z"]
    score = 0
    count_score(win, draw, lose, score, "Part 1")


def part_two():
    win =  ["C Z", "A Z", "B Z"]
    draw = ["A Y", "B Y", "C Y"]
    lose = ["B X", "C X", "A X"]
    score = 0
    count_score(win, draw, lose, score, "Part 2")


part_one()
part_two()
