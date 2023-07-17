class ListCoverage:
    def __init__(self, word_sequence, letter_set):
        # print(f"word_sequence={word_sequence} and letter_set={letter_set}")
        self.word_sequence = word_sequence
        self.first = self.word_sequence[0][0]
        self.last = self.word_sequence[-1][-1]
        # self.coverage=33
        self.coverage = _compute_coverage_set_from_list(letter_set, word_sequence)
        self.covered_letter_cnt = _compute_total_coverage_cnt(self.coverage)
        self.char_cnt = sum(len(word) for word in self.word_sequence)

    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last
    
    def getKey(self):
        return self.first, self.last

    def getCoverage(self):
        return self.coverage
    
    def getCoveredLetterCnt(self):
        return self.covered_letter_cnt

    def withAppended(self, other):
        new_word_sequence = self.word_sequence + other.word_sequence
        new_coverage = self.coverage | other.coverage
        result = ListCoverage(new_word_sequence, 'dummy')
        result.coverage = new_coverage
        result.covered_letter_cnt = _compute_total_coverage_cnt(result.coverage)
        return result
    
    def getUtility(self):
        return -self.char_cnt

    def __str__(self):
        cvg = bin(self.coverage)[2:].zfill(12)
        
        return f"{self.word_sequence}, ({self.first}, {self.last}) {self.char_cnt}, {self.covered_letter_cnt}, {cvg}"

def _compute_coverage_set(letter_set, candidate):
    bitset = 0
    for i, letter in enumerate(letter_set):
        if letter in candidate:
            bitset |= 1 << i
    # print(letter_set,candidate,bitset)
    return bitset

def _compute_coverage_set_from_list(letter_set, words):
    bitset = 0
    #print("GEO",letter_set,words)
    for word in words:
        bitset |= _compute_coverage_set(letter_set, word)
    return bitset

def _compute_total_coverage_cnt(bitset):
    count = 0
    while bitset != 0:
        if bitset & 1 == 1: count += 1
        bitset >>= 1
    return count
