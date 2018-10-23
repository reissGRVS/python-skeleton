# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  
  #Loop from MSB only to all bits
  for i in reversed(range(16)):
      #Get relevant bits for all portfolios
      prefixes = set([abs(portfolio >> i) for portfolio in portfolios])
      
      #Shift our previous answer up 1 bit so that it muches new bit selections above
      answer <<= 1
      #We want to increase our previous max, as we are going 1 bit at a time, this is the increased value
      candidate = answer + 1
      #For each prefix check if there is a another prefix that XORs to make our candidate max value
      for p in prefixes:
          if abs(candidate ^ p) in prefixes:
              #If a match is found update the answer
              answer = candidate
              break
  return answer