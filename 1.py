class wordrep:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
    def __repr__(self):
        return "{word1} {word2}.".format(word1=self.word1, word2=self.word2)

rep1 = wordrep("white", "genius")
print(rep1)