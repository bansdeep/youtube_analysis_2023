# Build Channel Atlas in Power BI Desktop

These are rebuild assets, not a compiled PBIX. They have not been executed in Power BI Desktop. Keep the original `.pbix` as a reference and save the new report as `Channel Atlas - YouTube 2023.pbix`.

1. In a new report, open **Transform data → Manage Parameters → New Parameter**. Create `CsvPath` (Text) with the full local path to `Global YouTube Statistics.csv`.
2. Create a blank query, paste `Channels.pq` into **Advanced Editor**, name the query `Channels`, then **Close & Apply**. Mark rank and count columns as **Don't summarize** by default. Use explicit measures in aggregations.
3. Create each measure in `measures.dax` separately. Format coverage as a percentage with one decimal. Import `theme.json` from **View → Themes → Browse for themes**. Check visual contrast after applying the theme.
4. Assemble these pages:

| Page | Visuals and interactions |
| --- | --- |
| Overview | Cards for Channel Count, Median Subscribers and Recent Subscriber Coverage; horizontal bars for channel count by country and category sorted descending; sync Country and Category slicers with the Leaders page. |
| Leaders | Table with Source Rank, Channel, Country, Category, Subscribers, Lifetime Views and Recent Subscribers. Sort by Subscribers descending initially; users can change the sort. For any dedicated recent leaderboard, apply `Recent Subscribers is not blank` rather than treating missing data as zero. |
| Data quality | Cards for Recent Reporting Channels, Recent Subscriber Coverage and both Unknown counts; matrix by country with Channel Count and Recent Subscriber Coverage. Include a note about snapshot scope and source rounding. |

## Desktop acceptance checks

- With no filters, check 995 channels, 17.7M median subscribers, and 658 recent-reporting channels (66.1%).
- Select India and check the Overview and Leaders pages both filter to 168 rows before any other filters. Clear the slicer and check that totals return.
- Check that T-Series is the subscriber leader and its CSV scientific-notation lifetime views import as 228,000,000,000. Confirm blank recent counts remain blank in the table.
- Change `CsvPath` to another local copy of the same CSV and refresh. Counts should be unchanged. Save and reopen the new PBIX before distributing it.
