import random

def flip_coins():
    """
    Generates a list of 100 random 'H' and 'T' values.
    """
    coin_flips = []
    for _ in range(100):
        if random.randint(0, 1) == 0:
            coin_flips.append('H')
        else:
            coin_flips.append('T')
    return coin_flips

def find_streak(coin_flips):
    """
    Checks if there is a streak of 6 heads or 6 tails in the list of coin flips.
    Returns True if a streak is found, False otherwise.
    """
    current_streak = 1
    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i-1]:
            current_streak += 1
            if current_streak >= 6:
                return True
        else:
            current_streak = 1
    return False

streak_count = 0
for _ in range(10_000):
    coin_flips = flip_coins()
    if find_streak(coin_flips):
        streak_count += 1

print(f"Percentage of coin flip lists with a streak of 6 heads or tails: {streak_count / 10_000 * 100:.2f}%")