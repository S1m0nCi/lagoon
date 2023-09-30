from arithmetic import Arithmetic

class Irrational_sqrt(Arithmetic):
  def __init__(self, x):
    self.x = x
  
  def square(self):
    return (self.x) ** 2


class Irrational_root(Arithmetic):
  def __init__(self, x, n):
    self.x = x
    self.n = n
  
  def n_power(self):
    return (self.x) ** (self.n)
    
  