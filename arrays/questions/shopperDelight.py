#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'getNumberOfOptions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY priceOfJeans
#  2. INTEGER_ARRAY priceOfShoes
#  3. INTEGER_ARRAY priceOfSkirts
#  4. INTEGER_ARRAY priceOfTops
#  5. INTEGER budgeted

def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
  jeansAndShoes = []

  for jean in priceOfJeans:
    for shoe in priceOfShoes:
      jeansAndShoes.append(jean+shoe)

  skirtsAndTops = []
  for skirt in priceOfSkirts:
    for top in priceOfTops:
      skirtsAndTops.append(skirt+top)

  jeansAndShoes.sort()
  skirtsAndTops.sort(reverse=True)

  count = 0
  limit = 0

  for cost in jeansAndShoes:
    amountLeft = budgeted - cost
    # budgeted -=

    while limit < len(skirtsAndTops) and skirtsAndTops[limit] > amountLeft:
      limit += 1
    
    if limit == len(skirtsAndTops):
      break

    count += len(skirtsAndTops) - limit

  return count

if __name__ == '__main__':
  print(getNumberOfOptions([2,3], [4], [2], [1,2,3], 10))