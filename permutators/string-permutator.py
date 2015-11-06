from collections import defaultdict
'''
Created on Nov 5, 2015
@author: clayt
StringPermuter solves 7-14 and 7-15 on p 271
'''
class StringPermuter():
    def __init__(self, string, k=None):
        self.string = string
        self.letters = self._dictify(self.string)
        self.soln = []
        if k is None or k > len(string):
            self.soln_length = len(self.string)
        else:
            self.soln_length = k
            
        
    def permute(self):
        if self._is_solution():
            self._process_solution()
        else:
            candidates = self._get_candidates()
            for candidate in candidates:
                self._make_move(candidate)
                self.permute()
                self._unmake_move(candidate)

    def _is_solution(self):
        if len(self.soln) == self.soln_length:
            return True
        else:
            return False
        
    def _get_candidates(self):
        return [key for key in self.letters.keys() if self.letters[key] > 0]
    
    def _make_move(self, candidate):
        self.letters[candidate] -= 1
        self.soln.append(candidate)
        
    def _unmake_move(self, candidate):
        self.letters[candidate] += 1
        self.soln.pop()
        
    def _process_solution(self):
        print (self.soln)
        
    def _dictify(self, string):
        dict = defaultdict(int)
        for letter in string:
            dict[letter] += 1
        return dict
        
if __name__ == '__main__':
    sp1 = StringPermuter("test")
    sp1.permute()
    
    sp2 = StringPermuter("test", 2)
    sp2.permute()
        
        
        