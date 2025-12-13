# Parallel Set Visualization Request

## You (2025-04-05T21:14:39.339594+00:00)

Hey, i have this table. Originally this is saved as a csv file. 

| Module ID | Strategy Type | Tension Axis | Ambiguity Type | Framing Move | Friction Archetype | Stabilizer | False Clarity | Org Implication | Functional Modality | Regulatory Scope | Temporal Coupling Sensitivity | Market Dispersion | Capital Substrate Intensity | Decomposability Gradient | Temporal Value Elasticity | Knowledge Codifiability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MODULE 1 - C1-I1 | Business-Level | Lean vs. Unique | Value Clash | Evidence Frame | Unknown | Unknown | Unknown | Unknown | Channel Differentiation Strategy | Partial | Moderate | Regional | Low | Segmented | Deferred-Stable | Codified-Dominant |
| MODULE 1 - C1-I2 | Innovation & Growth | Bold vs. Safe | Cognitive Fog | Evidence Frame | Legacy Hold | Outside Approval | No Signal | Overstretched Org | Cybersecurity Architecture Design | Full | Moderate | Global | Medium | Segmented | Deferred-Stable | Codified-Dominant |
| MODULE 1 - C1-I3 | Adaptive & Crisis | Plan vs. React | Value Clash | Urgency Frame | Unknown | Future-Proofed | Unknown | Adaptive Growth | Strategic Crisis Reframing | Partial | Moderate | Regional | Medium | Segmented | Deferred-Stable | Hybrid |
| MODULE 1 - C1-I4 | Business-Level | Global vs. Local | Value Clash | Both/And Frame | Unknown | Alignment Achieved | True Clarity | Adaptive Growth | Menu Localization | Partial | Moderate | Global | Low | Segmented | Deferred-Stable | Hybrid |
| MODULE 1 - C1-I5 | Adaptive & Crisis | Plan vs. React | System Tangle | Urgency Frame | Unknown | Alignment Achieved | True Clarity | Adaptive Growth | IPO Process Adaptation | Partial | Tight | Global | Low | Segmented | Immediate-Coupled | Codified-Dominant |

I want to visualize elements of this in a parallel set (sankey like) visualization. Here’s a list of columns I want to visualize. 

| Tension Axis |
| --- |
| Ambiguity Type |
| Framing Move |
| Friction Archetype |
| Stabilizer |
| False Clarity |
| Org Implication |

And I want the following as ‘Filters’ at the top of the visualization. 

| Regulatory Scope |
| --- |
| Temporal Coupling Sensitivity |
| Market Dispersion |
| Capital Substrate Intensity |
| Decomposability Gradient |
| Temporal Value Elasticity |
| Knowledge Codifiability |

---

Hey, so I think we've already discussed that I need some kind of Sankey chart-like or parallel set data visualization for the columns described and of course I need the specific columns as filters. Now here's the catch, I don't just want the typical parallel set data visualization. So my objective is I need to begin isolating certain data sets across the flow and trying to understand their, that individual data sets flow across the journey. So...

You can imagine the first five columns that I've shared with you as almost like phases in a longer journey, like what was the tension axis when a decision was being made, what was the ambiguity type, how did people frame their goal or objective or something like that. So these are basically phases within a longer journey and each module ID is unique. So each module ID is basically a story and we are trying to capture, so each row represents specific events that happened during a series of common phases throughout the journey. Now here's what I want to understand. So let's say under tension axis we have something like lean versus unique, bold versus safe. So what I want to do is within that same visualization, try to isolate what is the data set that aligns with lean versus unique or the series of rows where tension axis equals to lean versus unique.

And then within that isolated dataset, I want to see how that flows into different types of ambiguity types, different values for framing move, and so on and so forth, and then just evaluate the entire journey. Now that, to some degree, is possible with parallel sets, because the first dimension acts as a categorical dimension. So there's no hard value, it's just basically individual categories. And I think they can be color-coded accordingly. But another catch I have is, I don't just want the parallel sets to be defined based on just the first column. I need the ability to isolate certain values in sequential columns as well. For example...

There is a column called friction archetype and then friction archetype has some values like legacy hold or unknown. So what if I need to isolate all the rows where friction archetype equals to legacy hold and then just isolate those rows and evaluate that journey throughout the flow.

In previous attempts, when we tried something like this, one of the challenges we faced was the diagram, the data visualization itself, essentially re-renders itself where, suppose I pick legacy hold as friction archetype, then what it will do is, it will simply eliminate all the other roles where friction archetype does not equal to legacy hold, and then it will make a journey accordingly, which is not necessarily bad, but we do want to calculate things within context. So, I need some kind of color coding mechanism, where if I select friction archetype equals to legacy hold, then the data visualization as it is remains as is, like it doesn't necessarily change, but we just highlight or almost surface the specific roles where friction archetype equals to legacy hold, and within the data visualization, it will look like the rest of the diagram has a lot of these gray parts, and there's a specific set of data that has a highlighted version.

Another challenge we experienced in the past is even if we let's say find some way to introduce some interaction and then we allow user to select one node within a column like building on the previous example like let's say I select legacy hold as the node for friction archetype what it will do is isolate or sort of highlight the previous and the future path where for the rows where you know friction archetype equals to legacy hold. So it'll isolate those paths for a small journey but that highlighting gets diluted as we move through other nodes for example if legacy hold in friction archetype moves to something like outside approval in stabilizer then basically the entire node of outside approval will get highlighted and then as a result all future paths where even outside approval stable sorry stabilizer is equal to outside approval is true then those get highlighted in the future path which is bad because while it shows me the path for a specific data set that I need for two phases like before friction archetype and after friction archetype it does however like dilute the remaining path because then I'm not I don't have the ability to keep that data set isolated.

Something that I'm more than willing to sacrifice is interactivity. So, one of the options someone suggested was, maybe instead of making the actual data visualization interactive, we could introduce some kind of filters. Like, for example, we keep the drop-down filters that were shared earlier as filtering, but at the same time, for the series of columns that we want to visualize in the database, for those, we can make it so that it doesn't necessarily eliminate data from the data visualization, it just highlights. So, for example, like building on the previous example, if we keep friction-archetype equals to legacy-hold, then it can basically allow us to filter or select a certain dataset where friction-archetype equals to legacy-hold, and that can essentially highlight the entire database. So, like the selected dataset will be pink, and then the rest of the thing will be gray, something like that.

------

Tell me what youv'e understood so far

## ChatGPT (2025-04-05T21:14:40.238066+00:00)

Got it — here’s a breakdown of what I understand so far, step by step, with special focus on the **structure**, your **objectives**, and the **challenges** you want to solve:

---

### 🔢 **Dataset Structure**

You have a CSV-based table where:
- Each **row** represents a **Module ID** — a unique decision-making *story* or *journey*.
- You have a fixed number of **phases** (columns) that describe different decision-making conditions (e.g., Tension Axis, Ambiguity Type, Framing Move, etc.).
- You also have several **filter fields** that are contextual or background attributes (e.g., Regulatory Scope, Market Dispersion, etc.).

---

### 🎯 **Your Objectives**

You want a **parallel sets-style visualization** (like a Sankey diagram but for categories), with the following goals:

1. **Visualizing Journeys Across Phases**
   - You want to see how decision journeys (i.e. rows/Module IDs) *flow* through a series of categorical variables (the phases).
   - Specifically, these columns:
     - Tension Axis
     - Ambiguity Type
     - Framing Move
     - Friction Archetype
     - Stabilizer
     - False Clarity
     - Org Implication

2. **Apply Contextual Filters (but don't destroy the viz)**
   - You want users to filter rows *using the following columns* (as dropdown filters or similar):
     - Regulatory Scope
     - Temporal Coupling Sensitivity
     - Market Dispersion
     - Capital Substrate Intensity
     - Decomposability Gradient
     - Temporal Value Elasticity
     - Knowledge Codifiability

3. **Isolate and Highlight, Not Filter Out**
   - The visualization should *retain the full dataset* but allow highlighting (e.g. in **pink**) of a subset of rows based on selected criteria (e.g. Friction Archetype = "Legacy Hold").
   - The *rest* of the paths should stay in view (e.g. in **gray**), so you always have the full context.
   - You *don't* want the entire diagram to re-render or re-layout just because a filter is selected — just highlight the relevant flows.

4. **Non-Interactive Path Isolation**
   - You're open to *not* having full interactivity (like clicking on a node), if instead you can select criteria via dropdowns to **highlight specific journeys**.
   - You’re okay with a *static diagram that updates based on filters* rather than a dynamic, node-clicking interface.

---

### ⚠️ Key Challenges You've Experienced (and Want to Avoid)

1. **Path Bleed in Highlighting**  
   When you highlight something like "Legacy Hold" in Friction Archetype, it often causes future phases to light up **more than they should**, because those downstream nodes are connected to *multiple upstream paths*, not just the highlighted subset.

2. **Diagram Re-Rendering**  
   Most parallel sets re-render (change the layout) when you filter — you **want to avoid this**. Instead, the layout should remain fixed, and only coloring/highlighting should change.

3. **Lack of Precise Subset Isolation**  
   You want to **isolate** a particular journey across all phases (like all rows where Tension Axis = "Lean vs. Unique") and track those rows across all phases — without the data from other rows interfering in that path.

---

### ✅ Desired Features Summary

| Feature | Must-Have? | Notes |
|--------|------------|-------|
| Parallel sets-style visualization | ✅ | With categorical phases shown in vertical bands |
| Ability to **highlight** subset of rows (paths) | ✅ | Based on any phase (e.g. Tension Axis = XYZ) |
| Filtering by contextual attributes | ✅ | Via dropdowns, without redrawing the viz |
| Color-coding: highlighted vs dimmed | ✅ | E.g. highlight in pink, dim rest in gray |
| Avoid full re-rendering on selection | ✅ | Keep layout fixed, only visual emphasis changes |
| Interactivity (click-to-highlight) | ❌ | Not needed — dropdown filter-based interaction is preferred |

---

Is all of that accurate? Want me to walk you through the best tech stack to build this next?

## You (2025-04-05T21:16:17.372501+00:00)

Yes... before we begin code... help me understand the different ways we can achieve this. And help me weigh the pros and cons of each.

## ChatGPT (2025-04-05T21:16:18.195632+00:00)

Perfect — here are **four main approaches** you can take to achieve your goal, with **pros and cons for each**, especially considering your constraints around interactivity, highlighting vs filtering, and maintaining layout consistency.

---

### **1. D3.js-based Custom Parallel Sets (Static Highlighting with Dropdown Filters)**

#### **How it works**
- Use D3.js to build a custom parallel sets chart.
- All data is rendered up front.
- Dropdown filters control which rows are *highlighted*, using color (e.g. pink), and the rest are *dimmed* (e.g. gray).
- No change in layout — just visual emphasis.

#### ✅ Pros:
- **Fully customizable**: you control layout, colors, behavior.
- **Supports your highlight-over-filter need**: full data stays on screen.
- **Can scale to more dimensions**: supports multi-phase journeys.
- **One-time rendering**: no redraw lag on user selection.

#### ❌ Cons:
- **Requires D3 expertise**: building this from scratch takes more upfront effort.
- **No out-of-the-box components**: must build parallel sets layout logic yourself (or adapt open-source code).
- **Not super friendly for large datasets**: D3 needs tuning for large row counts.

---

### **2. Observable Plot or Vega-Lite with Layered Highlights**

#### **How it works**
- Use **Vega-Lite** (or Observable Plot) to create a parallel sets chart.
- Highlights are shown as layered, colored lines.
- Base layer is full dataset in gray, highlight layer is filtered data in pink.
- Filtering done via dropdowns.

#### ✅ Pros:
- **Declarative syntax**: much easier to build than raw D3.
- **Clean highlight layering**: works well with your gray/pink vision.
- **Observable + Vega-Lite = fast prototyping**.
- **No layout recalculation**: layout stays static unless you change axes.

#### ❌ Cons:
- **Less flexible**: limited interactivity/custom flow logic.
- **More visual than analytical**: harder to track specific rows unless labeled.
- **Need to preprocess into node-link format**: parallel sets aren't first-class in Vega-Lite.

---

### **3. Sankey-style Custom Viz with Fixed Node Positions**

#### **How it works**
- Use a modified **Sankey diagram**, but treat columns as discrete steps.
- Assign each category (e.g. "Legacy Hold") a fixed vertical position.
- Filtered rows are highlighted across the flow, unfiltered ones are dimmed.

#### ✅ Pros:
- **Visual style is familiar**: users get "flow" feeling.
- **Works with color-coded subset highlighting**.
- **Good for storytelling**: makes the journey narrative clear.

#### ❌ Cons:
- **Sankey is designed for aggregations**: you’re working with rows, not sums.
- **Highlighting individual rows can clutter**: need opacity control, maybe bundling.
- **Custom layout needed**: default Sankey libraries don’t do what you want.

---

### **4. Interactive Dashboards (e.g. Plotly Dash, Tableau, PowerBI)**

#### **How it works**
- Load your dataset into a dashboard tool.
- Create a series of parallel coordinates or parallel sets plots.
- Use dropdowns to filter, and possibly create custom highlights with conditional color logic.

#### ✅ Pros:
- **No coding (mostly)**: fast to build dashboards in tools like Tableau or PowerBI.
- **Dynamic filtering + highlighting**: built-in.
- **High polish**: professional-looking outputs.

#### ❌ Cons:
- **Limited highlight-only behavior**: most dashboards *filter* data out, not dim it.
- **Layout might shift when filters applied**.
- **Exporting/embedding issues**: harder to integrate into a web app if needed.

---

### ✅ **Summary Table**

| Approach | Customization | Layout Stability | Highlight (not filter) | Tech Skill Needed | Performance | Best For |
|---------|----------------|------------------|-------------------------|-------------------|-------------|----------|
| D3.js Custom | ⭐⭐⭐⭐ | ✅✅✅ | ✅✅✅✅ | High | Medium | Fully tailored control |
| Vega-Lite | ⭐⭐ | ✅✅ | ✅✅ | Low-Medium | High | Fast, simple prototypes |
| Sankey-style Flow | ⭐⭐⭐ | ✅✅✅ | ✅✅✅ | Medium | Medium | Story-driven visuals |
| Tableau/PowerBI | ⭐ | ❌ | ❌ | Low | High | Internal dashboards |

---

### 🔧 My Recommendation (based on your goals):

Start with **D3.js Custom Parallel Sets** if:
- You want the most control over highlighting behavior and styling.
- You're okay with some upfront setup and learning curve.

Or use **Vega-Lite + Observable** if:
- You want faster prototyping.
- You can compromise slightly on layout control.

---

Would you like a side-by-side visual mockup comparing these options next? Or should we go deeper into setting one of them up — like starting with D3.js?

## You (2025-04-05T21:20:36.268525+00:00)

lets discuss everything I'll need for the D3.js custom approach.

## ChatGPT (2025-04-05T21:20:36.793898+00:00)

Great — going the **D3.js custom parallel sets** route gives you maximum control, which is perfect for your highlighting vs filtering needs. Here's **everything you'll need**, broken into clear parts.

---

## 🧱 PART 1: **Project Setup**

### 🔧 Tools
- **D3.js** (v6 or v7 preferred)
- **Svelte** (since you’re using it in your project already)
- Optional: **Tailwind CSS** for styling, if desired
- **CSV file** as your dataset (already ready)

### 📁 Project Folder Structure (assumed)
From what you shared before:
```
/Users/sakshatgoyal/Desktop/Strategic Decision Making Work/Data Viz experiment/interactive-sankey
```

Inside that, we’ll want:

```
- /public/data/modules.csv   ← your CSV file
- /src/lib/ParallelSets.svelte ← new visualization component
- /src/routes/+page.svelte     ← main page where you'll display it
```

---

## 📊 PART 2: **Data Handling**

You’ll need to:
- Load the CSV file using `d3.csv`
- Convert it into a format usable for parallel sets:
  - Each row = one Module ID
  - Columns = each “phase” in the journey (your visualization columns)

We'll also preprocess it to:
- Extract **unique categories** per column
- Build **node-link paths** connecting one column’s value to the next (per row)

---

## 🖼️ PART 3: **Rendering the Parallel Sets**

### Each **column** (Tension Axis, Ambiguity Type, etc.) becomes:
- A **vertical axis** with **rectangular blocks** (nodes)
- Each block = one category (e.g. “Value Clash” in Ambiguity Type)

### Each **row** (Module ID) becomes:
- A **path** (ribbon or line) connecting the values across columns
- Highlighted with **color** if it matches the current filter
- Gray if not matched

We’ll use:
- D3 scales (e.g. `d3.scaleBand` for y-axis categories)
- D3 path generators to draw curves
- SVG layers to render
  - All paths (gray)
  - Highlighted paths (color)

---

## 🧩 PART 4: **Dropdown Filters**

### Two sets of controls:

1. **Highlight Filters** (for the main columns in the journey)
   - E.g. dropdown to highlight where “Friction Archetype” = “Legacy Hold”
   - Affects color, not layout

2. **Contextual Filters** (your additional fields)
   - E.g. “Market Dispersion = Regional”
   - Used to filter which rows get *included* in the diagram at all (optional)

We’ll add a control panel using:
- `<select>` dropdowns
- Svelte bindings (`bind:value`)
- Triggers to update filtered/highlighted row list

---

## 🎨 PART 5: **Color & Visual Design**

- **Highlighted paths** = pink or bright color
- **Unhighlighted paths** = gray with low opacity
- Optional:
  - Add **legend**
  - Add **labels** inside the vertical axis categories
  - Add **hover tooltips** showing Module ID or details

---

## 🚀 PART 6: **Performance Considerations**

If your dataset grows:
- Avoid animating all paths
- Debounce filter updates
- Use `requestAnimationFrame` for smoother renders
- Use canvas (instead of SVG) if interactivity is reintroduced later

---

## ✅ Summary of What You'll Build

| Feature | Tool / Method |
|--------|----------------|
| Data load | `d3.csv()` |
| Axes & categories | `d3.scaleBand`, vertical SVG groups |
| Paths | Custom D3 path drawing per row |
| Highlighting | Svelte reactive variables + CSS classes |
| Filters | Svelte `<select>` dropdowns |
| Layout | SVG with groups for each column and path layers |

---

Would you like me to now:
1. **Start building the component step-by-step**, or
2. **Sketch a simple wireframe/mockup** to visualize what it’ll look like?

## You (2025-04-05T21:44:52.878951+00:00)

lets start with the structure. Here's the folder i previously had. Now I'll need to know which ones i need to change and which ones i need to keep as is. 


sakshatgoyal@MacBook-Pro ~ % tree /Users/sakshatgoyal/Desktop/interactive-sankey 
/Users/sakshatgoyal/Desktop/interactive-sankey
├── node_modules
│   ├── @esbuild
│   │   └── darwin-arm64
│   │       ├── bin
│   │       │   └── esbuild
│   │       ├── package.json
│   │       └── README.md
│   ├── commander
│   │   ├── CHANGELOG.md
│   │   ├── esm.mjs
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package-support.json
│   │   ├── package.json
│   │   ├── Readme.md
│   │   └── typings
│   │       └── index.d.ts
│   ├── d3
│   │   ├── dist
│   │   │   ├── d3.js
│   │   │   └── d3.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       └── index.js
│   ├── d3-array
│   │   ├── dist
│   │   │   ├── d3-array.js
│   │   │   └── d3-array.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── array.js
│   │       ├── ascending.js
│   │       ├── bin.js
│   │       ├── bisect.js
│   │       ├── bisector.js
│   │       ├── blur.js
│   │       ├── constant.js
│   │       ├── count.js
│   │       ├── cross.js
│   │       ├── cumsum.js
│   │       ├── descending.js
│   │       ├── deviation.js
│   │       ├── difference.js
│   │       ├── disjoint.js
│   │       ├── every.js
│   │       ├── extent.js
│   │       ├── filter.js
│   │       ├── fsum.js
│   │       ├── greatest.js
│   │       ├── greatestIndex.js
│   │       ├── group.js
│   │       ├── groupSort.js
│   │       ├── identity.js
│   │       ├── index.js
│   │       ├── intersection.js
│   │       ├── least.js
│   │       ├── leastIndex.js
│   │       ├── map.js
│   │       ├── max.js
│   │       ├── maxIndex.js
│   │       ├── mean.js
│   │       ├── median.js
│   │       ├── merge.js
│   │       ├── min.js
│   │       ├── minIndex.js
│   │       ├── mode.js
│   │       ├── nice.js
│   │       ├── number.js
│   │       ├── pairs.js
│   │       ├── permute.js
│   │       ├── quantile.js
│   │       ├── quickselect.js
│   │       ├── range.js
│   │       ├── rank.js
│   │       ├── reduce.js
│   │       ├── reverse.js
│   │       ├── scan.js
│   │       ├── shuffle.js
│   │       ├── some.js
│   │       ├── sort.js
│   │       ├── subset.js
│   │       ├── sum.js
│   │       ├── superset.js
│   │       ├── threshold
│   │       │   ├── freedmanDiaconis.js
│   │       │   ├── scott.js
│   │       │   └── sturges.js
│   │       ├── ticks.js
│   │       ├── transpose.js
│   │       ├── union.js
│   │       ├── variance.js
│   │       └── zip.js
│   ├── d3-axis
│   │   ├── dist
│   │   │   ├── d3-axis.js
│   │   │   └── d3-axis.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── axis.js
│   │       ├── identity.js
│   │       └── index.js
│   ├── d3-brush
│   │   ├── dist
│   │   │   ├── d3-brush.js
│   │   │   └── d3-brush.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── brush.js
│   │       ├── constant.js
│   │       ├── event.js
│   │       ├── index.js
│   │       └── noevent.js
│   ├── d3-chord
│   │   ├── dist
│   │   │   ├── d3-chord.js
│   │   │   └── d3-chord.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── array.js
│   │       ├── chord.js
│   │       ├── constant.js
│   │       ├── index.js
│   │       ├── math.js
│   │       └── ribbon.js
│   ├── d3-color
│   │   ├── dist
│   │   │   ├── d3-color.js
│   │   │   └── d3-color.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── color.js
│   │       ├── cubehelix.js
│   │       ├── define.js
│   │       ├── index.js
│   │       ├── lab.js
│   │       └── math.js
│   ├── d3-contour
│   │   ├── dist
│   │   │   ├── d3-contour.js
│   │   │   └── d3-contour.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── area.js
│   │       ├── array.js
│   │       ├── ascending.js
│   │       ├── constant.js
│   │       ├── contains.js
│   │       ├── contours.js
│   │       ├── density.js
│   │       ├── index.js
│   │       └── noop.js
│   ├── d3-delaunay
│   │   ├── dist
│   │   │   ├── d3-delaunay.js
│   │   │   └── d3-delaunay.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── delaunay.js
│   │       ├── index.js
│   │       ├── path.js
│   │       ├── polygon.js
│   │       └── voronoi.js
│   ├── d3-dispatch
│   │   ├── dist
│   │   │   ├── d3-dispatch.js
│   │   │   └── d3-dispatch.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── dispatch.js
│   │       └── index.js
│   ├── d3-drag
│   │   ├── dist
│   │   │   ├── d3-drag.js
│   │   │   └── d3-drag.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── constant.js
│   │       ├── drag.js
│   │       ├── event.js
│   │       ├── index.js
│   │       ├── nodrag.js
│   │       └── noevent.js
│   ├── d3-dsv
│   │   ├── bin
│   │   │   ├── dsv2dsv.js
│   │   │   ├── dsv2json.js
│   │   │   └── json2dsv.js
│   │   ├── dist
│   │   │   ├── d3-dsv.js
│   │   │   └── d3-dsv.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── autoType.js
│   │       ├── csv.js
│   │       ├── dsv.js
│   │       ├── index.js
│   │       └── tsv.js
│   ├── d3-ease
│   │   ├── dist
│   │   │   ├── d3-ease.js
│   │   │   └── d3-ease.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── back.js
│   │       ├── bounce.js
│   │       ├── circle.js
│   │       ├── cubic.js
│   │       ├── elastic.js
│   │       ├── exp.js
│   │       ├── index.js
│   │       ├── linear.js
│   │       ├── math.js
│   │       ├── poly.js
│   │       ├── quad.js
│   │       └── sin.js
│   ├── d3-fetch
│   │   ├── dist
│   │   │   ├── d3-fetch.js
│   │   │   └── d3-fetch.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── blob.js
│   │       ├── buffer.js
│   │       ├── dsv.js
│   │       ├── image.js
│   │       ├── index.js
│   │       ├── json.js
│   │       ├── text.js
│   │       └── xml.js
│   ├── d3-force
│   │   ├── dist
│   │   │   ├── d3-force.js
│   │   │   └── d3-force.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── center.js
│   │       ├── collide.js
│   │       ├── constant.js
│   │       ├── index.js
│   │       ├── jiggle.js
│   │       ├── lcg.js
│   │       ├── link.js
│   │       ├── manyBody.js
│   │       ├── radial.js
│   │       ├── simulation.js
│   │       ├── x.js
│   │       └── y.js
│   ├── d3-format
│   │   ├── dist
│   │   │   ├── d3-format.js
│   │   │   └── d3-format.min.js
│   │   ├── LICENSE
│   │   ├── locale
│   │   │   ├── ar-001.json
│   │   │   ├── ar-AE.json
│   │   │   ├── ar-BH.json
│   │   │   ├── ar-DJ.json
│   │   │   ├── ar-DZ.json
│   │   │   ├── ar-EG.json
│   │   │   ├── ar-EH.json
│   │   │   ├── ar-ER.json
│   │   │   ├── ar-IL.json
│   │   │   ├── ar-IQ.json
│   │   │   ├── ar-JO.json
│   │   │   ├── ar-KM.json
│   │   │   ├── ar-KW.json
│   │   │   ├── ar-LB.json
│   │   │   ├── ar-LY.json
│   │   │   ├── ar-MA.json
│   │   │   ├── ar-MR.json
│   │   │   ├── ar-OM.json
│   │   │   ├── ar-PS.json
│   │   │   ├── ar-QA.json
│   │   │   ├── ar-SA.json
│   │   │   ├── ar-SD.json
│   │   │   ├── ar-SO.json
│   │   │   ├── ar-SS.json
│   │   │   ├── ar-SY.json
│   │   │   ├── ar-TD.json
│   │   │   ├── ar-TN.json
│   │   │   ├── ar-YE.json
│   │   │   ├── ca-ES.json
│   │   │   ├── cs-CZ.json
│   │   │   ├── da-DK.json
│   │   │   ├── de-CH.json
│   │   │   ├── de-DE.json
│   │   │   ├── en-CA.json
│   │   │   ├── en-GB.json
│   │   │   ├── en-IE.json
│   │   │   ├── en-IN.json
│   │   │   ├── en-US.json
│   │   │   ├── es-BO.json
│   │   │   ├── es-ES.json
│   │   │   ├── es-MX.json
│   │   │   ├── fi-FI.json
│   │   │   ├── fr-CA.json
│   │   │   ├── fr-FR.json
│   │   │   ├── he-IL.json
│   │   │   ├── hu-HU.json
│   │   │   ├── it-IT.json
│   │   │   ├── ja-JP.json
│   │   │   ├── ko-KR.json
│   │   │   ├── mk-MK.json
│   │   │   ├── nl-NL.json
│   │   │   ├── pl-PL.json
│   │   │   ├── pt-BR.json
│   │   │   ├── pt-PT.json
│   │   │   ├── ru-RU.json
│   │   │   ├── sl-SI.json
│   │   │   ├── sv-SE.json
│   │   │   ├── uk-UA.json
│   │   │   └── zh-CN.json
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── defaultLocale.js
│   │       ├── exponent.js
│   │       ├── formatDecimal.js
│   │       ├── formatGroup.js
│   │       ├── formatNumerals.js
│   │       ├── formatPrefixAuto.js
│   │       ├── formatRounded.js
│   │       ├── formatSpecifier.js
│   │       ├── formatTrim.js
│   │       ├── formatTypes.js
│   │       ├── identity.js
│   │       ├── index.js
│   │       ├── locale.js
│   │       ├── precisionFixed.js
│   │       ├── precisionPrefix.js
│   │       └── precisionRound.js
│   ├── d3-geo
│   │   ├── dist
│   │   │   ├── d3-geo.js
│   │   │   └── d3-geo.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── area.js
│   │       ├── bounds.js
│   │       ├── cartesian.js
│   │       ├── centroid.js
│   │       ├── circle.js
│   │       ├── clip
│   │       │   ├── antimeridian.js
│   │       │   ├── buffer.js
│   │       │   ├── circle.js
│   │       │   ├── extent.js
│   │       │   ├── index.js
│   │       │   ├── line.js
│   │       │   ├── rectangle.js
│   │       │   └── rejoin.js
│   │       ├── compose.js
│   │       ├── constant.js
│   │       ├── contains.js
│   │       ├── distance.js
│   │       ├── graticule.js
│   │       ├── identity.js
│   │       ├── index.js
│   │       ├── interpolate.js
│   │       ├── length.js
│   │       ├── math.js
│   │       ├── noop.js
│   │       ├── path
│   │       │   ├── area.js
│   │       │   ├── bounds.js
│   │       │   ├── centroid.js
│   │       │   ├── context.js
│   │       │   ├── index.js
│   │       │   ├── measure.js
│   │       │   └── string.js
│   │       ├── pointEqual.js
│   │       ├── polygonContains.js
│   │       ├── projection
│   │       │   ├── albers.js
│   │       │   ├── albersUsa.js
│   │       │   ├── azimuthal.js
│   │       │   ├── azimuthalEqualArea.js
│   │       │   ├── azimuthalEquidistant.js
│   │       │   ├── conic.js
│   │       │   ├── conicConformal.js
│   │       │   ├── conicEqualArea.js
│   │       │   ├── conicEquidistant.js
│   │       │   ├── cylindricalEqualArea.js
│   │       │   ├── equalEarth.js
│   │       │   ├── equirectangular.js
│   │       │   ├── fit.js
│   │       │   ├── gnomonic.js
│   │       │   ├── identity.js
│   │       │   ├── index.js
│   │       │   ├── mercator.js
│   │       │   ├── naturalEarth1.js
│   │       │   ├── orthographic.js
│   │       │   ├── resample.js
│   │       │   ├── stereographic.js
│   │       │   └── transverseMercator.js
│   │       ├── rotation.js
│   │       ├── stream.js
│   │       └── transform.js
│   ├── d3-hierarchy
│   │   ├── dist
│   │   │   ├── d3-hierarchy.js
│   │   │   └── d3-hierarchy.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── accessors.js
│   │       ├── array.js
│   │       ├── cluster.js
│   │       ├── constant.js
│   │       ├── hierarchy
│   │       │   ├── ancestors.js
│   │       │   ├── count.js
│   │       │   ├── descendants.js
│   │       │   ├── each.js
│   │       │   ├── eachAfter.js
│   │       │   ├── eachBefore.js
│   │       │   ├── find.js
│   │       │   ├── index.js
│   │       │   ├── iterator.js
│   │       │   ├── leaves.js
│   │       │   ├── links.js
│   │       │   ├── path.js
│   │       │   ├── sort.js
│   │       │   └── sum.js
│   │       ├── index.js
│   │       ├── lcg.js
│   │       ├── pack
│   │       │   ├── enclose.js
│   │       │   ├── index.js
│   │       │   └── siblings.js
│   │       ├── partition.js
│   │       ├── stratify.js
│   │       ├── tree.js
│   │       └── treemap
│   │           ├── binary.js
│   │           ├── dice.js
│   │           ├── index.js
│   │           ├── resquarify.js
│   │           ├── round.js
│   │           ├── slice.js
│   │           ├── sliceDice.js
│   │           └── squarify.js
│   ├── d3-interpolate
│   │   ├── dist
│   │   │   ├── d3-interpolate.js
│   │   │   └── d3-interpolate.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── array.js
│   │       ├── basis.js
│   │       ├── basisClosed.js
│   │       ├── color.js
│   │       ├── constant.js
│   │       ├── cubehelix.js
│   │       ├── date.js
│   │       ├── discrete.js
│   │       ├── hcl.js
│   │       ├── hsl.js
│   │       ├── hue.js
│   │       ├── index.js
│   │       ├── lab.js
│   │       ├── number.js
│   │       ├── numberArray.js
│   │       ├── object.js
│   │       ├── piecewise.js
│   │       ├── quantize.js
│   │       ├── rgb.js
│   │       ├── round.js
│   │       ├── string.js
│   │       ├── transform
│   │       │   ├── decompose.js
│   │       │   ├── index.js
│   │       │   └── parse.js
│   │       ├── value.js
│   │       └── zoom.js
│   ├── d3-path
│   │   ├── dist
│   │   │   ├── d3-path.js
│   │   │   └── d3-path.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── index.js
│   │       └── path.js
│   ├── d3-polygon
│   │   ├── dist
│   │   │   ├── d3-polygon.js
│   │   │   └── d3-polygon.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── area.js
│   │       ├── centroid.js
│   │       ├── contains.js
│   │       ├── cross.js
│   │       ├── hull.js
│   │       ├── index.js
│   │       └── length.js
│   ├── d3-quadtree
│   │   ├── dist
│   │   │   ├── d3-quadtree.js
│   │   │   └── d3-quadtree.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── add.js
│   │       ├── cover.js
│   │       ├── data.js
│   │       ├── extent.js
│   │       ├── find.js
│   │       ├── index.js
│   │       ├── quad.js
│   │       ├── quadtree.js
│   │       ├── remove.js
│   │       ├── root.js
│   │       ├── size.js
│   │       ├── visit.js
│   │       ├── visitAfter.js
│   │       ├── x.js
│   │       └── y.js
│   ├── d3-random
│   │   ├── dist
│   │   │   ├── d3-random.js
│   │   │   └── d3-random.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── bates.js
│   │       ├── bernoulli.js
│   │       ├── beta.js
│   │       ├── binomial.js
│   │       ├── cauchy.js
│   │       ├── defaultSource.js
│   │       ├── exponential.js
│   │       ├── gamma.js
│   │       ├── geometric.js
│   │       ├── index.js
│   │       ├── int.js
│   │       ├── irwinHall.js
│   │       ├── lcg.js
│   │       ├── logistic.js
│   │       ├── logNormal.js
│   │       ├── normal.js
│   │       ├── pareto.js
│   │       ├── poisson.js
│   │       ├── uniform.js
│   │       └── weibull.js
│   ├── d3-sankey
│   │   ├── dist
│   │   │   ├── d3-sankey.js
│   │   │   └── d3-sankey.min.js
│   │   ├── LICENSE
│   │   ├── node_modules
│   │   │   ├── d3-array
│   │   │   │   ├── dist
│   │   │   │   │   ├── d3-array.js
│   │   │   │   │   └── d3-array.min.js
│   │   │   │   ├── LICENSE
│   │   │   │   ├── package.json
│   │   │   │   ├── README.md
│   │   │   │   └── src
│   │   │   │       ├── array.js
│   │   │   │       ├── ascending.js
│   │   │   │       ├── bin.js
│   │   │   │       ├── bisect.js
│   │   │   │       ├── bisector.js
│   │   │   │       ├── constant.js
│   │   │   │       ├── count.js
│   │   │   │       ├── cross.js
│   │   │   │       ├── cumsum.js
│   │   │   │       ├── descending.js
│   │   │   │       ├── deviation.js
│   │   │   │       ├── difference.js
│   │   │   │       ├── disjoint.js
│   │   │   │       ├── every.js
│   │   │   │       ├── extent.js
│   │   │   │       ├── filter.js
│   │   │   │       ├── fsum.js
│   │   │   │       ├── greatest.js
│   │   │   │       ├── greatestIndex.js
│   │   │   │       ├── group.js
│   │   │   │       ├── groupSort.js
│   │   │   │       ├── identity.js
│   │   │   │       ├── index.js
│   │   │   │       ├── intersection.js
│   │   │   │       ├── least.js
│   │   │   │       ├── leastIndex.js
│   │   │   │       ├── map.js
│   │   │   │       ├── max.js
│   │   │   │       ├── maxIndex.js
│   │   │   │       ├── mean.js
│   │   │   │       ├── median.js
│   │   │   │       ├── merge.js
│   │   │   │       ├── min.js
│   │   │   │       ├── minIndex.js
│   │   │   │       ├── nice.js
│   │   │   │       ├── number.js
│   │   │   │       ├── pairs.js
│   │   │   │       ├── permute.js
│   │   │   │       ├── quantile.js
│   │   │   │       ├── quickselect.js
│   │   │   │       ├── range.js
│   │   │   │       ├── reduce.js
│   │   │   │       ├── reverse.js
│   │   │   │       ├── scan.js
│   │   │   │       ├── set.js
│   │   │   │       ├── shuffle.js
│   │   │   │       ├── some.js
│   │   │   │       ├── sort.js
│   │   │   │       ├── subset.js
│   │   │   │       ├── sum.js
│   │   │   │       ├── superset.js
│   │   │   │       ├── threshold
│   │   │   │       │   ├── freedmanDiaconis.js
│   │   │   │       │   ├── scott.js
│   │   │   │       │   └── sturges.js
│   │   │   │       ├── ticks.js
│   │   │   │       ├── transpose.js
│   │   │   │       ├── union.js
│   │   │   │       ├── variance.js
│   │   │   │       └── zip.js
│   │   │   ├── d3-path
│   │   │   │   ├── dist
│   │   │   │   │   ├── d3-path.js
│   │   │   │   │   └── d3-path.min.js
│   │   │   │   ├── LICENSE
│   │   │   │   ├── package.json
│   │   │   │   ├── README.md
│   │   │   │   └── src
│   │   │   │       ├── index.js
│   │   │   │       └── path.js
│   │   │   ├── d3-shape
│   │   │   │   ├── dist
│   │   │   │   │   ├── d3-shape.js
│   │   │   │   │   └── d3-shape.min.js
│   │   │   │   ├── LICENSE
│   │   │   │   ├── package.json
│   │   │   │   ├── README.md
│   │   │   │   └── src
│   │   │   │       ├── arc.js
│   │   │   │       ├── area.js
│   │   │   │       ├── areaRadial.js
│   │   │   │       ├── array.js
│   │   │   │       ├── constant.js
│   │   │   │       ├── curve
│   │   │   │       │   ├── basis.js
│   │   │   │       │   ├── basisClosed.js
│   │   │   │       │   ├── basisOpen.js
│   │   │   │       │   ├── bundle.js
│   │   │   │       │   ├── cardinal.js
│   │   │   │       │   ├── cardinalClosed.js
│   │   │   │       │   ├── cardinalOpen.js
│   │   │   │       │   ├── catmullRom.js
│   │   │   │       │   ├── catmullRomClosed.js
│   │   │   │       │   ├── catmullRomOpen.js
│   │   │   │       │   ├── linear.js
│   │   │   │       │   ├── linearClosed.js
│   │   │   │       │   ├── monotone.js
│   │   │   │       │   ├── natural.js
│   │   │   │       │   ├── radial.js
│   │   │   │       │   └── step.js
│   │   │   │       ├── descending.js
│   │   │   │       ├── identity.js
│   │   │   │       ├── index.js
│   │   │   │       ├── line.js
│   │   │   │       ├── lineRadial.js
│   │   │   │       ├── link
│   │   │   │       │   └── index.js
│   │   │   │       ├── math.js
│   │   │   │       ├── noop.js
│   │   │   │       ├── offset
│   │   │   │       │   ├── diverging.js
│   │   │   │       │   ├── expand.js
│   │   │   │       │   ├── none.js
│   │   │   │       │   ├── silhouette.js
│   │   │   │       │   └── wiggle.js
│   │   │   │       ├── order
│   │   │   │       │   ├── appearance.js
│   │   │   │       │   ├── ascending.js
│   │   │   │       │   ├── descending.js
│   │   │   │       │   ├── insideOut.js
│   │   │   │       │   ├── none.js
│   │   │   │       │   └── reverse.js
│   │   │   │       ├── pie.js
│   │   │   │       ├── point.js
│   │   │   │       ├── pointRadial.js
│   │   │   │       ├── stack.js
│   │   │   │       ├── symbol
│   │   │   │       │   ├── circle.js
│   │   │   │       │   ├── cross.js
│   │   │   │       │   ├── diamond.js
│   │   │   │       │   ├── square.js
│   │   │   │       │   ├── star.js
│   │   │   │       │   ├── triangle.js
│   │   │   │       │   └── wye.js
│   │   │   │       └── symbol.js
│   │   │   └── internmap
│   │   │       ├── dist
│   │   │       │   ├── internmap.js
│   │   │       │   └── internmap.min.js
│   │   │       ├── LICENSE
│   │   │       ├── package.json
│   │   │       ├── README.md
│   │   │       └── src
│   │   │           └── index.js
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── align.js
│   │       ├── constant.js
│   │       ├── index.js
│   │       ├── sankey.js
│   │       └── sankeyLinkHorizontal.js
│   ├── d3-scale
│   │   ├── dist
│   │   │   ├── d3-scale.js
│   │   │   └── d3-scale.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── band.js
│   │       ├── colors.js
│   │       ├── constant.js
│   │       ├── continuous.js
│   │       ├── diverging.js
│   │       ├── identity.js
│   │       ├── index.js
│   │       ├── init.js
│   │       ├── linear.js
│   │       ├── log.js
│   │       ├── nice.js
│   │       ├── number.js
│   │       ├── ordinal.js
│   │       ├── pow.js
│   │       ├── quantile.js
│   │       ├── quantize.js
│   │       ├── radial.js
│   │       ├── sequential.js
│   │       ├── sequentialQuantile.js
│   │       ├── symlog.js
│   │       ├── threshold.js
│   │       ├── tickFormat.js
│   │       ├── time.js
│   │       └── utcTime.js
│   ├── d3-scale-chromatic
│   │   ├── dist
│   │   │   ├── d3-scale-chromatic.js
│   │   │   └── d3-scale-chromatic.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── categorical
│   │       │   ├── Accent.js
│   │       │   ├── category10.js
│   │       │   ├── Dark2.js
│   │       │   ├── observable10.js
│   │       │   ├── Paired.js
│   │       │   ├── Pastel1.js
│   │       │   ├── Pastel2.js
│   │       │   ├── Set1.js
│   │       │   ├── Set2.js
│   │       │   ├── Set3.js
│   │       │   └── Tableau10.js
│   │       ├── colors.js
│   │       ├── diverging
│   │       │   ├── BrBG.js
│   │       │   ├── PiYG.js
│   │       │   ├── PRGn.js
│   │       │   ├── PuOr.js
│   │       │   ├── RdBu.js
│   │       │   ├── RdGy.js
│   │       │   ├── RdYlBu.js
│   │       │   ├── RdYlGn.js
│   │       │   └── Spectral.js
│   │       ├── index.js
│   │       ├── ramp.js
│   │       ├── rampClosed.js
│   │       ├── sequential-multi
│   │       │   ├── BuGn.js
│   │       │   ├── BuPu.js
│   │       │   ├── cividis.js
│   │       │   ├── cubehelix.js
│   │       │   ├── GnBu.js
│   │       │   ├── OrRd.js
│   │       │   ├── PuBu.js
│   │       │   ├── PuBuGn.js
│   │       │   ├── PuRd.js
│   │       │   ├── rainbow.js
│   │       │   ├── RdPu.js
│   │       │   ├── sinebow.js
│   │       │   ├── turbo.js
│   │       │   ├── viridis.js
│   │       │   ├── YlGn.js
│   │       │   ├── YlGnBu.js
│   │       │   ├── YlOrBr.js
│   │       │   └── YlOrRd.js
│   │       └── sequential-single
│   │           ├── Blues.js
│   │           ├── Greens.js
│   │           ├── Greys.js
│   │           ├── Oranges.js
│   │           ├── Purples.js
│   │           └── Reds.js
│   ├── d3-selection
│   │   ├── dist
│   │   │   ├── d3-selection.js
│   │   │   └── d3-selection.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── array.js
│   │       ├── constant.js
│   │       ├── create.js
│   │       ├── creator.js
│   │       ├── identity.js
│   │       ├── index.js
│   │       ├── local.js
│   │       ├── matcher.js
│   │       ├── namespace.js
│   │       ├── namespaces.js
│   │       ├── pointer.js
│   │       ├── pointers.js
│   │       ├── select.js
│   │       ├── selectAll.js
│   │       ├── selection
│   │       │   ├── append.js
│   │       │   ├── attr.js
│   │       │   ├── call.js
│   │       │   ├── classed.js
│   │       │   ├── clone.js
│   │       │   ├── data.js
│   │       │   ├── datum.js
│   │       │   ├── dispatch.js
│   │       │   ├── each.js
│   │       │   ├── empty.js
│   │       │   ├── enter.js
│   │       │   ├── exit.js
│   │       │   ├── filter.js
│   │       │   ├── html.js
│   │       │   ├── index.js
│   │       │   ├── insert.js
│   │       │   ├── iterator.js
│   │       │   ├── join.js
│   │       │   ├── lower.js
│   │       │   ├── merge.js
│   │       │   ├── node.js
│   │       │   ├── nodes.js
│   │       │   ├── on.js
│   │       │   ├── order.js
│   │       │   ├── property.js
│   │       │   ├── raise.js
│   │       │   ├── remove.js
│   │       │   ├── select.js
│   │       │   ├── selectAll.js
│   │       │   ├── selectChild.js
│   │       │   ├── selectChildren.js
│   │       │   ├── size.js
│   │       │   ├── sort.js
│   │       │   ├── sparse.js
│   │       │   ├── style.js
│   │       │   └── text.js
│   │       ├── selector.js
│   │       ├── selectorAll.js
│   │       ├── sourceEvent.js
│   │       └── window.js
│   ├── d3-shape
│   │   ├── dist
│   │   │   ├── d3-shape.js
│   │   │   └── d3-shape.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── arc.js
│   │       ├── area.js
│   │       ├── areaRadial.js
│   │       ├── array.js
│   │       ├── constant.js
│   │       ├── curve
│   │       │   ├── basis.js
│   │       │   ├── basisClosed.js
│   │       │   ├── basisOpen.js
│   │       │   ├── bump.js
│   │       │   ├── bundle.js
│   │       │   ├── cardinal.js
│   │       │   ├── cardinalClosed.js
│   │       │   ├── cardinalOpen.js
│   │       │   ├── catmullRom.js
│   │       │   ├── catmullRomClosed.js
│   │       │   ├── catmullRomOpen.js
│   │       │   ├── linear.js
│   │       │   ├── linearClosed.js
│   │       │   ├── monotone.js
│   │       │   ├── natural.js
│   │       │   ├── radial.js
│   │       │   └── step.js
│   │       ├── descending.js
│   │       ├── identity.js
│   │       ├── index.js
│   │       ├── line.js
│   │       ├── lineRadial.js
│   │       ├── link.js
│   │       ├── math.js
│   │       ├── noop.js
│   │       ├── offset
│   │       │   ├── diverging.js
│   │       │   ├── expand.js
│   │       │   ├── none.js
│   │       │   ├── silhouette.js
│   │       │   └── wiggle.js
│   │       ├── order
│   │       │   ├── appearance.js
│   │       │   ├── ascending.js
│   │       │   ├── descending.js
│   │       │   ├── insideOut.js
│   │       │   ├── none.js
│   │       │   └── reverse.js
│   │       ├── path.js
│   │       ├── pie.js
│   │       ├── point.js
│   │       ├── pointRadial.js
│   │       ├── stack.js
│   │       ├── symbol
│   │       │   ├── asterisk.js
│   │       │   ├── circle.js
│   │       │   ├── cross.js
│   │       │   ├── diamond.js
│   │       │   ├── diamond2.js
│   │       │   ├── plus.js
│   │       │   ├── square.js
│   │       │   ├── square2.js
│   │       │   ├── star.js
│   │       │   ├── times.js
│   │       │   ├── triangle.js
│   │       │   ├── triangle2.js
│   │       │   └── wye.js
│   │       └── symbol.js
│   ├── d3-time
│   │   ├── dist
│   │   │   ├── d3-time.js
│   │   │   └── d3-time.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── day.js
│   │       ├── duration.js
│   │       ├── hour.js
│   │       ├── index.js
│   │       ├── interval.js
│   │       ├── millisecond.js
│   │       ├── minute.js
│   │       ├── month.js
│   │       ├── second.js
│   │       ├── ticks.js
│   │       ├── week.js
│   │       └── year.js
│   ├── d3-time-format
│   │   ├── dist
│   │   │   ├── d3-time-format.js
│   │   │   └── d3-time-format.min.js
│   │   ├── LICENSE
│   │   ├── locale
│   │   │   ├── ar-EG.json
│   │   │   ├── ar-SY.json
│   │   │   ├── ca-ES.json
│   │   │   ├── cs-CZ.json
│   │   │   ├── da-DK.json
│   │   │   ├── de-CH.json
│   │   │   ├── de-DE.json
│   │   │   ├── en-CA.json
│   │   │   ├── en-GB.json
│   │   │   ├── en-US.json
│   │   │   ├── es-ES.json
│   │   │   ├── es-MX.json
│   │   │   ├── fa-IR.json
│   │   │   ├── fi-FI.json
│   │   │   ├── fr-CA.json
│   │   │   ├── fr-FR.json
│   │   │   ├── he-IL.json
│   │   │   ├── hr-HR.json
│   │   │   ├── hu-HU.json
│   │   │   ├── it-IT.json
│   │   │   ├── ja-JP.json
│   │   │   ├── ko-KR.json
│   │   │   ├── mk-MK.json
│   │   │   ├── nb-NO.json
│   │   │   ├── nl-BE.json
│   │   │   ├── nl-NL.json
│   │   │   ├── pl-PL.json
│   │   │   ├── pt-BR.json
│   │   │   ├── ru-RU.json
│   │   │   ├── sv-SE.json
│   │   │   ├── tr-TR.json
│   │   │   ├── uk-UA.json
│   │   │   ├── zh-CN.json
│   │   │   └── zh-TW.json
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── defaultLocale.js
│   │       ├── index.js
│   │       ├── isoFormat.js
│   │       ├── isoParse.js
│   │       └── locale.js
│   ├── d3-timer
│   │   ├── dist
│   │   │   ├── d3-timer.js
│   │   │   └── d3-timer.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── index.js
│   │       ├── interval.js
│   │       ├── timeout.js
│   │       └── timer.js
│   ├── d3-transition
│   │   ├── dist
│   │   │   ├── d3-transition.js
│   │   │   └── d3-transition.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── active.js
│   │       ├── index.js
│   │       ├── interrupt.js
│   │       ├── selection
│   │       │   ├── index.js
│   │       │   ├── interrupt.js
│   │       │   └── transition.js
│   │       └── transition
│   │           ├── attr.js
│   │           ├── attrTween.js
│   │           ├── delay.js
│   │           ├── duration.js
│   │           ├── ease.js
│   │           ├── easeVarying.js
│   │           ├── end.js
│   │           ├── filter.js
│   │           ├── index.js
│   │           ├── interpolate.js
│   │           ├── merge.js
│   │           ├── on.js
│   │           ├── remove.js
│   │           ├── schedule.js
│   │           ├── select.js
│   │           ├── selectAll.js
│   │           ├── selection.js
│   │           ├── style.js
│   │           ├── styleTween.js
│   │           ├── text.js
│   │           ├── textTween.js
│   │           ├── transition.js
│   │           └── tween.js
│   ├── d3-zoom
│   │   ├── dist
│   │   │   ├── d3-zoom.js
│   │   │   └── d3-zoom.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       ├── constant.js
│   │       ├── event.js
│   │       ├── index.js
│   │       ├── noevent.js
│   │       ├── transform.js
│   │       └── zoom.js
│   ├── delaunator
│   │   ├── delaunator.js
│   │   ├── delaunator.min.js
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── esbuild
│   │   ├── bin
│   │   │   └── esbuild
│   │   ├── install.js
│   │   ├── lib
│   │   │   ├── main.d.ts
│   │   │   └── main.js
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   └── README.md
│   ├── fsevents
│   │   ├── fsevents.d.ts
│   │   ├── fsevents.js
│   │   ├── fsevents.node
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── iconv-lite
│   │   ├── Changelog.md
│   │   ├── encodings
│   │   │   ├── dbcs-codec.js
│   │   │   ├── dbcs-data.js
│   │   │   ├── index.js
│   │   │   ├── internal.js
│   │   │   ├── sbcs-codec.js
│   │   │   ├── sbcs-data-generated.js
│   │   │   ├── sbcs-data.js
│   │   │   ├── tables
│   │   │   │   ├── big5-added.json
│   │   │   │   ├── cp936.json
│   │   │   │   ├── cp949.json
│   │   │   │   ├── cp950.json
│   │   │   │   ├── eucjp.json
│   │   │   │   ├── gb18030-ranges.json
│   │   │   │   ├── gbk-added.json
│   │   │   │   └── shiftjis.json
│   │   │   ├── utf16.js
│   │   │   ├── utf32.js
│   │   │   └── utf7.js
│   │   ├── lib
│   │   │   ├── bom-handling.js
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   └── streams.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── internmap
│   │   ├── dist
│   │   │   ├── internmap.js
│   │   │   └── internmap.min.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── src
│   │       └── index.js
│   ├── nanoid
│   │   ├── async
│   │   │   ├── index.browser.cjs
│   │   │   ├── index.browser.js
│   │   │   ├── index.cjs
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── index.native.js
│   │   │   └── package.json
│   │   ├── bin
│   │   │   └── nanoid.cjs
│   │   ├── index.browser.cjs
│   │   ├── index.browser.js
│   │   ├── index.cjs
│   │   ├── index.d.cts
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── nanoid.js
│   │   ├── non-secure
│   │   │   ├── index.cjs
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   └── package.json
│   │   ├── package.json
│   │   ├── README.md
│   │   └── url-alphabet
│   │       ├── index.cjs
│   │       ├── index.js
│   │       └── package.json
│   ├── picocolors
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── picocolors.browser.js
│   │   ├── picocolors.d.ts
│   │   ├── picocolors.js
│   │   ├── README.md
│   │   └── types.d.ts
│   ├── postcss
│   │   ├── lib
│   │   │   ├── at-rule.d.ts
│   │   │   ├── at-rule.js
│   │   │   ├── comment.d.ts
│   │   │   ├── comment.js
│   │   │   ├── container.d.ts
│   │   │   ├── container.js
│   │   │   ├── css-syntax-error.d.ts
│   │   │   ├── css-syntax-error.js
│   │   │   ├── declaration.d.ts
│   │   │   ├── declaration.js
│   │   │   ├── document.d.ts
│   │   │   ├── document.js
│   │   │   ├── fromJSON.d.ts
│   │   │   ├── fromJSON.js
│   │   │   ├── input.d.ts
│   │   │   ├── input.js
│   │   │   ├── lazy-result.d.ts
│   │   │   ├── lazy-result.js
│   │   │   ├── list.d.ts
│   │   │   ├── list.js
│   │   │   ├── map-generator.js
│   │   │   ├── no-work-result.d.ts
│   │   │   ├── no-work-result.js
│   │   │   ├── node.d.ts
│   │   │   ├── node.js
│   │   │   ├── parse.d.ts
│   │   │   ├── parse.js
│   │   │   ├── parser.js
│   │   │   ├── postcss.d.mts
│   │   │   ├── postcss.d.ts
│   │   │   ├── postcss.js
│   │   │   ├── postcss.mjs
│   │   │   ├── previous-map.d.ts
│   │   │   ├── previous-map.js
│   │   │   ├── processor.d.ts
│   │   │   ├── processor.js
│   │   │   ├── result.d.ts
│   │   │   ├── result.js
│   │   │   ├── root.d.ts
│   │   │   ├── root.js
│   │   │   ├── rule.d.ts
│   │   │   ├── rule.js
│   │   │   ├── stringifier.d.ts
│   │   │   ├── stringifier.js
│   │   │   ├── stringify.d.ts
│   │   │   ├── stringify.js
│   │   │   ├── symbols.js
│   │   │   ├── terminal-highlight.js
│   │   │   ├── tokenize.js
│   │   │   ├── warn-once.js
│   │   │   ├── warning.d.ts
│   │   │   └── warning.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   ├── robust-predicates
│   │   ├── esm
│   │   │   ├── incircle.js
│   │   │   ├── insphere.js
│   │   │   ├── orient2d.js
│   │   │   ├── orient3d.js
│   │   │   └── util.js
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── umd
│   │       ├── incircle.js
│   │       ├── incircle.min.js
│   │       ├── insphere.js
│   │       ├── insphere.min.js
│   │       ├── orient2d.js
│   │       ├── orient2d.min.js
│   │       ├── orient3d.js
│   │       ├── orient3d.min.js
│   │       ├── predicates.js
│   │       └── predicates.min.js
│   ├── rollup
│   │   ├── dist
│   │   │   ├── bin
│   │   │   │   └── rollup
│   │   │   ├── es
│   │   │   │   ├── getLogFilter.js
│   │   │   │   ├── package.json
│   │   │   │   ├── rollup.js
│   │   │   │   └── shared
│   │   │   │       ├── node-entry.js
│   │   │   │       └── watch.js
│   │   │   ├── getLogFilter.d.ts
│   │   │   ├── getLogFilter.js
│   │   │   ├── loadConfigFile.d.ts
│   │   │   ├── loadConfigFile.js
│   │   │   ├── rollup.d.ts
│   │   │   ├── rollup.js
│   │   │   └── shared
│   │   │       ├── fsevents-importer.js
│   │   │       ├── index.js
│   │   │       ├── loadConfigFile.js
│   │   │       ├── rollup.js
│   │   │       ├── watch-cli.js
│   │   │       ├── watch-proxy.js
│   │   │       └── watch.js
│   │   ├── LICENSE.md
│   │   ├── package.json
│   │   └── README.md
│   ├── rw
│   │   ├── index.js
│   │   ├── lib
│   │   │   └── rw
│   │   │       ├── dash.js
│   │   │       ├── decode.js
│   │   │       ├── encode.js
│   │   │       ├── read-file-sync.js
│   │   │       ├── read-file.js
│   │   │       ├── write-file-sync.js
│   │   │       └── write-file.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   └── test
│   │       ├── cat-async
│   │       ├── cat-sync
│   │       ├── encode-object-async
│   │       ├── encode-object-sync
│   │       ├── encode-string-async
│   │       ├── encode-string-sync
│   │       ├── encoding-async
│   │       ├── encoding-sync
│   │       ├── run-tests
│   │       ├── utf8.txt
│   │       ├── wc-async
│   │       ├── wc-sync
│   │       ├── write-async
│   │       └── write-sync
│   ├── safer-buffer
│   │   ├── dangerous.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── Porting-Buffer.md
│   │   ├── Readme.md
│   │   ├── safer.js
│   │   └── tests.js
│   ├── source-map-js
│   │   ├── lib
│   │   │   ├── array-set.js
│   │   │   ├── base64-vlq.js
│   │   │   ├── base64.js
│   │   │   ├── binary-search.js
│   │   │   ├── mapping-list.js
│   │   │   ├── quick-sort.js
│   │   │   ├── source-map-consumer.d.ts
│   │   │   ├── source-map-consumer.js
│   │   │   ├── source-map-generator.d.ts
│   │   │   ├── source-map-generator.js
│   │   │   ├── source-node.d.ts
│   │   │   ├── source-node.js
│   │   │   └── util.js
│   │   ├── LICENSE
│   │   ├── package.json
│   │   ├── README.md
│   │   ├── source-map.d.ts
│   │   └── source-map.js
│   ├── svelte
│   │   ├── action
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── index.mjs
│   │   │   └── package.json
│   │   ├── animate
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── index.mjs
│   │   │   └── package.json
│   │   ├── CHANGELOG.md
│   │   ├── compiler.d.ts
│   │   ├── compiler.js
│   │   ├── compiler.js.map
│   │   ├── compiler.mjs
│   │   ├── compiler.mjs.map
│   │   ├── easing
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── index.mjs
│   │   │   └── package.json
│   │   ├── elements
│   │   │   ├── index.d.ts
│   │   │   └── package.json
│   │   ├── index.js
│   │   ├── index.mjs
│   │   ├── internal
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── index.mjs
│   │   │   └── package.json
│   │   ├── LICENSE.md
│   │   ├── motion
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── index.mjs
│   │   │   └── package.json
│   │   ├── package.json
│   │   ├── README.md
│   │   ├── register.js
│   │   ├── ssr.js
│   │   ├── ssr.mjs
│   │   ├── store
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── index.mjs
│   │   │   └── package.json
│   │   ├── transition
│   │   │   ├── index.d.ts
│   │   │   ├── index.js
│   │   │   ├── index.mjs
│   │   │   └── package.json
│   │   └── types
│   │       ├── compiler
│   │       │   ├── compile
│   │       │   │   ├── compiler_errors.d.ts
│   │       │   │   ├── compiler_warnings.d.ts
│   │       │   │   ├── Component.d.ts
│   │       │   │   ├── create_module.d.ts
│   │       │   │   ├── css
│   │       │   │   │   ├── gather_possible_values.d.ts
│   │       │   │   │   ├── interfaces.d.ts
│   │       │   │   │   ├── Selector.d.ts
│   │       │   │   │   └── Stylesheet.d.ts
│   │       │   │   ├── index.d.ts
│   │       │   │   ├── internal_exports.d.ts
│   │       │   │   ├── nodes
│   │       │   │   │   ├── Action.d.ts
│   │       │   │   │   ├── Animation.d.ts
│   │       │   │   │   ├── Attribute.d.ts
│   │       │   │   │   ├── AwaitBlock.d.ts
│   │       │   │   │   ├── Binding.d.ts
│   │       │   │   │   ├── Body.d.ts
│   │       │   │   │   ├── CatchBlock.d.ts
│   │       │   │   │   ├── Class.d.ts
│   │       │   │   │   ├── Comment.d.ts
│   │       │   │   │   ├── ConstTag.d.ts
│   │       │   │   │   ├── DebugTag.d.ts
│   │       │   │   │   ├── Document.d.ts
│   │       │   │   │   ├── EachBlock.d.ts
│   │       │   │   │   ├── Element.d.ts
│   │       │   │   │   ├── ElseBlock.d.ts
│   │       │   │   │   ├── EventHandler.d.ts
│   │       │   │   │   ├── Fragment.d.ts
│   │       │   │   │   ├── Head.d.ts
│   │       │   │   │   ├── IfBlock.d.ts
│   │       │   │   │   ├── InlineComponent.d.ts
│   │       │   │   │   ├── interfaces.d.ts
│   │       │   │   │   ├── KeyBlock.d.ts
│   │       │   │   │   ├── Let.d.ts
│   │       │   │   │   ├── MustacheTag.d.ts
│   │       │   │   │   ├── Options.d.ts
│   │       │   │   │   ├── PendingBlock.d.ts
│   │       │   │   │   ├── RawMustacheTag.d.ts
│   │       │   │   │   ├── shared
│   │       │   │   │   │   ├── AbstractBlock.d.ts
│   │       │   │   │   │   ├── Context.d.ts
│   │       │   │   │   │   ├── Expression.d.ts
│   │       │   │   │   │   ├── get_const_tags.d.ts
│   │       │   │   │   │   ├── is_contextual.d.ts
│   │       │   │   │   │   ├── map_children.d.ts
│   │       │   │   │   │   ├── Node.d.ts
│   │       │   │   │   │   ├── Tag.d.ts
│   │       │   │   │   │   └── TemplateScope.d.ts
│   │       │   │   │   ├── Slot.d.ts
│   │       │   │   │   ├── SlotTemplate.d.ts
│   │       │   │   │   ├── StyleDirective.d.ts
│   │       │   │   │   ├── Text.d.ts
│   │       │   │   │   ├── ThenBlock.d.ts
│   │       │   │   │   ├── Title.d.ts
│   │       │   │   │   ├── Transition.d.ts
│   │       │   │   │   └── Window.d.ts
│   │       │   │   ├── render_dom
│   │       │   │   │   ├── Block.d.ts
│   │       │   │   │   ├── index.d.ts
│   │       │   │   │   ├── invalidate.d.ts
│   │       │   │   │   ├── Renderer.d.ts
│   │       │   │   │   └── wrappers
│   │       │   │   │       ├── AwaitBlock.d.ts
│   │       │   │   │       ├── Body.d.ts
│   │       │   │   │       ├── Comment.d.ts
│   │       │   │   │       ├── DebugTag.d.ts
│   │       │   │   │       ├── Document.d.ts
│   │       │   │   │       ├── EachBlock.d.ts
│   │       │   │   │       ├── Element
│   │       │   │   │       │   ├── Attribute.d.ts
│   │       │   │   │       │   ├── Binding.d.ts
│   │       │   │   │       │   ├── EventHandler.d.ts
│   │       │   │   │       │   ├── fix_attribute_casing.d.ts
│   │       │   │   │       │   ├── handle_select_value_binding.d.ts
│   │       │   │   │       │   ├── index.d.ts
│   │       │   │   │       │   ├── SpreadAttribute.d.ts
│   │       │   │   │       │   └── StyleAttribute.d.ts
│   │       │   │   │       ├── Fragment.d.ts
│   │       │   │   │       ├── Head.d.ts
│   │       │   │   │       ├── IfBlock.d.ts
│   │       │   │   │       ├── InlineComponent
│   │       │   │   │       │   └── index.d.ts
│   │       │   │   │       ├── KeyBlock.d.ts
│   │       │   │   │       ├── MustacheTag.d.ts
│   │       │   │   │       ├── RawMustacheTag.d.ts
│   │       │   │   │       ├── shared
│   │       │   │   │       │   ├── add_actions.d.ts
│   │       │   │   │       │   ├── add_const_tags.d.ts
│   │       │   │   │       │   ├── add_event_handlers.d.ts
│   │       │   │   │       │   ├── bind_this.d.ts
│   │       │   │   │       │   ├── create_debugging_comment.d.ts
│   │       │   │   │       │   ├── get_slot_definition.d.ts
│   │       │   │   │       │   ├── is_dynamic.d.ts
│   │       │   │   │       │   ├── is_head.d.ts
│   │       │   │   │       │   ├── mark_each_block_bindings.d.ts
│   │       │   │   │       │   ├── Tag.d.ts
│   │       │   │   │       │   └── Wrapper.d.ts
│   │       │   │   │       ├── Slot.d.ts
│   │       │   │   │       ├── SlotTemplate.d.ts
│   │       │   │   │       ├── Text.d.ts
│   │       │   │   │       ├── Title.d.ts
│   │       │   │   │       └── Window.d.ts
│   │       │   │   ├── render_ssr
│   │       │   │   │   ├── handlers
│   │       │   │   │   │   ├── AwaitBlock.d.ts
│   │       │   │   │   │   ├── Comment.d.ts
│   │       │   │   │   │   ├── DebugTag.d.ts
│   │       │   │   │   │   ├── EachBlock.d.ts
│   │       │   │   │   │   ├── Element.d.ts
│   │       │   │   │   │   ├── Head.d.ts
│   │       │   │   │   │   ├── HtmlTag.d.ts
│   │       │   │   │   │   ├── IfBlock.d.ts
│   │       │   │   │   │   ├── InlineComponent.d.ts
│   │       │   │   │   │   ├── KeyBlock.d.ts
│   │       │   │   │   │   ├── shared
│   │       │   │   │   │   │   ├── get_attribute_value.d.ts
│   │       │   │   │   │   │   ├── get_const_tags.d.ts
│   │       │   │   │   │   │   └── get_slot_scope.d.ts
│   │       │   │   │   │   ├── Slot.d.ts
│   │       │   │   │   │   ├── SlotTemplate.d.ts
│   │       │   │   │   │   ├── Tag.d.ts
│   │       │   │   │   │   ├── Text.d.ts
│   │       │   │   │   │   ├── Title.d.ts
│   │       │   │   │   │   └── utils
│   │       │   │   │   │       └── remove_whitespace_children.d.ts
│   │       │   │   │   ├── index.d.ts
│   │       │   │   │   └── Renderer.d.ts
│   │       │   │   └── utils
│   │       │   │       ├── __test__.d.ts
│   │       │   │       ├── a11y.d.ts
│   │       │   │       ├── add_to_set.d.ts
│   │       │   │       ├── check_enable_sourcemap.d.ts
│   │       │   │       ├── check_graph_for_cycles.d.ts
│   │       │   │       ├── collapse_template_literal.d.ts
│   │       │   │       ├── compare_node.d.ts
│   │       │   │       ├── contenteditable.d.ts
│   │       │   │       ├── flatten_reference.d.ts
│   │       │   │       ├── get_name_from_filename.d.ts
│   │       │   │       ├── get_object.d.ts
│   │       │   │       ├── get_slot_data.d.ts
│   │       │   │       ├── hash.d.ts
│   │       │   │       ├── is_used_as_reference.d.ts
│   │       │   │       ├── nodes_to_template_literal.d.ts
│   │       │   │       ├── replace_object.d.ts
│   │       │   │       ├── reserved_keywords.d.ts
│   │       │   │       ├── scope.d.ts
│   │       │   │       ├── string_to_member_expression.d.ts
│   │       │   │       └── stringify.d.ts
│   │       │   ├── config.d.ts
│   │       │   ├── index.d.ts
│   │       │   ├── interfaces.d.ts
│   │       │   ├── parse
│   │       │   │   ├── acorn.d.ts
│   │       │   │   ├── errors.d.ts
│   │       │   │   ├── index.d.ts
│   │       │   │   ├── read
│   │       │   │   │   ├── context.d.ts
│   │       │   │   │   ├── css-tree-cq
│   │       │   │   │   │   ├── css_tree_parse.d.ts
│   │       │   │   │   │   └── node
│   │       │   │   │   │       ├── comparison.d.ts
│   │       │   │   │   │       ├── container_feature_style.d.ts
│   │       │   │   │   │       ├── container_query.d.ts
│   │       │   │   │   │       ├── index.d.ts
│   │       │   │   │   │       ├── lookahead_is_range.d.ts
│   │       │   │   │   │       ├── media_query.d.ts
│   │       │   │   │   │       ├── query_css_function.d.ts
│   │       │   │   │   │       ├── query_feature_range.d.ts
│   │       │   │   │   │       └── query_feature.d.ts
│   │       │   │   │   ├── expression.d.ts
│   │       │   │   │   ├── script.d.ts
│   │       │   │   │   └── style.d.ts
│   │       │   │   ├── state
│   │       │   │   │   ├── fragment.d.ts
│   │       │   │   │   ├── mustache.d.ts
│   │       │   │   │   ├── tag.d.ts
│   │       │   │   │   └── text.d.ts
│   │       │   │   └── utils
│   │       │   │       ├── bracket.d.ts
│   │       │   │       ├── entities.d.ts
│   │       │   │       ├── html.d.ts
│   │       │   │       └── node.d.ts
│   │       │   ├── preprocess
│   │       │   │   ├── decode_sourcemap.d.ts
│   │       │   │   ├── index.d.ts
│   │       │   │   ├── replace_in_code.d.ts
│   │       │   │   └── types.d.ts
│   │       │   ├── Stats.d.ts
│   │       │   └── utils
│   │       │       ├── clone.d.ts
│   │       │       ├── error.d.ts
│   │       │       ├── extract_svelte_ignore.d.ts
│   │       │       ├── flatten.d.ts
│   │       │       ├── full_char_code_at.d.ts
│   │       │       ├── fuzzymatch.d.ts
│   │       │       ├── get_code_frame.d.ts
│   │       │       ├── globals.d.ts
│   │       │       ├── link.d.ts
│   │       │       ├── list.d.ts
│   │       │       ├── mapped_code.d.ts
│   │       │       ├── names.d.ts
│   │       │       ├── namespaces.d.ts
│   │       │       ├── nodes_match.d.ts
│   │       │       ├── patterns.d.ts
│   │       │       ├── push_array.d.ts
│   │       │       └── trim.d.ts
│   │       ├── runtime
│   │       │   ├── action
│   │       │   │   └── index.d.ts
│   │       │   ├── ambient.d.ts
│   │       │   ├── animate
│   │       │   │   └── index.d.ts
│   │       │   ├── easing
│   │       │   │   └── index.d.ts
│   │       │   ├── index.d.ts
│   │       │   ├── internal
│   │       │   │   ├── animations.d.ts
│   │       │   │   ├── await_block.d.ts
│   │       │   │   ├── Component.d.ts
│   │       │   │   ├── dev.d.ts
│   │       │   │   ├── dom.d.ts
│   │       │   │   ├── environment.d.ts
│   │       │   │   ├── globals.d.ts
│   │       │   │   ├── index.d.ts
│   │       │   │   ├── keyed_each.d.ts
│   │       │   │   ├── lifecycle.d.ts
│   │       │   │   ├── loop.d.ts
│   │       │   │   ├── ResizeObserverSingleton.d.ts
│   │       │   │   ├── scheduler.d.ts
│   │       │   │   ├── spread.d.ts
│   │       │   │   ├── ssr.d.ts
│   │       │   │   ├── style_manager.d.ts
│   │       │   │   ├── transitions.d.ts
│   │       │   │   ├── types.d.ts
│   │       │   │   └── utils.d.ts
│   │       │   ├── motion
│   │       │   │   ├── index.d.ts
│   │       │   │   ├── spring.d.ts
│   │       │   │   ├── tweened.d.ts
│   │       │   │   └── utils.d.ts
│   │       │   ├── ssr.d.ts
│   │       │   ├── store
│   │       │   │   └── index.d.ts
│   │       │   └── transition
│   │       │       └── index.d.ts
│   │       └── shared
│   │           ├── boolean_attributes.d.ts
│   │           └── utils
│   │               └── names.d.ts
│   └── vite
│       ├── bin
│       │   ├── openChrome.applescript
│       │   └── vite.js
│       ├── client.d.ts
│       ├── dist
│       │   ├── client
│       │   │   ├── client.mjs
│       │   │   ├── client.mjs.map
│       │   │   ├── env.mjs
│       │   │   └── env.mjs.map
│       │   ├── node
│       │   │   ├── chunks
│       │   │   │   ├── dep-5215c85e.js
│       │   │   │   ├── dep-845e3752.js
│       │   │   │   ├── dep-c423598f.js
│       │   │   │   ├── dep-f0c7dae0.js
│       │   │   │   └── dep-faa9987b.js
│       │   │   ├── cli.js
│       │   │   ├── constants.js
│       │   │   ├── index.d.ts
│       │   │   └── index.js
│       │   └── node-cjs
│       │       └── publicUtils.cjs
│       ├── index.cjs
│       ├── LICENSE.md
│       ├── package.json
│       ├── README.md
│       └── types
│           ├── customEvent.d.ts
│           ├── hmrPayload.d.ts
│           ├── hot.d.ts
│           ├── importGlob.d.ts
│           ├── importMeta.d.ts
│           ├── metadata.d.ts
│           └── package.json
├── package-lock.json
├── package.json
├── public
│   └── data.csv
├── src
│   ├── App.svelte
│   └── Sankey.svelte
└── vite.config.js

233 directories, 1494 files
sakshatgoyal@MacBook-Pro ~ %

## ChatGPT (2025-04-05T21:44:53.518382+00:00)

User's project folder is at `/Users/sakshatgoyal/Desktop/interactive-sankey`.

## ChatGPT (2025-04-05T21:44:57.066032+00:00)

Thanks! Based on your current structure at:

```
/Users/sakshatgoyal/Desktop/interactive-sankey
```

Here's a breakdown of what to **keep**, what to **add**, and what to **change**.

---

## ✅ You Can Keep As Is

| Folder/File | Why Keep It |
|-------------|-------------|
| `node_modules/` | All installed D3 and Svelte dependencies are already there. |
| `package.json` / `package-lock.json` | Already configured with necessary packages. |
| `vite.config.js` | Keep unless you later need to adjust asset paths. |
| `public/data.csv` | Keep this — we’ll read it using `d3.csv()` as your input data. |

---

## ✅ Rename or Replace

| Current File | What to Do | Why |
|--------------|------------|-----|
| `src/Sankey.svelte` | ✅ Rename to `ParallelSets.svelte` | Since we’re doing a **parallel sets** viz, not a Sankey. This helps avoid confusion. |

```bash
mv /Users/sakshatgoyal/Desktop/interactive-sankey/src/Sankey.svelte \
   /Users/sakshatgoyal/Desktop/interactive-sankey/src/ParallelSets.svelte
```

---

## ✅ Add These New Files

| File Path | Purpose |
|-----------|---------|
| `/src/lib/ParallelSets.svelte` | Component that renders the parallel sets visualization (after rename). |
| `/src/routes/+page.svelte` | Main page that imports and displays the component, plus filter UI. |

If `+page.svelte` already exists (from SvelteKit starter), we’ll just edit it later.

---

## ✅ Optional Cleanup

| File | Action |
|------|--------|
| `App.svelte` | Remove or leave untouched, depending on how your project entry point is set up. Not used if you're in a SvelteKit setup. |

---

## ✅ Next Step

Do you want to:
1. Start building the `ParallelSets.svelte` component from scratch now, or  
2. First update the main page (`+page.svelte`) to load the component and show basic dropdowns?

Let me know how you'd like to proceed.

## You (2025-04-05T21:52:23.406808+00:00)

Here's a recap of what I understood. Here are the three files in discussion along with their current location. 

/Users/sakshatgoyal/Desktop/interactive-sankey/public/data.csv
/Users/sakshatgoyal/Desktop/interactive-sankey/src/App.svelte
/Users/sakshatgoyal/Desktop/interactive-sankey/src/ParallelSets.svelte

there doesn't seem to be any lib folder in src folder.

## ChatGPT (2025-04-05T21:52:24.012874+00:00)

Perfect — your recap is right on point. Here's where we currently stand and what needs to happen next:

---

## ✅ Your Current Files

| File | Status |
|------|--------|
| `/Users/sakshatgoyal/Desktop/interactive-sankey/public/data.csv` | ✅ Good — this will be our input CSV. |
| `/Users/sakshatgoyal/Desktop/interactive-sankey/src/App.svelte` | ✅ Present — could be used as the main view (especially if you're not using SvelteKit). |
| `/Users/sakshatgoyal/Desktop/interactive-sankey/src/ParallelSets.svelte` | ✅ Renamed Sankey component — we’ll work on this soon. |

---

## 🆕 Optional: Create `lib/` Folder (if you want to keep things clean)

You **don’t have to** create a `lib/` folder unless you want to follow a more modular structure (common in SvelteKit). If you decide to use it:

```bash
mkdir /Users/sakshatgoyal/Desktop/interactive-sankey/src/lib
mv /Users/sakshatgoyal/Desktop/interactive-sankey/src/ParallelSets.svelte \
   /Users/sakshatgoyal/Desktop/interactive-sankey/src/lib/ParallelSets.svelte
```

But since you're using a simpler setup, you can also just **keep it directly under `/src/`** — that's totally fine.

---

## 🔜 Next Step

Would you like to:
1. **Build out the data loading and processing logic** inside `ParallelSets.svelte` now, or
2. First **set up `App.svelte` to load and display the component**?

Either works — just let me know where you'd like to begin.

