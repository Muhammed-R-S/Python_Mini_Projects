import random

class Hat:
    def __init__(self, **balls):
        self.contents = [color for color, count in balls.items() for _ in range(count)]

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()  # return all balls in the hat
            self.contents.clear()  # empty the hat
            return drawn_balls
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    def check_balls(drawn, expected):
        drawn_counts = {color: drawn.count(color) for color in drawn}
        return all(drawn_counts.get(color, 0) >= count for color, count in expected.items())

    match_count = 0

    for _ in range(num_experiments):
        test_hat = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = test_hat.draw(num_balls_drawn)
        if check_balls(drawn_balls, expected_balls):
            match_count += 1

    return match_count / num_experiments

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(probability)
