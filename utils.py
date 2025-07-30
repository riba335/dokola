def calculate_attractiscore(event):
    score = 50
    if event['price'] < 120:
        score += 20
    if "Taylor Swift" in event['name']:
        score += 20
    return min(score, 100)