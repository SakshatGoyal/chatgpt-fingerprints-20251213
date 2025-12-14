# Remap Numbers Formula



## You (2025-01-10T07:56:56.770187+00:00)

Hey, I have a series of number that total to 223. I want to remap each of those numbers on a scale of 0 to 320. Could you give me a formula that can help me do that, but make sure that the number 223 and 320 are kept as variables so I can reuse the formula for other things.

## ChatGPT (2025-01-10T07:57:12.446080+00:00)

Certainly! To remap your series of numbers from their original scale (0 to 223) to a new scale (0 to 320), you can use the following formula:

### Formula:
\[
\text{New Value} = \left( \frac{\text{Original Value}}{\text{Old Total}} \right) \times \text{New Total}
\]

### With Variables:
\[
\text{New Value} = \left( \frac{\text{Original Value}}{A} \right) \times B
\]

Where:
- \( A \) is the old total (223 in your case).
- \( B \) is the new total (320 in your case).

### Example for a Spreadsheet:
Assume your original numbers are in column A, starting from A1, and the old total (223) is in cell B1, and the new total (320) is in cell B2. You can calculate the remapped value in column B using this formula:

\[
\text{In B1:} = (A1 / $B$1) * $B$2
\]

Drag this formula down for all the numbers in column A. This will remap each value in column A to the 0 to 320 scale.

## You (2025-01-10T08:04:56.627429+00:00)

could u give me a spreadsheet formula? in such a way that
'original value' is C2
'A' is G2
'B' is H2

## ChatGPT (2025-01-10T08:05:05.274979+00:00)

Certainly! Here's the spreadsheet formula based on your requirements:

```excel
=(C2 / $G$2) * $H$2
```

### Explanation:
- `C2` is the **Original Value**.
- `$G$2` is the **Old Total (A)** (223 in this case, but it’s flexible since you can update G2).
- `$H$2` is the **New Total (B)** (320 in this case, but it’s flexible since you can update H2).

### Steps:
1. Place your original value in column C (e.g., C2, C3, C4, etc.).
2. Enter the old total (e.g., 223) in G2.
3. Enter the new total (e.g., 320) in H2.
4. Use the formula in a new column (e.g., D2):
   ```excel
   =(C2 / $G$2) * $H$2
   ```
5. Drag the formula down to calculate for all the values in column C.

This will map all your numbers from the old scale to the new scale.
