#!/usr/bin/python3

"""Module to determine the winner of the prime game"""

def is_prime(num):
  """
  Checks if a number is prime
  Args:
    num (int): the number to check
    Returns:
        bool: True if the number is prime, otherwise False
  """
  if num < 2:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return  False
  return True 

def isWinner(x, nums):
  """
  Determine the winner of the prime game

  Args:
    x (int): The number of rounds
    nums (list): An array of n for each round

  Returns:
    str or None: The name of the player that won the most rounds
                or None if the winner can not be determined
  """
  def play_round(n):
    """
    Play one round of the prime game

    Args:
        n (int): The range of consecutive integers from 1 up to
                and including n.

    Returns:
        str: The name of the player that won the round
    """
    # Initializa the winner
    winner = "Maria"
    # Create a list to keep track of which numbers are still available
    available_nums = [True] * (n + 1)

    for i in range(2, n + 1):
        if available_nums[i] and is_prime(i):
            # Remove multiples of the chosen prime
            for j in range(i, n + 1, i):
                available_nums[j] = False
            # Switch players
            winner = "Maria" if winner == "Ben" else "Ben"
    return winner
  # Initialize the wins count for Maria and Ben
  maria_wins = 0
  ben_wins = 0
  for n in nums:
    if n > 0:
      winner = play_round(n)
      if winner == "Maria":
        maria_wins += 1
      elif winner == "Ben":
        ben_wins += 1
  # Determine the overall winner
  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None
