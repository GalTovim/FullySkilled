class Faq:

    """ Class Faq """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return "Question: {}, Answer:{}".format(self.question, self.answer)
