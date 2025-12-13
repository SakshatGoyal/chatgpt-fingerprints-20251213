# Exploratory Data Analysis

## You (2025-04-03T07:03:20.119000+00:00)

could you do an exploratory analysis of this data? it doesn't have numbers so you'll have to rely on counts to begin your exploration.

## ChatGPT (2025-04-03T07:03:20.701502+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "import pandas as pd\n\n# Load the uploaded CSV file\nfile_path = '/mnt/data/Tagging - Compilation.csv'\ndf = pd.read_csv(file_path)\n\n# Display the first few rows of the dataset to understand its structure\ndf.head()"}

## ChatGPT (2025-04-03T07:03:26.436214+00:00)

Thanks for the context! Since this dataset is mostly categorical, we can approach the exploratory analysis using frequency counts and visual summaries to understand distribution patterns, common themes, and potential relationships between variables.

Here’s what I’ll start with:
1. **Top-level summary** of missing values and unique counts.
2. **Most frequent values** per column.
3. **Cross-tabulations** between key categorical features (e.g., Strategy Type vs. Ambiguity Type).
4. **Visualizations** (e.g., bar plots of value distributions).

Let me run that initial analysis and show you what stands out.

## ChatGPT (2025-04-03T07:03:31.122926+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Basic summary: missing values and number of unique entries per column\nsummary = pd.DataFrame({\n    'Missing Values': df.isnull().sum(),\n    'Unique Values': df.nunique(),\n    'Most Frequent Value': df.mode().iloc[0]\n})\n\nimport ace_tools as tools; tools.display_dataframe_to_user(name=\"Dataset Summary\", dataframe=summary)"}

## ChatGPT (2025-04-03T07:03:38.404212+00:00)

Here's a summary of the dataset, showing missing values, how many unique values each column contains, and the most common value in each column. From this, we can already see that several columns have a dominant category (e.g. "Unknown" appears often), which might be important in your analysis.

Would you like me to continue with visualizing the distributions of the most relevant columns? Or are you interested in diving into specific comparisons, like how "Strategy Type" relates to "Ambiguity Type"?

## You (2025-04-03T07:08:24.571000+00:00)

nest to the most frequent value column, could you add another column that counts the number of times the most frequent value appeared as a percentage.

## ChatGPT (2025-04-03T07:08:25.519539+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Calculate the count of the most frequent value as a percentage of the total for each column\nmost_frequent_counts = df.mode().iloc[0]\nmost_frequent_percentages = df.apply(lambda col: (col == most_frequent_counts[col.name]).sum() / len(col) * 100)\n\n# Add to the existing summary\nsummary['Most Frequent %'] = most_frequent_percentages.round(2)\n\ntools.display_dataframe_to_user(name=\"Enhanced Dataset Summary\", dataframe=summary)"}

## ChatGPT (2025-04-03T07:08:30.396757+00:00)

Here's the updated dataset summary with the percentage of times the most frequent value appears in each column. This helps highlight which columns are heavily dominated by a single value (like "Ambiguity Type" with "Value Clash" at 40%).

Let me know if you'd like to dive into any specific columns, do comparisons, or start charting this out visually!

## You (2025-04-03T07:12:12.999000+00:00)

could you also create two columns - one that has the least frequent value, and its adjacent column that has a percentage of how many times it appears.

## ChatGPT (2025-04-03T07:12:13.653706+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Calculate the least frequent value and its percentage for each column\nleast_frequent_values = df.apply(lambda col: col.value_counts().idxmin())\nleast_frequent_percentages = df.apply(lambda col: col.value_counts().min() / len(col) * 100)\n\n# Add new columns to the summary DataFrame\nsummary['Least Frequent Value'] = least_frequent_values\nsummary['Least Frequent %'] = least_frequent_percentages.round(2)\n\ntools.display_dataframe_to_user(name=\"Full Frequency Summary\", dataframe=summary)"}

## ChatGPT (2025-04-03T07:12:18.916200+00:00)

All set! You now have the **least frequent value** in each column, along with how often it appears as a percentage of the dataset.

This gives a nice contrast to the dominant patterns, highlighting which categories are rare and might deserve special attention (like anomalies or niche cases).

Would you like to visualize these distributions or start looking at cross-column relationships?

## You (2025-04-03T07:13:07.836000+00:00)

you can exclude Module ID as a count. Its the unique identifier for each row so we don't need to consider that in our analysis

## ChatGPT (2025-04-03T07:13:08.459936+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Exclude \"Module ID\" from the summary as it's a unique identifier\nsummary_filtered = summary.drop(index='Module ID')\n\ntools.display_dataframe_to_user(name=\"Filtered Frequency Summary\", dataframe=summary_filtered)"}

## ChatGPT (2025-04-03T07:13:12.393237+00:00)

Great — I've removed **Module ID** from the summary since it's just a unique row identifier and doesn't add analytical value.

This cleaned-up table now focuses on the meaningful categorical fields. Want to move on to some visualizations next, like bar charts of top vs. bottom categories, or comparisons between columns?

## You (2025-04-03T07:19:24.917000+00:00)

I'm wondering if you can make corrections to the data. For example, the word 'National' in Market Dispersion should actually be 'Regional'. that's an error in the data

## ChatGPT (2025-04-03T07:19:25.580995+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Replace incorrect value 'National' with the corrected value 'Regional' in the 'Market Dispersion' column\ndf['Market Dispersion'] = df['Market Dispersion'].replace('National', 'Regional')\n\n# Confirm the replacement worked by showing unique values in 'Market Dispersion'\ndf['Market Dispersion'].unique()"}

## ChatGPT (2025-04-03T07:19:29.546609+00:00)

Done! I’ve corrected the value in **Market Dispersion**, replacing all instances of **"National"** with **"Regional"**. The column now only includes: `'Regional'`, `'Global'`, and `'Localized'`.

If there are other known issues or corrections you'd like to apply to the dataset, just let me know!

## You (2025-04-03T07:20:13.681000+00:00)

ok, now could you refresh the the least frequent value columns

## ChatGPT (2025-04-03T07:20:14.325006+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Recalculate least frequent value and percentage, now that data has been corrected\nleast_frequent_values_updated = df.apply(lambda col: col.value_counts().idxmin())\nleast_frequent_percentages_updated = df.apply(lambda col: col.value_counts().min() / len(col) * 100)\n\n# Update the filtered summary\nsummary_filtered['Least Frequent Value'] = least_frequent_values_updated.drop('Module ID')\nsummary_filtered['Least Frequent %'] = least_frequent_percentages_updated.drop('Module ID').round(2)\n\ntools.display_dataframe_to_user(name=\"Updated Frequency Summary\", dataframe=summary_filtered)"}

## ChatGPT (2025-04-03T07:20:22.197697+00:00)

The least frequent values and their percentages have been refreshed to reflect the corrected data.

Let me know if you want to apply more data fixes, explore another part of the dataset, or move into visual or relational analysis!

## You (2025-04-03T07:21:40.274000+00:00)

you can also exclude the row 'functional modality'. most values are most likely unique so they won't show us a pattern

## ChatGPT (2025-04-03T07:21:41.366734+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Drop 'Functional Modality' from the summary since it's mostly unique values\nif 'Functional Modality' in summary_filtered.index:\n    summary_filtered = summary_filtered.drop(index='Functional Modality')\n\ntools.display_dataframe_to_user(name=\"Refined Frequency Summary\", dataframe=summary_filtered)"}

## ChatGPT (2025-04-03T07:21:45.809502+00:00)

Got it — I've excluded **Functional Modality** from the summary since it's likely too unique to show meaningful patterns.

If there are any other columns you’d like to clean up or drop, or if you want to move into some visuals or correlation checks, I’m ready when you are!

## You (2025-04-03T07:27:44.769000+00:00)

apply 'Business-level' strategy as a filter for this entire table

## ChatGPT (2025-04-03T07:27:45.743120+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Filter the dataset where 'Strategy Type' is 'Business-Level'\nbusiness_level_df = df[df['Strategy Type'] == 'Business-Level']\n\n# Recalculate the frequency summary for the filtered dataset\nfiltered_summary = pd.DataFrame({\n    'Missing Values': business_level_df.isnull().sum(),\n    'Unique Values': business_level_df.nunique(),\n    'Most Frequent Value': business_level_df.mode().iloc[0],\n    'Most Frequent %': business_level_df.apply(lambda col: (col == business_level_df.mode().iloc[0][col.name]).sum() / len(col) * 100).round(2),\n    'Least Frequent Value': business_level_df.apply(lambda col: col.value_counts().idxmin()),\n    'Least Frequent %': business_level_df.apply(lambda col: col.value_counts().min() / len(col) * 100).round(2)\n})\n\n# Remove 'Module ID' and 'Functional Modality' from the summary\nfiltered_summary = filtered_summary.drop(index=['Module ID', 'Functional Modality'])\n\ntools.display_dataframe_to_user(name=\"Business-Level Strategy Summary\", dataframe=filtered_summary)"}

## ChatGPT (2025-04-03T07:27:52.782730+00:00)

Here's the filtered summary focusing only on rows where **Strategy Type** is **Business-Level**.

You can now see how frequencies shift within this subset — for example, "Value Clash" becomes even more dominant in Ambiguity Type (56.4%).

Want to explore another strategy type next? Or maybe dive deeper into relationships between two columns within this filtered view?

## You (2025-04-03T07:32:53.042000+00:00)

you can remove the missing values column.

## ChatGPT (2025-04-03T07:32:54.229287+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Drop 'Missing Values' column as requested\nfiltered_summary = filtered_summary.drop(columns='Missing Values')\n\ntools.display_dataframe_to_user(name=\"Business-Level Strategy Summary (Refined)\", dataframe=filtered_summary)"}

## ChatGPT (2025-04-03T07:32:59.067079+00:00)

Cleaned up! The **Missing Values** column is now removed, giving you a sharper summary for rows under the **Business-Level** strategy.

Let me know if you'd like to slice the data by a different strategy type or compare this to another subset!

## You (2025-04-03T07:43:46.954000+00:00)

hey this has been really helpful. we've been able to indentify issues with our data using this. 

two corrections. there are incorrect entries for the 'stabilizer' column. 

For row

CATEGORICAL MODULE 13 - C2-I4, stabilizer should be: Future-Proofed
CATEGORICAL MODULE 33 - C1-I3, stabilizer should be: Tested First

Please make the necessary adjustments and update this table.

## ChatGPT (2025-04-03T07:43:47.444058+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Apply the specific corrections to the 'Stabilizer' column based on the Module ID\ndf.loc[df['Module ID'] == 'CATEGORICAL MODULE 13 - C2-I4', 'Stabilizer'] = 'Future-Proofed'\ndf.loc[df['Module ID'] == 'CATEGORICAL MODULE 33 - C1-I3', 'Stabilizer'] = 'Tested First'\n\n# Refilter the dataset for 'Business-Level' strategy after corrections\nbusiness_level_df = df[df['Strategy Type'] == 'Business-Level']\n\n# Recalculate the frequency summary\ncorrected_summary = pd.DataFrame({\n    'Unique Values': business_level_df.nunique(),\n    'Most Frequent Value': business_level_df.mode().iloc[0],\n    'Most Frequent %': business_level_df.apply(lambda col: (col == business_level_df.mode().iloc[0][col.name]).sum() / len(col) * 100).round(2),\n    'Least Frequent Value': business_level_df.apply(lambda col: col.value_counts().idxmin()),\n    'Least Frequent %': business_level_df.apply(lambda col: col.value_counts().min() / len(col) * 100).round(2)\n})\n\n# Drop 'Module ID' and 'Functional Modality' from the updated summary\ncorrected_summary = corrected_summary.drop(index=['Module ID', 'Functional Modality'])\n\ntools.display_dataframe_to_user(name=\"Corrected Business-Level Strategy Summary\", dataframe=corrected_summary)"}

## ChatGPT (2025-04-03T07:43:54.094351+00:00)

Awesome to hear this has been helpful!

I've made the corrections to the **Stabilizer** values for those two rows, and the table has been updated accordingly. You can now see that “Future-Proofed” is correctly appearing in the **least frequent values** with an updated percentage.

Let me know if you’ve got more corrections, or if you’re ready to explore trends across other strategy types or dimensions!

## You (2025-04-03T07:57:08.138000+00:00)

hey, we have columns for most frequent and least frequent. Is there a way we can make a column for something that roughly falls in between? I don't want to say average because technically its not average, but i think its more like median.

## ChatGPT (2025-04-03T07:57:10.400318+00:00)

Totally makes sense — you're aiming for a middle-ground value in terms of frequency, something like a **"median frequency value"** rather than just max or min. This gives you a sense of what a "typical" category might be in the column, without being skewed by the extremes.

Here’s what we can do:
- For each column, get the frequency counts of the values.
- Sort those frequencies.
- Pick the value that falls in the **middle of the distribution** (i.e. the one with the median frequency count).

Let me calculate that and add two new columns:
1. **Median Frequency Value**
2. **Median Frequency %** (how often that value appears in the filtered data)

Let’s do it!

## ChatGPT (2025-04-03T07:57:16.436910+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Function to compute median frequency value and its percentage\ndef get_median_frequency_value(series):\n    value_counts = series.value_counts()\n    sorted_counts = value_counts.sort_values()\n    median_index = len(sorted_counts) // 2\n    median_value = sorted_counts.index[median_index]\n    median_percentage = (sorted_counts.iloc[median_index] / len(series)) * 100\n    return median_value, round(median_percentage, 2)\n\n# Apply function to each column in the filtered business-level DataFrame\nmedian_values = {}\nmedian_percentages = {}\nfor col in corrected_summary.index:\n    value, percent = get_median_frequency_value(business_level_df[col])\n    median_values[col] = value\n    median_percentages[col] = percent\n\n# Add median frequency value and percentage to the summary\ncorrected_summary['Median Frequency Value'] = pd.Series(median_values)\ncorrected_summary['Median Frequency %'] = pd.Series(median_percentages)\n\ntools.display_dataframe_to_user(name=\"Business-Level Strategy Summary with Median\", dataframe=corrected_summary)"}

## ChatGPT (2025-04-03T07:57:29.371983+00:00)

There you go — now you've got **Median Frequency Value** and **%** added in!

This gives you a solid sense of the "middle ground" in each column — not too dominant like the most frequent, and not rare like the least frequent. Perfect for spotting what a “typical” entry might look like without bias from extremes.

Want to apply this same approach to another subset or strategy type?

## You (2025-04-03T07:58:04.316000+00:00)

mould you move the 'least frequent' columns to the far right.

## ChatGPT (2025-04-03T07:58:04.854820+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Reorder the columns to move 'Least Frequent Value' and 'Least Frequent %' to the far right\ncolumn_order = [\n    'Unique Values',\n    'Most Frequent Value', 'Most Frequent %',\n    'Median Frequency Value', 'Median Frequency %',\n    'Least Frequent Value', 'Least Frequent %'\n]\ncorrected_summary = corrected_summary[column_order]\n\ntools.display_dataframe_to_user(name=\"Reordered Business-Level Strategy Summary\", dataframe=corrected_summary)"}

## ChatGPT (2025-04-03T07:58:09.265496+00:00)

Done! The **Least Frequent** columns are now neatly placed on the far right for better readability and flow.

Let me know if you want to apply this format to another strategy type, export the table, or do anything else with the data!

## You (2025-04-04T14:13:46.215000+00:00)

Could you make a very similar table where strategy type is Adaptive and Crisis. Keep the one we made for Business-Level Strategy as is

## ChatGPT (2025-04-04T14:13:46.788976+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Filter the dataset for 'Adaptive & Crisis' strategy type\nadaptive_crisis_df = df[df['Strategy Type'] == 'Adaptive & Crisis']\n\n# Generate frequency summary for the filtered dataset\nadaptive_summary = pd.DataFrame({\n    'Unique Values': adaptive_crisis_df.nunique(),\n    'Most Frequent Value': adaptive_crisis_df.mode().iloc[0],\n    'Most Frequent %': adaptive_crisis_df.apply(\n        lambda col: (col == adaptive_crisis_df.mode().iloc[0][col.name]).sum() / len(col) * 100\n    ).round(2),\n    'Median Frequency Value': adaptive_crisis_df.apply(\n        lambda col: col.value_counts().sort_values().index[len(col.value_counts()) // 2]\n    ),\n    'Median Frequency %': adaptive_crisis_df.apply(\n        lambda col: col.value_counts().sort_values().iloc[len(col.value_counts()) // 2] / len(col) * 100\n    ).round(2),\n    'Least Frequent Value': adaptive_crisis_df.apply(lambda col: col.value_counts().idxmin()),\n    'Least Frequent %': adaptive_crisis_df.apply(lambda col: col.value_counts().min() / len(col) * 100).round(2)\n})\n\n# Drop 'Module ID' and 'Functional Modality' as they aren't analytically useful\nadaptive_summary = adaptive_summary.drop(index=['Module ID', 'Functional Modality'])\n\ntools.display_dataframe_to_user(name=\"Adaptive & Crisis Strategy Summary\", dataframe=adaptive_summary)"}

## ChatGPT (2025-04-04T14:13:52.971328+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Re-import necessary libraries after code execution state reset\nimport pandas as pd\n\n# Reload the uploaded CSV file\nfile_path = '/mnt/data/Tagging - Compilation.csv'\ndf = pd.read_csv(file_path)\n\n# Re-apply previous data corrections\ndf['Market Dispersion'] = df['Market Dispersion'].replace('National', 'Regional')\ndf.loc[df['Module ID'] == 'CATEGORICAL MODULE 13 - C2-I4', 'Stabilizer'] = 'Future-Proofed'\ndf.loc[df['Module ID'] == 'CATEGORICAL MODULE 33 - C1-I3', 'Stabilizer'] = 'Tested First'\n\n# Filter the dataset for 'Adaptive & Crisis' strategy type\nadaptive_crisis_df = df[df['Strategy Type'] == 'Adaptive & Crisis']\n\n# Generate frequency summary for the filtered dataset\nadaptive_summary = pd.DataFrame({\n    'Unique Values': adaptive_crisis_df.nunique(),\n    'Most Frequent Value': adaptive_crisis_df.mode().iloc[0],\n    'Most Frequent %': adaptive_crisis_df.apply(\n        lambda col: (col == adaptive_crisis_df.mode().iloc[0][col.name]).sum() / len(col) * 100\n    ).round(2),\n    'Median Frequency Value': adaptive_crisis_df.apply(\n        lambda col: col.value_counts().sort_values().index[len(col.value_counts()) // 2]\n    ),\n    'Median Frequency %': adaptive_crisis_df.apply(\n        lambda col: col.value_counts().sort_values().iloc[len(col.value_counts()) // 2] / len(col) * 100\n    ).round(2),\n    'Least Frequent Value': adaptive_crisis_df.apply(lambda col: col.value_counts().idxmin()),\n    'Least Frequent %': adaptive_crisis_df.apply(lambda col: col.value_counts().min() / len(col) * 100).round(2)\n})\n\n# Drop 'Module ID' and 'Functional Modality' as they aren't analytically useful\nadaptive_summary = adaptive_summary.drop(index=['Module ID', 'Functional Modality'])\n\nimport ace_tools as tools; tools.display_dataframe_to_user(name=\"Adaptive & Crisis Strategy Summary\", dataframe=adaptive_summary)"}

## ChatGPT (2025-04-04T14:14:10.842240+00:00)

It looks like the session reset, which caused the uploaded file to be lost. Could you please re-upload the **"Tagging - Compilation.csv"** file? Once you do, I’ll quickly reapply the corrections and generate the **Adaptive & Crisis** strategy summary table just like we did for the Business-Level one.

## You (2025-04-04T14:14:36.262000+00:00)

here you go

## ChatGPT (2025-04-04T14:14:36.753242+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Re-import the file\nfile_path = '/mnt/data/Tagging - Compilation.csv'\ndf = pd.read_csv(file_path)\n\n# Re-apply data corrections\ndf['Market Dispersion'] = df['Market Dispersion'].replace('National', 'Regional')\ndf.loc[df['Module ID'] == 'CATEGORICAL MODULE 13 - C2-I4', 'Stabilizer'] = 'Future-Proofed'\ndf.loc[df['Module ID'] == 'CATEGORICAL MODULE 33 - C1-I3', 'Stabilizer'] = 'Tested First'\n\n# Filter the dataset for 'Adaptive & Crisis' strategy type\nadaptive_crisis_df = df[df['Strategy Type'] == 'Adaptive & Crisis']\n\n# Generate frequency summary for the filtered dataset\nadaptive_summary = pd.DataFrame({\n    'Unique Values': adaptive_crisis_df.nunique(),\n    'Most Frequent Value': adaptive_crisis_df.mode().iloc[0],\n    'Most Frequent %': adaptive_crisis_df.apply(\n        lambda col: (col == adaptive_crisis_df.mode().iloc[0][col.name]).sum() / len(col) * 100\n    ).round(2),\n    'Median Frequency Value': adaptive_crisis_df.apply(\n        lambda col: col.value_counts().sort_values().index[len(col.value_counts()) // 2]\n    ),\n    'Median Frequency %': adaptive_crisis_df.apply(\n        lambda col: col.value_counts().sort_values().iloc[len(col.value_counts()) // 2] / len(col) * 100\n    ).round(2),\n    'Least Frequent Value': adaptive_crisis_df.apply(lambda col: col.value_counts().idxmin()),\n    'Least Frequent %': adaptive_crisis_df.apply(lambda col: col.value_counts().min() / len(col) * 100).round(2)\n})\n\n# Drop 'Module ID' and 'Functional Modality'\nadaptive_summary = adaptive_summary.drop(index=['Module ID', 'Functional Modality'])\n\n# Reorder columns to put least frequent values at the far right\ncolumn_order = [\n    'Unique Values',\n    'Most Frequent Value', 'Most Frequent %',\n    'Median Frequency Value', 'Median Frequency %',\n    'Least Frequent Value', 'Least Frequent %'\n]\nadaptive_summary = adaptive_summary[column_order]\n\nimport ace_tools as tools; tools.display_dataframe_to_user(name=\"Adaptive & Crisis Strategy Summary\", dataframe=adaptive_summary)"}

## ChatGPT (2025-04-04T14:14:56.787483+00:00)

Here’s your **Adaptive & Crisis Strategy Summary**, structured just like the Business-Level one:

- It includes the **most**, **median**, and **least** frequent values per column.
- Frequencies are expressed as percentages for quick comparison.
- "Unknown" still pops up in a few least-frequent spots, which could be worth a deeper dive or cleanup.

Let me know if you want to compare this with other strategies or visualize any patterns between them!

## You (2025-04-04T14:22:37.648000+00:00)

Sry, instead of adaptive could you use 'Functional and Tactical' as the strategy type filter

## ChatGPT (2025-04-04T14:22:38.233138+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Filter the dataset for 'Functional & Tactical' strategy type\nfunctional_tactical_df = df[df['Strategy Type'] == 'Functional & Tactical']\n\n# Generate frequency summary for the filtered dataset\nfunctional_summary = pd.DataFrame({\n    'Unique Values': functional_tactical_df.nunique(),\n    'Most Frequent Value': functional_tactical_df.mode().iloc[0],\n    'Most Frequent %': functional_tactical_df.apply(\n        lambda col: (col == functional_tactical_df.mode().iloc[0][col.name]).sum() / len(col) * 100\n    ).round(2),\n    'Median Frequency Value': functional_tactical_df.apply(\n        lambda col: col.value_counts().sort_values().index[len(col.value_counts()) // 2]\n    ),\n    'Median Frequency %': functional_tactical_df.apply(\n        lambda col: col.value_counts().sort_values().iloc[len(col.value_counts()) // 2] / len(col) * 100\n    ).round(2),\n    'Least Frequent Value': functional_tactical_df.apply(lambda col: col.value_counts().idxmin()),\n    'Least Frequent %': functional_tactical_df.apply(lambda col: col.value_counts().min() / len(col) * 100).round(2)\n})\n\n# Drop 'Module ID' and 'Functional Modality'\nfunctional_summary = functional_summary.drop(index=['Module ID', 'Functional Modality'])\n\n# Reorder columns to move least frequent values to the right\nfunctional_summary = functional_summary[[\n    'Unique Values',\n    'Most Frequent Value', 'Most Frequent %',\n    'Median Frequency Value', 'Median Frequency %',\n    'Least Frequent Value', 'Least Frequent %'\n]]\n\nimport ace_tools as tools; tools.display_dataframe_to_user(name=\"Functional & Tactical Strategy Summary\", dataframe=functional_summary)"}

## ChatGPT (2025-04-04T14:22:59.439769+00:00)

Here’s the summary filtered for **Functional & Tactical** strategy type — now showing the full breakdown of frequency patterns across key columns:

- **Cognitive Fog** is the leading ambiguity type here.
- **Capability Frame** dominates the framing move.
- Still a fair bit of **"Unknown"** showing up, especially in the **Stabilizer** column.

Let me know if you'd like to compare this with the other strategies side-by-side or explore a different lens!

## You (2025-04-04T14:26:34.165000+00:00)

Could you make a very similar table, but with no filter for strategy type. Keep the one we made for Business-Level Strategy as is

## ChatGPT (2025-04-04T14:26:34.695938+00:00)

{"content_type": "code", "language": "unknown", "response_format_name": null, "text": "# Generate frequency summary for the entire dataset (no strategy filter)\noverall_summary = pd.DataFrame({\n    'Unique Values': df.nunique(),\n    'Most Frequent Value': df.mode().iloc[0],\n    'Most Frequent %': df.apply(\n        lambda col: (col == df.mode().iloc[0][col.name]).sum() / len(col) * 100\n    ).round(2),\n    'Median Frequency Value': df.apply(\n        lambda col: col.value_counts().sort_values().index[len(col.value_counts()) // 2]\n    ),\n    'Median Frequency %': df.apply(\n        lambda col: col.value_counts().sort_values().iloc[len(col.value_counts()) // 2] / len(col) * 100\n    ).round(2),\n    'Least Frequent Value': df.apply(lambda col: col.value_counts().idxmin()),\n    'Least Frequent %': df.apply(lambda col: col.value_counts().min() / len(col) * 100).round(2)\n})\n\n# Drop 'Module ID' and 'Functional Modality' as before\noverall_summary = overall_summary.drop(index=['Module ID', 'Functional Modality'])\n\n# Reorder columns to match the layout used previously\noverall_summary = overall_summary[[\n    'Unique Values',\n    'Most Frequent Value', 'Most Frequent %',\n    'Median Frequency Value', 'Median Frequency %',\n    'Least Frequent Value', 'Least Frequent %'\n]]\n\nimport ace_tools as tools; tools.display_dataframe_to_user(name=\"Overall Strategy Summary\", dataframe=overall_summary)"}

## ChatGPT (2025-04-04T14:26:46.148490+00:00)

Here’s the **Overall Strategy Summary** (no filters applied), structured just like the previous ones:

- You can now clearly compare this baseline against the filtered strategy views.
- Useful for spotting broad patterns — like how dominant "Value Clash" and "True Clarity" are across the board.
- Also reveals a more even distribution in **Strategy Type**, with **"Innovation & Growth"** showing up as the median.

Would you like to stack these summaries together for comparison? Or maybe visualize how one column shifts across strategy types?

