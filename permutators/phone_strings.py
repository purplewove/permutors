'''
Created on Nov 6, 2015

@author: clayt
'''

class StandardPhonePad():
    def __init__(self):
        self.keys = {1:[''], 
                2:['a','b','c'], 
                3:['d','e','f'], 
                4:['g','h','i'],
                5:['j','k','l'], 
                6:['m','n','o'], 
                7:['p','q','r','s'], 
                8:['t','u','v'], 
                9:['w','x','y','z']}
    
    def __getitem__(self, key):
        return self.keys[key]
    

class PhoneMessageGenerator():
    def __init__(self, phone_pad):
        self.phone_pad = phone_pad
        
    def generate_messages(self, phone_number):    
        self.phone_number = [int(x) for x in list(str(phone_number))]
        self.phone_number_pointer = 0
        self.soln = []
        self._backtrack()
        
    def _backtrack(self):
        if self._is_solution():
            self._process_solution()
        else:
            candidates = self._get_candidates()
            for candidate in candidates:
                self._make_move(candidate)
                self._backtrack()
                self._unmake_move()
                
    def _get_candidates(self):
        return self.phone_pad[self.phone_number[self.phone_number_pointer]]
    
    def _make_move(self, candidate):
        self.soln.append(candidate)
        self.phone_number_pointer += 1
        
    def _unmake_move(self):
        self.soln.pop()
        self.phone_number_pointer -= 1
        
    def _is_solution(self):
        if len(self.soln) == len(self.phone_number):
            return True
        else:
            return False
        
    def _process_solution(self):
        print (self.soln)
        
        
if __name__ == '__main__':
    phone_pad = StandardPhonePad()
    message_generator = PhoneMessageGenerator(phone_pad)
    message_generator.generate_messages(4891561)
    