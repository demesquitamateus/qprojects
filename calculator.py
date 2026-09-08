# --- QUANT PROJECT 1: EXPECTED VALUE & SIZING ---

# 1. Inputs (Our Assumptions)
bankroll = 1000.00         # Total capital available in dollars
win_probability = 0.55     # 55% chance the trade wins
loss_probability = 0.45    # 45% chance the trade loses (1 - 0.55)

win_payout = 1.10          # Win $1.10 per $1 risked
loss_cost = 1.00           # Lose $1.00 per $1 risked

# 2. The Core Formula: Expected Value per $1 risked
# EV = (Probability of Win * Profit) - (Probability of Loss * Loss)
ev = (win_probability * win_payout) - (loss_probability * loss_cost)

print("--- TRADE ANALYSIS ---")
print("Expected Value per $1 risked:", round(ev, 4))

# 3. Decision Logic (Is this trade worth taking?)
if ev > 0:
    print("Decision: ACCEPT TRADE (+EV opportunity)")
    
    # Kelly Criterion Formula for optimal position size:
    # fraction = (p * b - q) / b
    # where p = win rate, q = loss rate, b = payout odds
    kelly_fraction = (win_probability * win_payout - loss_probability) / win_payout
    
    # Sizing in dollars
    recommended_position = bankroll * kelly_fraction
    print("Optimal Kelly Allocation:", round(kelly_fraction * 100, 2), "% of bankroll")
    print("Recommended Bet Size: $", round(recommended_position, 2))
else:
    print("Decision: REJECT TRADE (-EV opportunity)")