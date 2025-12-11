import sys


def logistic_equation(P_t: float, r: float) -> float:
    """
    Calculates the population at the next time step (P_t+1) using the Logistic Equation.

    The formula is: P(t+1) = P(t) + r * P(t) * (1 - P(t))

    Args:
        P_t: Population at time t (as a percentage of total population).
        r: The growth rate.

    Returns:
        The population at time t+1.
    """
    # Standard discrete logistic map: P(t+1) = r * P(t) * (1 - P(t))
    return r * P_t * (1.0 - P_t)


def validate_and_parse_args():
    """
    Validates and parses command-line arguments.
    Handles incorrect argument count, invalid types, and range violations.
    """
    # Captures inputs from command line arguments (Mastery criterion)

    # Check 1: Correct number of arguments (3 values + script name)
    if len(sys.argv) != 4:
        # Handles 'no command line parameters at all' case
        print("Error: Usage requires exactly three command-line arguments:")
        print(
            "python3 simulation.py <initial_population_pct> <growth_rate> <iterations>"
        )
        # Use sys.exit(1) to stop execution on a fatal error
        sys.exit(1)

    try:
        # Check 2: Parse arguments and handle ValueError (e.g., non-numeric input)
        p_initial = float(sys.argv[1])
        growth_rate = float(sys.argv[2])
        num_iterations = int(sys.argv[3])
    except ValueError:
        print("Error: All arguments must be valid numbers.")
        print(
            "Initial population and growth rate must be floatable. Iterations must be an integer."
        )
        sys.exit(1)

    # Check 3: Validate ranges for numerical inputs (Mastery criterion)

    # Initial Population (P0) must be in the range [0, 1)
    if p_initial < 0.0 or p_initial >= 1.0:
        print(
            f"Error: Initial population P0 must be in range 0 <= P0 < 1.0. Found: {p_initial}"
        )
        sys.exit(1)

    # Growth Rate (r) for the logistic map should be 0 < r < 4
    if not (0.0 < growth_rate < 4.0):
        print(f"Error: Growth rate (r) must satisfy 0 < r < 4. Found: {growth_rate}")
        sys.exit(1)

    # Iterations
    if num_iterations <= 0:
        print(
            f"Error: Number of iterations must be a positive integer. Found: {num_iterations}"
        )
        sys.exit(1)

    return p_initial, growth_rate, num_iterations


def main():
    """
    Main function to run the population simulation and print output.
    """
    # Get and check arguments. Program will exit if validation fails.
    p_initial, growth_rate, num_iterations = validate_and_parse_args()

    current_population = p_initial

    # Print initial condition (time step 0) formatted to 3 decimal places
    print(f"0 {current_population:.3f}")

    # Use a meaningful loop (Mastery criterion) to run the simulation
    # The loop runs for the specified number of iterations (from t=1 up to num_iterations)
    for time_step in range(1, num_iterations + 1):
        # Calculate the next population value
        next_population = logistic_equation(current_population, growth_rate)

        # Print the result (time step and population) formatted to 3 decimal places
        # This addresses the 'Are values displayed to 3 decimal places?' test.
        print(f"{time_step} {next_population:.3f}")

        # Update the population for the next iteration
        current_population = next_population


# Main function with conditional execution (Mastery criterion)
if __name__ == "__main__":
    main()
