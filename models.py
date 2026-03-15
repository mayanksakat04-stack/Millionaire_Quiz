class Question:
    def __init__(self, id, text, options, answer):
        self._id = id
        self.text = text
        self.options = options
        self.answer = answer

    def display(self):
        print(f"\n{self._id}. {self.text}\n")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
