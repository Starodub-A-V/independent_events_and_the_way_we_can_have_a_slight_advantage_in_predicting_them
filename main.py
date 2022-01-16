import random
from plot_history import plot_history

# Related quantity of all events. Gives an understanding of how much the event occurs more (positive values)
# or less (negative values) than it should?
# Value for COIN:
quantity_of_each_event = {
    "HEAD": 0,
    "TAIL": 0,
}
# Value for DICE:
# quantity_of_each_event = {
#     1: 0,
#     2: 0,
#     3: 0,
#     4: 0,
#     5: 0,
#     6: 0,
# }

history = {}
for key in quantity_of_each_event.keys():
    history[key] = []
# Start prediction process when any event happened less then should by this value.
start_threshold = 0
right_prediction_number = 0
wrong_prediction_number = 0
# Approximate events number; prediction process may (probably, will) be longer.
approximate_events_number = 3000000

prediction = None
i = 0
# Go events_number iteration, then until prediction process will be finished.
while i < approximate_events_number or prediction:
    # Print progress.
    if i % (approximate_events_number * 0.25) == 0:
        print(i)

    if not prediction:
        # If NOT the prediction process:
        # go through all events, checking the threshold for starting the forecast process.
        last_number = 0
        for event, number in quantity_of_each_event.items():
            if last_number:
                if number < last_number:
                    last_number = number
                    prediction = event
            else:
                if number < -1 * start_threshold:
                    last_number = number
                    prediction = event
    else:
        # If prediction process:
        # the prediction stops if the number of events is not less (negative number) than it should be.
        if quantity_of_each_event[prediction] >= 0:
            prediction = None

    # Get one of events; all events occur with equal probability.
    result = random.choice([key for key in quantity_of_each_event.keys()])

    # Check if the prediction is correct or not and increase the corresponding counter.
    if prediction:
        if result == prediction:
            right_prediction_number += 1
        else:
            wrong_prediction_number += 1

    # Changing the related quantity.
    # For example:
    # 0. Initial value: { head: 0, tails: 0}.
    # 1. Occurred head event:
    #   1.1. Head counter + 2, so: {head: 0 + 2, tails 0} => {head: 2, tails 0}; (2 is number of possible events:
    #   head and tail).
    #   1.2. All events -1, so: { head: 2 - 1 , tails 0 - 1} => {head: 1, tails -1}.
    # 2. Occurred tail event:
    #   1.1. Tail counter + 2, so: { head: 1, tails -1 + 2} => { head: 1, tails 1}.
    #   1.2. All events -1, so: { head: 1 - 1, tails 1 - 1} => {head: 0, tails 0}.
    #
    # Increasing value of occurred event.
    quantity_of_each_event[result] += len(quantity_of_each_event)
    # Decreasing value of all events.
    for key in quantity_of_each_event.keys():
        quantity_of_each_event[key] -= 1
        # Save value to the history.
        history[key].append(quantity_of_each_event[key])

    # Increasing iteration.
    i += 1

# Print result of predictions.
print(f"\nNumber of right predictions: {right_prediction_number}\n"
      f"Number of wrong predictions: {wrong_prediction_number}")

# Calculating percentage of prediction.
if right_prediction_number + wrong_prediction_number != 0:
    percentage_of_right_predictions = right_prediction_number / (
                right_prediction_number + wrong_prediction_number) * 100
    percentage_of_predicting_at_random = 1 / len(quantity_of_each_event) * 100
    percentage_diff = percentage_of_right_predictions - percentage_of_predicting_at_random

    # Print more details.
    print(f"Predictions are right in {percentage_of_right_predictions:.4f} % of cases. This is more than predicting "
          f"at random by {percentage_diff:.4f} %.")
else:
    print("There was no good time for predictions.")

# Plot the chart.
# Note: will be pretty slow for cases with large amount of events.
plot_history(history, "Toss a coin", "Experiments", "Related quantity of events")
