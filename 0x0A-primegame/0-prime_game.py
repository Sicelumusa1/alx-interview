#!/usr/bin/python3

"""A module to determine the winner of the prime game""" 

def isWinner(x, nums):
  """
  Determine the winner of a series of games where Maria and Ben take turns removing prime numbers from a set

  Args:
    x (int): The number of rounds to play
    nums (list): A list of integers representing the upper bounds of the sets for each round
  
  Returns:
    str or None: the name of he winner or None if it is a tie
  """
  def primes_up_to_n(n):
    """
    Generate all prime numbers up to n

    Args:
      n (int): The upper bound for prime number generation

    Returns:
      list: Alist containing all prime numbers up to n
    """
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
      if  primes[p]:
        for i in range(p * p, n + 1, p):
          primes[i] = False
      p += 1
    return [i for i in range(n + 1) if primes[i]]
  
  def can_win(n):
    """
    Determine if the player whose turn is to play first can win the game

    Args:
      n (int): The upper bound for the set in the current game.
    
    Returns:
      bool: True if the starting player can win, False othrwise
    """
    primes = primes_up_to_n(n)
    if len(primes) == 0:
      return False
    return len(primes) % 2 == 1
  
  maria_wins = 0
  ben_wins = 0

  for n in nums:
    if can_win(n):
        maria_wins += 1
    else:
      ben_wins += 1
  
  # Determine the overall winner
  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None
