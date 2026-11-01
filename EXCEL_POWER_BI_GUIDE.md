# COVID-19 Trends: Excel & Power BI Guide

This guide complements the CSV dataset and Python starter script in this repository.

## Excel workflow
Create PivotTables for cases, recoveries and deaths by country and date. Use line charts for daily trends. Do not interpret this synthetic sample as official health data.

## Power BI dashboard
 Measures:
```DAX
New Cases = SUM(covid_daily[new_cases])
Recoveries = SUM(covid_daily[new_recoveries])
Deaths = SUM(covid_daily[new_deaths])
```
Dashboard: cases/recoveries/deaths cards; daily cases line chart; country comparison bar chart; date and country slicers. Data is synthetic practice data, not public-health reporting.

## Import and modelling notes
1. In Power BI Desktop choose **Get Data → Text/CSV** and select `data/dataset.csv`.
2. Rename the imported table to the name used in the DAX measures in this guide.
3. Check data types (dates as Date, counts and amounts as Whole/Decimal Number).
4. Create the measures from **Modeling → New measure**.
5. Add the suggested visuals and slicers; save your work as `dashboard.pbix` in this repository when finished.

**Important:** The supplied datasets are small synthetic practice samples. Validate field names and data types after import. The PBIX dashboard must be created and saved in Power BI Desktop; this guide does not claim a PBIX file is already included.
