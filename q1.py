# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  for i in reversed(range(16)):
      prefixes = set([portfolio >> i for portfolio in portfolios])
      answer <<= 1
      candidate = answer + 1

      #For each prefix check if there is an optimal XOR for current candidate answer
      for p in prefixes:
          if candidate ^ p in prefixes:
              answer = candidate
              break
  return answer