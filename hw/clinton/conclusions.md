# Was Bill Clinton Right?

## Methodology and Interpretation

The analysis was performed by making the following key interpretations of the problem:

1.  **Time Period:** The analysis covers the 52-year span from the start of 1961 through the end of 2012.
2.  **Presidential Years:** The `presidents.txt` file was constructed to match the 28 Republican years and 24 Democratic years cited in Clinton's speech, assigning an entire calendar year to the party in the presidency for the majority of that year.
3.  **Job Production:** The number of jobs "produced" in any given year is calculated as the net change in employment from the end of the previous year to the end of the next.

## Summary of Results

| Category | Clinton Claim | Calculated Data (Millions) | Difference |
| :--- | :--- | :--- | :--- |
| **Total Job Creation** | 66.0 Million | 68.068 Million | 2.068 Million |
| **Republican Job Creation** | 24.0 Million | 24.703 Million | 0.703 Million |
| **Democratic Job Creation** | 42.0 Million | 43.365 Million | 1.365 Million |

## Conclusion

Based on the specific BLS data provided and assuming we're following the same methodology as Clinton's team did, **Clinton's claimed data is ACCURATE ENOUGH (Within margin of error)**.

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

