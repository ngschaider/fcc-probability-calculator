import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, *args, **kwargs):
    self.contents = []
    for key,value in kwargs.items():
      for i in range(0, value):
        self.contents.append(key)

  def draw(self, amount):
    drawn = []
    for i in range(0, amount):
      if len(self.contents) < 1:
        break
      index = random.randrange(0, len(self.contents))
      drawn.append(self.contents[index])
      del self.contents[index]
    return drawn


"""
Next, create an experiment function in prob_calculator.py (not inside the Hat class). This function should accept the following arguments:

hat: A hat object containing balls that should be copied inside the function.
expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
num_balls_drawn: The number of balls to draw out of the hat in each experiment.
num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
The experiment function should return a probability.

For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball when you draw 5 balls from a hat containing 6 black, 4 red, and 3 green. To do this, we perform N experiments, count how many times M we get at least 2 red balls and 1 green ball, and estimate the probability as M/N. Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls, and checking if we got the balls we were attempting to draw.

Here is how you would call the experiment function based on the example above with 2000 experiments:

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
"""
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  experiment_succeeded = 0
  for i in range(0, num_experiments):
    experiment_hat = copy.deepcopy(hat)
    drawn_balls = experiment_hat.draw(num_balls_drawn)
    res = check_experiment(expected_balls, drawn_balls)
    if(res):
      experiment_succeeded += 1
  return experiment_succeeded / num_experiments
    


def check_experiment(expected_balls, drawn_balls):
  for key,value in expected_balls.items():
    if(drawn_balls.count(key) < value):
      return False
  return True