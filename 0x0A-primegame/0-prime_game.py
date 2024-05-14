#!/usr/bin/python3

def is_prime(num):
  if num < 2:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return  False
  return True 

def isWinner(x, nums):
  def play_round(n):
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
