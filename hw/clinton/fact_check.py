import csv
import os

# Use the script's folder as the base directory
BASE_DIR = os.path.dirname(__file__)  # folder containing fact_check.py
JOBS_FILE = os.path.join(BASE_DIR, "BLS_private.csv")
PRESIDENTS_FILE = os.path.join(BASE_DIR, "presidents.txt")
CONCLUSIONS_FILE = os.path.join(BASE_DIR, "conclusions.md")

def read_jobs_data(file_path):
    """
    Reads the BLS jobs data file and returns a dictionary
    mapping the year (int) to a dictionary of monthly jobs (float, in thousands).
    """
    jobs_data = {}
    with open(file_path, mode='r', newline='') as file:
        # Skip header rows until the data starts (line starting with a year)
        for _ in range(12):
            next(file)
            
        reader = csv.reader(file)
        
        # Read the main data
        header = next(reader)
        months = header[1:]  # Jan, Feb, Mar, ...
        
        for row in reader:
            if not row or not row[0].isdigit():
                continue
            
            year = int(row[0])
            monthly_data = {}
            
            # The job data is in thousands, stored as strings. Convert to float.
            for i, month in enumerate(months):
                if row[i + 1]:
                    monthly_data[month] = float(row[i + 1])
                
            jobs_data[year] = monthly_data
            
    return jobs_data

def read_presidents_data(file_path):
    """
    Reads the presidents.txt file and returns a dictionary
    mapping the year (int) to the party (str).
    """
    party_by_year = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            try:
                year_str, party = line.split(',')
                party_by_year[int(year_str)] = party
            except ValueError:
                # Handle lines that don't match the expected format
                continue
                
    return party_by_year


def calculate_job_gains(jobs_data, party_by_year):
    """
    Compute net annual job gains as (Dec_this_year - Dec_prev_year)
    and aggregate those gains (values are in thousands).
    If Dec of the previous year is missing (e.g., Dec 1960),
    use Jan of the current year for calculating job changes that year.
    """
    democratic_jobs = 0.0
    republican_jobs = 0.0

    # Process the years present in the data (hard-coded for 1961-2012)
    for year in sorted(jobs_data):
        if 1961 <= year <= 2012:
            cur_dec = jobs_data.get(year, {}).get('Dec')
            prev_dec = jobs_data.get(year - 1, {}).get('Dec')

            # Fallback: if previous Dec missing, use Jan of the current year
            if prev_dec is None:
                prev_dec = jobs_data.get(year, {}).get('Jan')

            # Require a current Dec and some previous baseline to compute a gain
            if cur_dec is None or prev_dec is None:
                continue

            yearly_gain = cur_dec - prev_dec

            party = party_by_year.get(year)
            if party == 'D':
                democratic_jobs += yearly_gain
            elif party == 'R':
                republican_jobs += yearly_gain

    return democratic_jobs, republican_jobs

def generate_conclusions(democratic_jobs, republican_jobs):
    """
    Formats the analysis results and prose into the conclusions.md file.
    """
    # Convert job numbers from thousands (float) to millions (int) for prose
    # Round to 3 decimal places
    dem_millions = round(democratic_jobs / 1000, 3)
    rep_millions = round(republican_jobs / 1000, 3)
    total_millions = round((democratic_jobs + republican_jobs) / 1000, 3)

    # Clinton's claim numbers for comparison
    CLINTON_D = 42.0
    CLINTON_R = 24.0
    CLINTON_TOTAL = 66.0
    
    # Determine the verdict
    data_accuracy = ""
    if (abs(dem_millions - CLINTON_D) < (CLINTON_D * 0.1)) and (abs(rep_millions - CLINTON_R) < (CLINTON_R * 0.1)):
        # Allow for a small margin of error (e.g., 2 million) since the data source is different
        data_accuracy = "ACCURATE ENOUGH (Within margin of error)"
    else:
        data_accuracy = "NOT ACCURATE (Outside margin of error)"

    content = f"""# Was Bill Clinton Right?

## Methodology and Interpretation

The analysis was performed by making the following key interpretations of the problem:

1.  **Time Period:** The analysis covers the 52-year span from the start of 1961 through the end of 2012.
2.  **Presidential Years:** The `presidents.txt` file was constructed to match the 28 Republican years and 24 Democratic years cited in Clinton's speech, assigning an entire calendar year to the party in the presidency for the majority of that year.
3.  **Job Production:** The number of jobs "produced" in any given year is calculated as the net change in employment from the end of the previous year to the end of the next.

## Summary of Results

| Category | Clinton Claim | Calculated Data (Millions) | Difference |
| :--- | :--- | :--- | :--- |
| **Total Job Creation** | {CLINTON_TOTAL:.1f} Million | {total_millions:.3f} Million | {round(total_millions - CLINTON_TOTAL, 3):.3f} Million |
| **Republican Job Creation** | {CLINTON_R:.1f} Million | {rep_millions:.3f} Million | {round(rep_millions - CLINTON_R, 3):.3f} Million |
| **Democratic Job Creation** | {CLINTON_D:.1f} Million | {dem_millions:.3f} Million | {round(dem_millions - CLINTON_D, 3):.3f} Million |

## Conclusion

Based on the specific BLS data provided and assuming we're following the same methodology as Clinton's team did, **Clinton's claimed data is {data_accuracy}**.

***

## Bonus Question Analysis

Clinton (and almost all politicians) use these jobs statistics in misleading ways because:

1.  **Jobs are Created by Businesses, Not Governments:** While politicians can influence economic conditions through policies, regulations, and fiscal measures, they do not directly create jobs. Job creation is primarily driven by private sector businesses responding to market conditions, consumer demand, and broader economic trends. Thus, attributing job creation solely to the president / party in power is inaccurate.
2.  **Presidents Lack Direct Control:** The president does not have direct control over legislative changes. Additionally, there are many periods where the party with a president in the White House does not control both the House and Senate, limiting their ability to enact policies that could influence job creation.
3.  **The Effect of Enacted Policies is Delayed:** A president's (and their party's) economic policies take time (often a year or more) to be felt in the job market. Crediting the jobs gained in January of a new administration to that new president ignores the momentum, crises, or policies enacted by the *previous* administration. This is especially relevant in transition years.
4.  **Economic Factors are Global/Monetary:** Job creation is heavily influenced by non-partisan factors like the Federal Reserve's monetary policy, global economic cycles, technological shifts, and oil prices, none of which are directly controlled by the President. Attributing all job creation to the occupant of the White House oversimplifies complex economic reality.

**To better (but still not perfectly) reflect party influence on job creation, the analysis could be adjusted by:**

* **Lagged Credit:** Shift the credit for job creation by a year.
* **Weighted Credit:** If a party does not control the Presidency, House, and Senate, split the credit for job creation in that year, after taking into account the lag principle just mentioned.

"""
    
    with open(CONCLUSIONS_FILE, 'w') as f:
        f.write(content)

def main():
    """
    Main execution function.
    """
    # Create the directory if it doesn't exist (helpful for local testing/submission prep)
    os.makedirs(BASE_DIR, exist_ok=True)
    
    # 1. Read Data
    jobs_data = read_jobs_data(JOBS_FILE)
    party_by_year = read_presidents_data(PRESIDENTS_FILE)
    
    # 2. Calculate Gains
    democratic_jobs, republican_jobs = calculate_job_gains(jobs_data, party_by_year)
    
    # 3. Generate Output
    generate_conclusions(democratic_jobs, republican_jobs)
    
    print(f"Analysis complete. Results written to {CONCLUSIONS_FILE}")

if __name__ == '__main__':
    main()