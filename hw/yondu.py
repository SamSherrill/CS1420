"""
Yondu's Plunder Calculator

This program calculates the final unit shares for Yondu, Peter Quill, and the
rest of the crew based on a set of rules and user-provided inputs.

Learning Outcomes demonstrated:
- Keyboard input (input())
- Basic data types (int, float, string)
- Type conversion (to int/float)
- Statements and expressions
- Printing to console using f-strings formatted to 2 decimal places.
"""

# --- Constants for calculation ---
# The initial individual share given to the crew (excluding Yondu and Quill).
INITIAL_CREW_SHARE = 3.0
# Yondu's cut of the total units (13%).
YONDU_CUT_PERCENTAGE = 0.13
# Peter's cut of the remaining units (11%).
PETER_CUT_PERCENTAGE = 0.11


def calculate_plunder_shares():
    """
    Reads the total units and number of pirates from the user, then computes
    the final share for Yondu, Peter, and the crew based on the problem rules.
    """
    # Get User Input and Convert to Appropriate Types
    try:
        total_pirates = int(input("How many pirates:\n"))
        total_units = float(input("How many units:\n"))
    except ValueError:
        print("Error: Please enter valid numbers for units and pirates.")
        return

    # The problem specifies that Yondu and Quill are excluded from the initial crew count.
    other_crew_count = total_pirates - 2

    # Calculate the total units distributed to the crew before Yondu and Quill take their cuts.
    initial_disbursement = other_crew_count * INITIAL_CREW_SHARE
    remaining_units = total_units - initial_disbursement

    # Yondu takes 13% of the remaining units.
    yondu_share_from_cut = round(remaining_units * YONDU_CUT_PERCENTAGE, 2)
    remaining_after_yondu = remaining_units - yondu_share_from_cut

    # Peter takes 11% of what is *left* after Yondu's cut.
    peter_share_from_cut = round(remaining_after_yondu * PETER_CUT_PERCENTAGE, 2)
    remaining_after_peter = remaining_after_yondu - peter_share_from_cut

    # The remaining amount is divided evenly among *all* pirates (including Yondu and Quill).
    final_individual_share = round(remaining_after_peter / total_pirates, 2)

    # Yondu's Final Share: His cut + his share of the final split.
    yondu_final_share = yondu_share_from_cut + final_individual_share

    # Peter's Final Share: His cut + his share of the final split.
    peter_final_share = peter_share_from_cut + final_individual_share

    # Crew's Final Share: Their initial 3 units + their share of the final split.
    crew_final_share = INITIAL_CREW_SHARE + final_individual_share

    # Print the Results
    print(f"Yondu's share: {yondu_final_share:.2f}")
    print(f"Peter's share: {peter_final_share:.2f}")
    print(f"Crew's share: {crew_final_share:.2f}")

if __name__ == "__main__":
    calculate_plunder_shares()