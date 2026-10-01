"""Module 4 exercise: a simple SIR model with pre-outbreak vaccination.

Change R0 and VACCINE_COVERAGE, run the script, and see how the epidemic size
changes. Find the coverage where the outbreak no longer takes off and compare
it with the herd immunity threshold 1 - 1/R0.

Run:  python sir_model.py            (prints a summary, plots if matplotlib is installed)
"""

# --- Parameters to play with -------------------------------------------------
POPULATION = 100_000
INITIAL_INFECTED = 10
R0 = 3.0                 # basic reproduction number
INFECTIOUS_DAYS = 7      # average infectious period (1 / gamma)
VACCINE_COVERAGE = 0.0   # fraction immune before the outbreak (0 to 1)
DAYS = 300
# -----------------------------------------------------------------------------


def run_sir(population, initial_infected, r0, infectious_days, coverage, days, dt=0.1):
    gamma = 1 / infectious_days
    beta = r0 * gamma
    recovered = coverage * population
    infected = float(initial_infected)
    susceptible = population - infected - recovered

    t_series, s_series, i_series, r_series = [], [], [], []
    steps_per_day = int(round(1 / dt))
    for step in range(days * steps_per_day):
        if step % steps_per_day == 0:
            t_series.append(step // steps_per_day)
            s_series.append(susceptible)
            i_series.append(infected)
            r_series.append(recovered)
        new_infections = beta * susceptible * infected / population * dt
        new_recoveries = gamma * infected * dt
        susceptible -= new_infections
        infected += new_infections - new_recoveries
        recovered += new_recoveries
    return t_series, s_series, i_series, r_series


def main():
    t, s, i, r = run_sir(POPULATION, INITIAL_INFECTED, R0, INFECTIOUS_DAYS,
                         VACCINE_COVERAGE, DAYS)
    vaccinated = VACCINE_COVERAGE * POPULATION
    total_infected = r[-1] + i[-1] - vaccinated
    peak = max(i)
    peak_day = t[i.index(peak)]
    herd_threshold = 1 - 1 / R0

    print(f"R0 = {R0}, vaccine coverage = {VACCINE_COVERAGE:.0%}")
    print(f"Effective R at start  = {R0 * (1 - VACCINE_COVERAGE):.2f}")
    print(f"Herd immunity threshold (1 - 1/R0) = {herd_threshold:.0%}")
    print(f"Peak infected = {peak:,.0f} on day {peak_day}")
    print(f"Total ever infected = {total_infected:,.0f} "
          f"({total_infected / POPULATION:.1%} of population)")

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("(Install matplotlib to see the plot.)")
        return
    plt.plot(t, s, label="Susceptible")
    plt.plot(t, i, label="Infected")
    plt.plot(t, r, label="Recovered / immune")
    plt.xlabel("Day")
    plt.ylabel("People")
    plt.title(f"SIR model: R0 = {R0}, coverage = {VACCINE_COVERAGE:.0%}")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
