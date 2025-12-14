# Score Calculation Formula



## You (2024-11-10T22:46:51.446049+00:00)

I need a complex calculation in my spreadsheet.

I have a list of invitees; each row represents an individual person. I broke down their responses into themes and patterns, spread them across different columns, and I wanna use that to create a score.

let's start with row 2 for now.

If AR has value Yes, its 2 points
If AS has value Yes, its 2 points
If AT has value Yes, its 1 point
If AU has value Yes, its 1 point
If AV has value Yes, its 1 point
If BA has value Yes, its 1 point
If BB has value Yes, its 1 point
If BC has value Yes, its 1 point
If BD has value Yes, its 1 point
If BG has value Yes, its 1 point
If BJ has value Yes, its 1 point
If S has value ‘Shift in Perspective, Inspiration from Thought Leaders, and Practical Insights Gained’, its 4 points
I want a total of all these points in the desired cell.

## ChatGPT (2024-11-10T22:46:57.527730+00:00)

Here's a formula you can use in the desired cell to calculate the score for row 2 based on your criteria:

```excel
=IF(AR2="Yes", 2, 0) + IF(AS2="Yes", 2, 0) + IF(AT2="Yes", 1, 0) + IF(AU2="Yes", 1, 0) + IF(AV2="Yes", 1, 0) + IF(BA2="Yes", 1, 0) + IF(BB2="Yes", 1, 0) + IF(BC2="Yes", 1, 0) + IF(BD2="Yes", 1, 0) + IF(BG2="Yes", 1, 0) + IF(BJ2="Yes", 1, 0) + IF(S2="Shift in Perspective, Inspiration from Thought Leaders, and Practical Insights Gained", 4, 0)
```

This formula checks each specified cell in row 2, adds the respective points if the condition is met, and totals them in the cell where you enter the formula. If you'd like to apply this to additional rows, you can adjust the row numbers accordingly.
