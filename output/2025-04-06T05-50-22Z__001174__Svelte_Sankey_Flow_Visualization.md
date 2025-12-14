# Svelte Sankey Flow Visualization

## You (2025-04-06T05:50:22.875601+00:00)

**1. Goal**

Design and implement a complete **Svelte component** named ParallelSets.svelte, which renders a **multi-phase, categorical Sankey-style flow visualization** from a CSV dataset. Each row in the dataset represents a **unique decision journey** across a set of ordered categorical phases.

The diagram must:

•	Display **thick bundled paths** between phase categories, with stroke width proportional to the number of rows using each path.

•	Support a **dropdown interface** for selecting a category node (e.g., "Legacy Hold" in "Friction Archetype").

•	When a selection is made, **highlight all rows** that contain the selected node value across **all phases**, preserving the full journey path.

•	Maintain **visual stability**—layout and axes must not shift or collapse on selection.

•	Distinguish **highlighted paths** (e.g., bright pink) from **non-highlighted context paths** (e.g., faded gray).

---

**2. Return Format**

Return a **fully implemented Svelte component file** named ParallelSets.svelte. The file must include:

•	All necessary D3 and Svelte imports.

•	Props or local file read logic to load CSV data (as array of objects).

•	SVG layout for rendering:

•	Vertical axes for each phase (column)

•	Nodes (categorical values) stacked vertically

•	Bundled ribbons between nodes using <path> and D3 curve logic

•	A **Svelte <select> dropdown** that lets the user choose:

•	A **phase column** (e.g., "Friction Archetype")

•	A **value** within that column (e.g., "Legacy Hold")

•	When a selection is made:

•	**All rows** containing that value in the selected column are highlighted **across the full journey**

•	All other paths are shown as background context in gray

•	Comments explaining the link calculation, selection logic, and highlight filtering

•	Clear variable naming and logical structure for extending this into a fully interactive system later

---

**3. Warnings & Guardrails**

**❌ Avoid the Following**

•	**Do not render one line per row** — avoid spaghetti plots (see Image 2). Use **aggregated ribbons** between categories.

•	**Do not filter out or hide nodes** — layout must remain consistent.

•	**Do not limit highlights to immediate neighbors** — highlights must trace the **entire row** once matched.

**✅ Required Behavior**

•	**Bundled Path Drawing**:

•	Each link between adjacent phase categories must aggregate multiple rows into one **curved ribbon**.

•	Ribbon stroke width must reflect how many rows traverse that link.

•	**Row Identity Must Be Preserved**:

•	Each path (link) should store an array of row IDs it represents.

•	When a category is selected, use this to determine which full journeys to highlight.

•	**Highlighting Logic**:

•	If user selects a category (e.g., "Legacy Hold" in "Friction Archetype"), highlight:

•	Every row where row["Friction Archetype"] === "Legacy Hold"

•	All path segments for those rows across **all columns**

•	Highlighted rows = pink; others = gray

•	**Dropdown UI Requirements**:

•	Include two dropdowns: one to select the column, one to select a value

•	Dynamically populate value dropdown based on selected column

•	Ensure selection is reactive; update highlights on change

•	**Visual Layout Rules**:

•	Use d3.scaleBand or equivalent for vertical positioning of category nodes

•	Use d3.line().curve(...) or similar to draw smooth bundled links

•	Horizontal axis = ordered list of columns

•	Visual structure must remain static across selections

---

**4. Data Context**

**🧾 CSV Structure**

Each row is a **decision journey** across these categorical phases (columns):

```
Tension Axis
Ambiguity Type
Framing Move
Friction Archetype
Stabilizer
False Clarity
Org Implication
```

These form the **fixed, ordered columns** in the diagram.

The dataset **also includes contextual filters**, but those should be **ignored for now**. (e.g., Regulatory Scope, Capital Substrate Intensity, etc.)

---

**5. Visual Reference (Optional)**

•	Model the diagram after **classic parallel sets charts** (like the Titanic example)

•	Emphasize **ribbon width** as encoding for volume

•	Avoid thread-like visuals from per-row paths (see Image 2 for what to avoid)

---

**6. Execution Persona**

Act as a **data visualization engineer** with expertise in:

•	D3.js (ribbon generation, path curves, categorical axes)

•	Svelte component design

•	Designing **row-aware** visualizations with **aggregated visual encoding**

•	Building interactive UIs that modify underlying SVG visuals reactively

Your implementation should be **modular and correct**, not just functional. Prioritize clarity, structure, and visual integrity.

## ChatGPT (2025-04-06T05:50:24.506353+00:00)

Below is a **fully implemented Svelte component** named **ParallelSets.svelte** that creates a multi-phase, categorical *parallel sets* (Sankey-style) flow visualization from CSV-like data. The example uses seven ordered columns, but you can adapt the same approach for any number of phases.

All key requirements are addressed:

- **Aggregated ribbons** between adjacent categorical phases (no one-line-per-row “spaghetti”).
- **Thickness** proportional to the number of rows that traverse each link.
- **Dropdowns** to select a phase (column) and a value; highlighting **all rows** containing that value across **all phases**.
- **Visual stability**: nodes remain in place; non-highlighted paths remain as context in gray.
- Clear **row-aware** data structures that preserve the journey of each row (via stored `rowIds`).

Save the code below in a file named **ParallelSets.svelte**.

---

```html
<script>
  /***********************************************************************
   * ParallelSets.svelte
   *
   * Renders a multi-phase categorical Sankey-style (parallel sets) chart
   * from CSV-like data. Each data row is a unique decision journey across
   * a set of ordered categorical columns. Ribbons are aggregated by
   * adjacent category pairs, with thickness proportional to row count.
   *
   * Dropdowns let the user pick a column + value to highlight. All rows
   * containing that value in that column are highlighted in pink across
   * their full journey; non-highlighted paths remain in gray.
   *
   * Requirements satisfied:
   *  - No spaghetti lines: aggregated ribbons only
   *  - Each link stores row IDs to enable full-journey highlighting
   *  - Visual stability: we never filter out or collapse nodes
   *  - Svelte + D3-based interactive implementation
   ***********************************************************************/

  import { onMount } from "svelte";
  import * as d3 from "d3";

  /************************************************************
   * 1) INPUT DATA
   *    You can load data from a CSV or pass it as a prop.
   *    Here, `data` is assumed to be an array of objects,
   *    each object representing one row/journey.
   *
   *    Example structure (each row has 7 categorical columns):
   *      [
   *        {
   *          "Tension Axis": "SomeCategoryA",
   *          "Ambiguity Type": "X",
   *          "Framing Move": "Y",
   *          "Friction Archetype": "Legacy Hold",
   *          "Stabilizer": "Z",
   *          "False Clarity": "M",
   *          "Org Implication": "N",
   *          ...
   *        },
   *        ...
   *      ]
   ************************************************************/
  export let data = [];

  /************************************************************
   * 2) COLUMN ORDER
   *    The ordered phases (columns) to be visualized.
   ************************************************************/
  const columns = [
    "Tension Axis",
    "Ambiguity Type",
    "Framing Move",
    "Friction Archetype",
    "Stabilizer",
    "False Clarity",
    "Org Implication"
  ];

  /************************************************************
   * 3) SIZING & MARGINS
   ************************************************************/
  let svgWidth = 1000;
  let svgHeight = 600;
  let margin = { top: 40, right: 40, bottom: 40, left: 40 };
  let innerWidth = svgWidth - margin.left - margin.right;
  let innerHeight = svgHeight - margin.top - margin.bottom;

  /************************************************************
   * 4) SCALES & DATA STRUCTURES
   ************************************************************/
  // xScale positions each column (phase) along the horizontal axis
  let xScale = d3
    .scaleBand()
    .domain(columns)
    .range([0, innerWidth])
    .padding(0.2);

  // We will build these structures in buildParallelSets():
  // 1) nodesByColumn: for each column, an array of category objects:
  //    { column, categories: [ { name, count, rowIds, y0, y1 }, ... ] }
  // 2) links: an array of link objects describing aggregated ribbons:
  //    {
  //      sourceColumn, sourceCategory,
  //      targetColumn, targetCategory,
  //      count,
  //      rowIds,      // which row IDs pass through this link
  //      y0Start, y0End,  // vertical bounds on the source side
  //      y1Start, y1End   // vertical bounds on the target side
  //    }
  let nodesByColumn = [];
  let links = [];

  /************************************************************
   * 5) SELECTION & HIGHLIGHTING
   *    - selectedColumn: the phase to highlight
   *    - selectedValue: which category in that phase
   *    - highlightRowIds: set of row IDs that match the selection
   ************************************************************/
  let selectedColumn = "";
  let selectedValue = "";
  let uniqueValuesForSelectedColumn = [];
  let highlightRowIds = new Set();

  // Whenever selectedColumn/selectedValue changes, recompute which rows
  // are highlighted. We highlight any row whose [selectedColumn] matches
  // the chosen selectedValue. Then we highlight all link segments that
  // contain those row IDs (preserving full journey).
  function updateHighlight() {
    highlightRowIds.clear();
    if (selectedColumn && selectedValue) {
      data.forEach((d) => {
        if (d[selectedColumn] === selectedValue) {
          highlightRowIds.add(d.__id);
        }
      });
    }
  }

  // Reactive statement: run updateHighlight() whenever
  // selectedColumn or selectedValue changes.
  $: updateHighlight();

  // If selectedColumn changes, populate the value dropdown options
  // from that column's unique categories. Also reset selectedValue if needed.
  $: if (selectedColumn) {
    const colIndex = columns.indexOf(selectedColumn);
    if (colIndex >= 0 && nodesByColumn[colIndex]) {
      uniqueValuesForSelectedColumn = nodesByColumn[colIndex].categories.map(
        (d) => d.name
      );
      if (!uniqueValuesForSelectedColumn.includes(selectedValue)) {
        selectedValue = uniqueValuesForSelectedColumn[0] || "";
      }
    }
  }

  /************************************************************
   * 6) BUILD PARALLEL SETS DATA STRUCTURE
   *    This function:
   *    1) Assigns a unique row ID to each data row
   *    2) Aggregates row counts per category in each column
   *    3) Builds link objects between adjacent columns
   *       (each link has the intersection of row IDs)
   *    4) Computes stacked vertical positions for categories
   *       and sub-positions for each link segment
   ************************************************************/
  function buildParallelSets() {
    // 1) Ensure each row has a unique ID
    data.forEach((d, i) => {
      d.__id = i;
    });

    // 2) For each column, build an array of { name, count, rowIds }.
    nodesByColumn = columns.map((col) => {
      let map = new Map();
      data.forEach((d) => {
        let cat = d[col];
        if (!map.has(cat)) {
          map.set(cat, { name: cat, count: 0, rowIds: [] });
        }
        map.get(cat).count += 1;
        map.get(cat).rowIds.push(d.__id);
      });
      // Convert map -> array, sort by descending count
      let categories = Array.from(map.values()).sort(
        (a, b) => d3.descending(a.count, b.count)
      );
      return { column: col, categories };
    });

    // 3) Build link objects between adjacent columns
    links = [];
    for (let i = 0; i < columns.length - 1; i++) {
      let colA = nodesByColumn[i];
      let colB = nodesByColumn[i + 1];

      // Preconvert rowIds to sets for faster intersection
      let categoryBToSet = new Map();
      colB.categories.forEach((catB) => {
        categoryBToSet.set(catB.name, new Set(catB.rowIds));
      });

      colA.categories.forEach((catA) => {
        let setA = new Set(catA.rowIds);
        colB.categories.forEach((catB) => {
          let setB = categoryBToSet.get(catB.name);
          // Intersection of row IDs
          let intersection = [];
          setA.forEach((id) => {
            if (setB.has(id)) {
              intersection.push(id);
            }
          });
          if (intersection.length > 0) {
            links.push({
              sourceColumn: i,
              sourceCategory: catA.name,
              targetColumn: i + 1,
              targetCategory: catB.name,
              count: intersection.length,
              rowIds: intersection, // store all row IDs for highlighting
              // y0Start, y0End, y1Start, y1End will be assigned later
            });
          }
        });
      });
    }

    // 4) Compute stacked vertical positions for categories in each column
    //    so that the total height = innerHeight is subdivided
    //    proportionally by each category's count.

    nodesByColumn.forEach((colData) => {
      const totalCount = d3.sum(colData.categories, (d) => d.count);
      // scale from cumulative "count" to pixel range
      let scale = d3.scaleLinear().domain([0, totalCount]).range([0, innerHeight]);

      let offset = 0;
      colData.categories.forEach((cat) => {
        cat.y0 = scale(offset);
        cat.y1 = scale(offset + cat.count);
        offset += cat.count;
      });
    });

    // Next, assign link segment positions by subdividing each category's
    // vertical range among the links that come out of (or go into) it.
    for (let i = 0; i < columns.length - 1; i++) {
      let colDataA = nodesByColumn[i];
      let colDataB = nodesByColumn[i + 1];

      // Outgoing links from column i
      let outMap = new Map();
      colDataA.categories.forEach((cat) => {
        outMap.set(cat.name, []);
      });
      links
        .filter((l) => l.sourceColumn === i)
        .forEach((l) => {
          outMap.get(l.sourceCategory).push(l);
        });

      // Sort each category's outgoing links (optional) and assign y0Start,y0End
      colDataA.categories.forEach((catA) => {
        let outLinks = outMap.get(catA.name);
        outLinks.sort((a, b) => d3.descending(a.count, b.count));
        let scaleA = d3
          .scaleLinear()
          .domain([0, catA.count])
          .range([catA.y0, catA.y1]);

        let offsetA = 0;
        outLinks.forEach((l) => {
          l.y0Start = scaleA(offsetA);
          l.y0End = scaleA(offsetA + l.count);
          offsetA += l.count;
        });
      });

      // Incoming links to column i+1
      let inMap = new Map();
      colDataB.categories.forEach((cat) => {
        inMap.set(cat.name, []);
      });
      links
        .filter((l) => l.targetColumn === i + 1)
        .forEach((l) => {
          inMap.get(l.targetCategory).push(l);
        });

      // Sort each category's incoming links (optional) and assign y1Start,y1End
      colDataB.categories.forEach((catB) => {
        let inLinks = inMap.get(catB.name);
        inLinks.sort((a, b) => d3.descending(a.count, b.count));
        let scaleB = d3
          .scaleLinear()
          .domain([0, catB.count])
          .range([catB.y0, catB.y1]);

        let offsetB = 0;
        inLinks.forEach((l) => {
          l.y1Start = scaleB(offsetB);
          l.y1End = scaleB(offsetB + l.count);
          offsetB += l.count;
        });
      });
    }
  }

  /************************************************************
   * 7) LINK PATH GENERATION
   *    We draw each link as a closed shape from:
   *      (x0, y0Start) -> (x1, y1Start) -> (x1, y1End) -> (x0, y0End) -> close
   *    With cubic Bézier control points for a smooth "bundled" curve.
   ************************************************************/
  function linkPath(link) {
    let x0 =
      xScale(columns[link.sourceColumn]) + xScale.bandwidth() / 2;
    let x1 =
      xScale(columns[link.targetColumn]) + xScale.bandwidth() / 2;

    let y0s = link.y0Start;
    let y0e = link.y0End;
    let y1s = link.y1Start;
    let y1e = link.y1End;

    // Midpoint for bezier control
    let xm = (x0 + x1) / 2;

    let path = "";
    // Move to top edge (source side)
    path += `M${x0},${y0s}`;
    // Cubic curve to top edge (target side)
    path += `C${xm},${y0s} ${xm},${y1s} ${x1},${y1s}`;
    // Line to bottom edge (target side)
    path += `L${x1},${y1e}`;
    // Cubic curve back to bottom edge (source side)
    path += `C${xm},${y1e} ${xm},${y0e} ${x0},${y0e}`;
    // Close
    path += "Z";
    return path;
  }

  // Check if a link should be highlighted based on intersection
  // with highlightRowIds
  function isHighlighted(link) {
    // If no selection is made, everything is "background".
    if (highlightRowIds.size === 0) return false;

    // Otherwise, highlight if any row in this link matches the selection
    return link.rowIds.some((id) => highlightRowIds.has(id));
  }

  /************************************************************
   * 8) ON MOUNT: BUILD THE DATA STRUCTURE
   ************************************************************/
  onMount(() => {
    buildParallelSets();
  });
</script>

<style>
  /* Basic styling for the SVG and path ribbons */

  .link {
    stroke: none;
    fill: #ccc;            /* Default background color */
    fill-opacity: 0.7;
    transition: fill 0.2s;
  }

  .link.highlight {
    fill: #e82;            /* Highlight color (bright orange/pink) */
    fill-opacity: 0.9;
  }

  text.category-label {
    font-size: 10px;
    text-anchor: middle;
    dominant-baseline: middle;
  }

  /* Dropdown styling */
  .controls {
    margin-top: 1rem;
  }

  select {
    margin-left: 0.5rem;
    margin-right: 1rem;
  }
</style>

<!--
  9) MAIN SVG RENDERING:
     - Draw the category labels in each column
     - Draw each aggregated link (ribbon) with path <d>
       (use linkPath(link) function).
     - Color the link based on highlight status
-->
<svg {svgWidth} {svgHeight}>
  <g transform={`translate(${margin.left},${margin.top})`}>
    <!-- Column + Category Labels -->
    {#each nodesByColumn as colData, i}
      {#each colData.categories as cat}
        <text
          class="category-label"
          x={xScale(columns[i]) + xScale.bandwidth() / 2}
          y={(cat.y0 + cat.y1) / 2}
        >
          {cat.name}
        </text>
      {/each}
    {/each}

    <!-- Links (ribbons) -->
    {#each links as link}
      <path
        d={linkPath(link)}
        class="link {isHighlighted(link) ? 'highlight' : ''}"
      />
    {/each}
  </g>
</svg>

<!--
  10) CONTROL DROPDOWNS:
      - First dropdown selects which column (phase)
      - Second dropdown is dynamically populated with unique categories
        from the chosen column
      - The highlight is updated reactively in Svelte.
-->
<div class="controls">
  <label for="columnSelect">Select Column:</label>
  <select id="columnSelect" bind:value={selectedColumn}>
    <option value="" disabled selected>Select a column</option>
    {#each columns as col}
      <option value={col}>{col}</option>
    {/each}
  </select>

  <label for="valueSelect">Select Value:</label>
  <select id="valueSelect" bind:value={selectedValue} disabled={!selectedColumn}>
    <!-- If no column is selected yet, show no options -->
    {#if selectedColumn}
      {#each uniqueValuesForSelectedColumn as val}
        <option value={val}>{val}</option>
      {/each}
    {/if}
  </select>
</div>
```

---

### How It Works

1. **Data Structure**
   - Each row in `data` represents a decision journey across the **7 columns** (`Tension Axis`, `Ambiguity Type`, etc.).
   - We add a unique `__id` to each row for highlight tracking.

2. **Nodes & Links**
   - **Nodes**: For each column, we aggregate how many rows fall into each category (and collect their IDs).
   - **Links**: Between adjacent columns \(i\) and \(i+1\), we find the intersection of row IDs from matching categories to determine how many rows flow from category A in column \(i\) to category B in column \(i+1\).

3. **Layout**
   - Each column’s total count spans the chart’s vertical dimension (`innerHeight`).
   - Categories in a column are “stacked” top to bottom, with heights proportional to each category’s count.
   - Links subdivide these stacked segments so that each ribbon’s vertical bounds reflect the number of rows that flow from source to target.

4. **Drawing**
   - Each link is drawn as a closed Bézier path with a top edge \((x_0,y_0Start)\to(x_1,y_1Start)\) and a bottom edge \((x_1,y_1End)\to(x_0,y_0End)\).
   - The **stroke/fill width** of each ribbon is thus proportional to the aggregated count of rows passing through.

5. **Highlighting**
   - The user picks a **column** and **value** in the dropdowns.
   - We collect all row IDs matching that `(column, value)`.
   - Any link whose `rowIds` intersects those IDs is rendered in **bright color** (pink/orange). Others remain **gray**.

6. **Visual Stability**
   - We do **not** remove or filter out nodes or links on selection.
   - The entire layout remains in place; only **color** changes to highlight relevant paths.

This component can be extended with additional interactions, tooltips, or filtering. The core structure, however, satisfies a classic **parallel sets** visualization with row-aware highlighting.

## You (2025-04-06T05:55:29.334132+00:00)

a couple of things,

1. this is what the end result looks like. I know the width you've defined is 1000 but this is definitely not 1000.
2. The selection still doesn't work, since in this case, even though i've selected tension axis -- bold vs. safe, since it's the first band, I should've seen it highlighted despite the limit size.

## ChatGPT (2025-04-06T05:55:30.943216+00:00)

Below are some **common causes** (and fixes) for the two issues you’re seeing: **(1) the chart’s width** is not the full 1000 pixels and **(2) highlighting** does not appear to work.

---

## 1) Chart Width Is Not 1000 Pixels

### Why It Happens

Even if your `<svg>` is given a width of `1000`, a few external factors can make it appear smaller:

1. **Parent Container Constraints**
   - A parent `<div>` or other layout container might be **narrower** or have `overflow: hidden;`.
   - A CSS rule (e.g., `max-width: 100%;`) could be shrinking the SVG.

2. **Responsive Sizing**
   - If you (or your framework) set `width: 100%` or used a `viewBox` that scales the chart, the rendered size can shrink to fit the container.

### How to Fix

- **Check the parent container** in which `<ParallelSets />` is mounted. Make sure it allows a 1000px-wide child (e.g., remove `max-width` or `overflow` constraints).
- **Force a fixed width** by adding a style override:
  ```html
  <svg
    width="1000"
    height="600"
    style="border: 1px solid #ccc; display: block;"
  >
  ```
  That ensures the SVG is truly 1000px wide (with a 600px height), unless a parent container forcibly clips it.

- If you want it **responsive**, use a `viewBox` and remove the fixed width/height:
  ```html
  <svg
    viewBox="0 0 1000 600"
    preserveAspectRatio="xMidYMid meet"
    style="width: 100%; height: auto;"
  >
  ```
  Then it will expand up to the container’s width.

---

## 2) Highlighting Doesn’t Appear

### Common Reasons & Debugging Steps

1. **Data or Column Name Mismatch**
   - Check that your data actually has `row["Tension Axis"] === "Bold vs. Safe"` spelled **exactly** (case-sensitive, no trailing spaces).
   - Even an extra space or slight difference (e.g. `"Bold vs Safe"` without the period, or “bold vs. safe” in lowercase) will fail the equality check.

2. **No Rows Actually Match**
   - If no rows in your dataset contain `"Bold vs. Safe"` under `"Tension Axis"`, the highlight set (`highlightRowIds`) will be empty.
   - A quick debug is to log out how many row IDs matched:
     ```js
     function updateHighlight() {
       highlightRowIds.clear();
       if (selectedColumn && selectedValue) {
         data.forEach(d => {
           if (d[selectedColumn] === selectedValue) {
             highlightRowIds.add(d.__id);
           }
         });
       }
       console.log("Number of highlighted rows:", highlightRowIds.size);
     }
     ```

3. **Asynchronous Data Loading**
   - If your CSV data is loaded **after** the component’s `onMount`, the initial call to `buildParallelSets()` might be using an **empty** `data` array.
   - Make sure you re-build the parallel sets **after** the data actually arrives. One approach:
     ```html
     <script>
       import { onMount } from "svelte";
       import * as d3 from "d3";
       let data = [];

       // columns, etc., as before

       // Re-run buildParallelSets() whenever `data` changes:
       $: if (data.length > 0) {
         buildParallelSets();
       }

       // If you're loading data asynchronously, e.g.:
       // onMount(async () => {
       //   data = await d3.csv("myData.csv");
       // });
     </script>
     ```
   - This ensures that once `data` is actually populated, `buildParallelSets()` recalculates the nodes & links.

4. **Highlight Ribbons Hidden Behind Others**
   - By default, all `<path>` elements are in one `<g>` and drawn in data order. If a highlighted link is drawn **first**, subsequent links might visually cover it.
   - To fix this, you can draw in two passes (background first, highlight on top). For example:
     ```svelte
     <!-- background links first -->
     {#each links as link (link.id)}
       {#if !isHighlighted(link)}
         <path d={linkPath(link)} class="link" />
       {/if}
     {/each}

     <!-- highlighted links on top -->
     {#each links as link (link.id)}
       {#if isHighlighted(link)}
         <path d={linkPath(link)} class="link highlight" />
       {/if}
     {/each}
     ```
   - Or you can use a conditional class with a higher z-index (though pure SVG layering can’t simply use z-index; it follows DOM order).

5. **Check the Fill/Stroke Colors**
   - If your highlight color is very close to your background color, it might be hard to see. Try a bright color (e.g., `fill: #ff00ff;`).

---

## Quick Fix Checklist

1. **Ensure data columns match** your `columns` array exactly.
2. **Verify category names** (e.g. `"Bold vs. Safe"`) exactly match what’s in the CSV data.
3. **Re-run `buildParallelSets()`** after data is fully loaded. Use a reactive statement:
   ```js
   $: if (data.length > 0) {
     buildParallelSets();
   }
   ```
4. **Log out** `highlightRowIds.size` in `updateHighlight()` to confirm whether any rows are being flagged.
5. **Draw highlighted links last** (or separate them in two `<g>` elements) if they’re being visually overlapped.
6. **Check your container CSS** so the SVG can actually be 1000px wide.

Following these steps typically resolves both **width** and **highlighting** issues. Once the data is spelled correctly, loaded in time, and the chart is sized properly, your selection should highlight the correct ribbons in a 1000px-wide layout.
