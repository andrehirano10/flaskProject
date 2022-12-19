from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/probability", methods=["POST"])
def probability():

    hand = request.form["hand"]
    hand = hand.casefold()

    # Number of possible combinations of hands
    total_combinations = 52 * 51 * 50 * 49 / (4 * 3 * 2 * 1)

    # Probability of a royal flush
    royal_flush_probability = 1 / total_combinations

    # Probability of a straight flush
    straight_flush_probability = royal_flush_probability * 10

    # Probability of a four of a kind
    four_of_a_kind_probability = straight_flush_probability * 13

    # Probability of a full house
    full_house_probability = four_of_a_kind_probability * 3

    # Probability of a flush
    flush_probability = full_house_probability * 4

    # Probability of a straight
    straight_probability = flush_probability * 5

    # Probability of a three of a kind
    three_of_a_kind_probability = straight_probability * 4

    # Probability of a two pair
    two_pair_probability = three_of_a_kind_probability * 11

    # Probability of a one pair
    one_pair_probability = two_pair_probability * 6

    # Probability of a high card
    high_card_probability = one_pair_probability * 12

    # Check the input and return the corresponding probability
    if hand == "royal flush":
        probability = royal_flush_probability
    elif hand == "straight flush":
        probability = straight_flush_probability
    elif hand == "four of a kind":
        probability = four_of_a_kind_probability
    elif hand == "full house":
        probability = full_house_probability
    elif hand == "flush":
        probability = flush_probability
    elif hand == "straight":
        probability = straight_probability
    elif hand == "three of a kind":
        probability = three_of_a_kind_probability
    elif hand == "two pair":
        probability = two_pair_probability
    elif hand == "one pair":
        probability = one_pair_probability
    elif hand == "high card":
        probability = high_card_probability
    else:
        # Return an error message if the input is not recognized
        return "Invalid input. Please enter the name of a hand (e.g. royal flush, straight flush, four of a kind, etc.)."

    # Return the probability as a string
    return f"This is the probability of getting this hand is {probability:.10f}%"

