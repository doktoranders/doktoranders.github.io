class Student:

    def __init__(self, scores):
      self.scores = scores

    def get_scores(self, scores):
        total = 0
        for item in scores:
            total += item
        return total

scores = [55, 75, 80, 62, 77]
s1 = Student(scores)
total = s1.get_scores(scores)
print(total)