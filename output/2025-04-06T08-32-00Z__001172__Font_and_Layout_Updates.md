# Font and Layout Updates

## You (2025-04-06T08:32:00.126531+00:00)

I have the following code, and i need you to help me make the following edts

1. I want all fonts to be 'Anonymous Pro' available on google fonts on this page (https://fonts.google.com/specimen/Anonymous+Pro?categoryFilters=Appearance:%2FMonospace%2FMonospace;Feeling:%2FExpressive%2FBusiness)

This includes all headings, tooltips, buttons, filters, literally anything on the screen. 


2. Right now the dropdown filters are 3 in a row. I want to set a guideline wherein we set a fixed width of 240px, and the continue wrapping to the next line based on the available screen width. They'll have a 16px padding in between them horizontally, with a vertical spacing of about 24 px. 


I have more changes, but we'll work through that later. 




import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import copy

"""
How to run this file

1. Navigate to the folder in Terminal:
    cd /Users/sakshatgoyal/Desktop/Strategic\ Decision\ Making\ Work/Data\ Viz\ experiment

2. (Optional) Create a virtual environment (only once):
    python3 -m venv venv

3. Activate the virtual environment:
    source venv/bin/activate

4. Install any required dependencies:
    pip install -r requirements.txt

5. Run the file:
    python full_analyzer.py

6. Deactivate the virtual environment when done:
    deactivate
"""

# ------------------------------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------------------------------
CSV_FILE_PATH = 'Tagging - Compilation.csv'

# The categorical 'phases' we want to visualize as parallel sets:
STAGE_COLUMNS = [
    'Tension Axis',
    'Ambiguity Type',
    'Framing Move',
   'Friction Archetype',
    'Stabilizer',
    'False Clarity',
    'Org Implication'
]

# Contextual/Background columns used for filtering/highlighting but NOT removing
# them from the overall flow:
FILTER_COLUMNS = [
    'Regulatory Scope',
    'Temporal Coupling Sensitivity',
    'Market Dispersion',
    'Capital Substrate Intensity',
    'Decomposability Gradient',
    'Temporal Value Elasticity',
    'Knowledge Codifiability'
]

# We will allow *all* columns (both "phases" and "filter columns") to be used
# for highlighting criteria. That way a user can highlight by Tension Axis,
# or by Market Dispersion, etc. The rest remain in grey.
ALL_FILTERABLE_COLUMNS = STAGE_COLUMNS + FILTER_COLUMNS

# Colors:
HIGHLIGHT_COLOR = 'rgba(180, 0, 35, 0.8)'  # Pink highlight
REMAINDER_COLOR = 'rgba(235, 226, 217, 0.8)' # Light grey
NODE_DEFAULT_COLOR = 'rgba(170,170,170,0.8)'  # Grey-ish for nodes

NODE_PAD = 25
NODE_THICKNESS = 16
FONT_SIZE = 14
SANKEY_HEIGHT = 750

# ------------------------------------------------------------------------------------
# DATA LOADING
# ------------------------------------------------------------------------------------
def load_data(filepath):
    """Loads the CSV and ensures each relevant column is present (if missing, fill as 'Unknown')."""
    try:
        df = pd.read_csv(filepath)
        # Ensure columns exist, fill missing with "Unknown"
        needed_cols = set(STAGE_COLUMNS + FILTER_COLUMNS)
        for col in needed_cols:
            if col not in df.columns:
                print(f"Warning: Missing column '{col}' in CSV. Using 'Unknown' for it.")
                df[col] = "Unknown"
            else:
                # Convert to str and strip
                df[col] = df[col].fillna('Unknown').astype(str).str.strip()

        # It's also helpful to have an ID for each row (e.g. "Module ID") if it exists:
        if 'Module ID' not in df.columns:
            # Not strictly required, but let's ensure we have some unique reference
            df['Module ID'] = df.index.astype(str)

        print(f"Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns.")
        return df
    except FileNotFoundError:
        print(f"File not found at: {filepath}")
        return pd.DataFrame()
    except Exception as e:
        print("Error loading data:", e)
        return pd.DataFrame()

df_full = load_data(CSV_FILE_PATH)

# ------------------------------------------------------------------------------------
# BUILD THE STATIC NODE LAYOUT FOR THE FULL DATASET
# (We do this ONCE so that Sankey node positions remain the same; no re-layout.)
# ------------------------------------------------------------------------------------
def prepare_sankey_nodes(df, stage_cols):
    """
    Create a fixed x,y layout for each (stage, category) pair across the entire dataset.
    Returns:
      - dict of lists: {
            'labels': [...],
            'x': [...],
            'y': [...],
            'stages': [...]
        }
      - a map from node_id to node_index
    """
    if df.empty:
        return {'labels': [], 'x': [], 'y': [], 'stages': []}, {}

    # We assign each stage to a vertical "slice" (x-position),
    # and each category within that stage to some spaced y-position.
    num_stages = len(stage_cols)
    if num_stages <= 1:
        # Edge case: only one stage means no "links" anyway
        return {'labels': [], 'x': [], 'y': [], 'stages': []}, {}

    stage_width = 1.0 / (num_stages - 1)  # distance between stage columns
    all_nodes = []
    node_xpos = {}
    node_ypos = {}

    for i, stage in enumerate(stage_cols):
        unique_vals = sorted(df[stage].unique())
        x_pos = i * stage_width
        count_vals = len(unique_vals)
        # We space them in [0..1], with some small fractional offset:
        y_step = 1.0 / (count_vals + 1) if count_vals else 0.5

        for j, val in enumerate(unique_vals):
            node_id = f"{stage}_{val}"
            all_nodes.append({
                'id': node_id,
                'label': val,
                'stage': stage
            })
            node_xpos[node_id] = x_pos
            node_ypos[node_id] = (j + 1) * y_step

    # Create a node_map for referencing
    node_map = {nd['id']: idx for idx, nd in enumerate(all_nodes)}

    # Build final structures
    node_labels = [nd['label'] for nd in all_nodes]
    node_stages = [nd['stage'] for nd in all_nodes]
    node_x = [node_xpos[nd['id']] for nd in all_nodes]
    node_y = [node_ypos[nd['id']] for nd in all_nodes]

    return {
        'labels': node_labels,
        'x': node_x,
        'y': node_y,
        'stages': node_stages
    }, node_map

full_nodes_data, full_node_map = prepare_sankey_nodes(df_full, STAGE_COLUMNS)

# ------------------------------------------------------------------------------------
# HELPERS: BUILD THE LINK DATA (2-LINK APPROACH FOR HIGHLIGHT vs REMAINDER)
# ------------------------------------------------------------------------------------
def build_sankey_links(df, df_highlight, stage_cols, node_map):
    """
    Construct the sankey link data for the ENTIRE dataset (df) + a highlighted subset (df_highlight).
    We'll create two sets of links between each pair of adjacent stages:
      1) A "highlight" link in pink for the subset count
      2) A "remainder" link in grey for the rest
    So each (stage_col, next_stage_col, cat_val1, cat_val2) pair can produce up to two links.

    Returns a dict with:
       {
         'source': [...],
         'target': [...],
         'value': [...],
         'label': [...],
         'color': [...]
       }
    """
    links = {
        'source': [],
        'target': [],
        'value': [],
        'label': [],
        'color': []
    }

    if df.empty or len(stage_cols) < 2:
        return links

    num_stages = len(stage_cols)
    # Pre-group both the full dataset and the highlight subset
    # by pairs of adjacent columns:
    # e.g. groupby([Tension Axis, Ambiguity Type]) => count
    # We'll do that for each adjacent stage i -> i+1
    for i in range(num_stages - 1):
        s_col = stage_cols[i]
        t_col = stage_cols[i + 1]

        # Full dataset link counts:
        full_gb = df.groupby([s_col, t_col]).size().reset_index(name='full_count')
        # Highlight subset link counts:
        if df_highlight.empty:
            high_gb = pd.DataFrame(columns=[s_col, t_col, 'highlight_count'])
        else:
            high_gb = df_highlight.groupby([s_col, t_col]).size().reset_index(name='highlight_count')

        # Merge them so we can see (full_count, highlight_count) side by side
        merged = pd.merge(
            full_gb, high_gb,
            on=[s_col, t_col],
            how='left'
        ).fillna({'highlight_count': 0})

        for _, row in merged.iterrows():
            s_val = row[s_col]
            t_val = row[t_col]
            total_ct = row['full_count']
            highlight_ct = row['highlight_count']
            remainder_ct = total_ct - highlight_ct

            s_id = f"{s_col}_{s_val}"
            t_id = f"{t_col}_{t_val}"
            if s_id not in node_map or t_id not in node_map:
                # Shouldn't happen unless data changed
                continue

            s_idx = node_map[s_id]
            t_idx = node_map[t_id]

            # 1) Highlight link (pink)
            if highlight_ct > 0:
                links['source'].append(s_idx)
                links['target'].append(t_idx)
                links['value'].append(highlight_ct)
                links['label'].append(f"{s_val} -> {t_val} (highlight)")
                links['color'].append(HIGHLIGHT_COLOR)

            # 2) Remainder link (grey)
            # only if there's something left
            if remainder_ct > 0:
                links['source'].append(s_idx)
                links['target'].append(t_idx)
                links['value'].append(remainder_ct)
                links['label'].append(f"{s_val} -> {t_val} (remainder)")
                links['color'].append(REMAINDER_COLOR)

    return links

# ------------------------------------------------------------------------------------
# DASH APP
# ------------------------------------------------------------------------------------
app = dash.Dash(__name__)
app.title = "Parallel Sets Highlighter"
app.css.append_css({"external_url": "https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap"})

# Build dynamic dropdowns for each "filterable" column
def dropdown_filter_block(col):
    return html.Div([
        html.Label(f"{col}:"),
        dcc.Dropdown(
            id=f'filter-{col}',
            options=[{'label': v, 'value': v} for v in sorted(df_full[col].unique())] 
                if col in df_full.columns else [],
            multi=True,
            placeholder=f"Highlight by {col}..."
        )
    ], style={'width': '30%', 'display': 'inline-block', 'padding': '5px'})

app.layout = html.Div([
    html.H1("Parallel Sets-Style Visualization with Highlighting"),

    html.Div([
        dropdown_filter_block(c) for c in ALL_FILTERABLE_COLUMNS
    ], style={'marginBottom': '20px'}),

    html.Button('Reset All Selections', id='reset-button', n_clicks=0, style={'marginBottom': '10px'}),

    dcc.Loading(
        id="loading-sankey",
        type="circle",
        children=dcc.Graph(
            id='sankey-diagram',
            config={'displayModeBar': True}
        )
    ),
    html.Div(id='debug-output', style={'marginTop': '20px', 'whiteSpace': 'pre-wrap', 'fontFamily': 'monospace'})
], style={'fontFamily': "'Source Code Pro', monospace"})
    


# A small convenience to produce default "None" for each filter
def empty_filter_dict():
    return {col: [] for col in ALL_FILTERABLE_COLUMNS}

@app.callback(
    Output('sankey-diagram', 'figure'),
    Output('debug-output', 'children'),
    [Input(f'filter-{col}', 'value') for col in ALL_FILTERABLE_COLUMNS] + [Input('reset-button', 'n_clicks')]
)
def update_sankey(*args):
    """
    The callback will be triggered by changes to any column's filter selection
    or the reset button.
    We'll interpret the final argument as the reset button clicks.
    """
    ctx = dash.callback_context
    if not ctx.triggered:
        # Initial load
        filter_values = empty_filter_dict()
        reset_clicks = 0
    else:
        # We get len(ALL_FILTERABLE_COLUMNS) + 1 inputs in *args
        n_filter_cols = len(ALL_FILTERABLE_COLUMNS)
        filter_vals_list = args[:n_filter_cols]
        reset_clicks = args[n_filter_cols]

        # Check if the trigger is the reset button
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if triggered_id == 'reset-button':
            # If reset is clicked, we discard filter selections
            filter_values = empty_filter_dict()
        else:
            filter_values = {}
            for col, val in zip(ALL_FILTERABLE_COLUMNS, filter_vals_list):
                # val might be None or a list
                if val is None:
                    val = []
                filter_values[col] = val

    # -- Build the highlight subset based on filter_values
    # A row is included in the highlight subset if it meets
    # (col in filter_values[col]) for all columns that have non-empty lists
    # i.e. an AND across columns
    df_highlight = df_full.copy()
    for col, selected_vals in filter_values.items():
        if selected_vals:  # non-empty => filter
            df_highlight = df_highlight[df_highlight[col].isin(selected_vals)]

    debug_messages = []
    debug_messages.append(f"Reset button clicks: {reset_clicks}")
    debug_messages.append("Current Selections:")
    for col in ALL_FILTERABLE_COLUMNS:
        if filter_values[col]:
            debug_messages.append(f"  {col}: {filter_values[col]}")
    debug_messages.append(f"Highlighted subset: {df_highlight.shape[0]} rows out of {df_full.shape[0]} total.")

    # Build links using 2-link approach
    links_data = build_sankey_links(df_full, df_highlight, STAGE_COLUMNS, full_node_map)

    # Build node coloring: pink if node is used by the highlight subset, else grey
    # We'll check how many highlight rows each node has. If > 0 => pink.
    highlight_node_counts = {}
    if not df_highlight.empty:
        for stage in STAGE_COLUMNS:
            # count how many rows for each category in highlight set
            vc = df_highlight[stage].value_counts()
            for cat_val, ct in vc.items():
                node_id = f"{stage}_{cat_val}"
                if node_id not in highlight_node_counts:
                    highlight_node_counts[node_id] = 0
                highlight_node_counts[node_id] += ct

        total_row_count = len(df_full)
    subset_row_count = len(df_highlight)

    node_colors = []
    node_customdata = []

    for i, lbl in enumerate(full_nodes_data['labels']):
        stage = full_nodes_data['stages'][i]
        node_id = f"{stage}_{lbl}"

        # Total count and % (from df_full)
        total_ct = df_full[df_full[stage] == lbl].shape[0]
        total_pct = (total_ct / total_row_count) * 100 if total_row_count > 0 else 0

        # Subset count and % (from df_highlight)
        subset_ct = df_highlight[df_highlight[stage] == lbl].shape[0]
        subset_pct = (subset_ct / subset_row_count) * 100 if subset_row_count > 0 else 0

        # Color logic
        color = HIGHLIGHT_COLOR if subset_ct > 0 else NODE_DEFAULT_COLOR
        node_colors.append(color)

        # Customdata layout:
        # [stage, total_ct, total_row_count, total_pct, subset_ct, subset_row_count, subset_pct]
        node_customdata.append([
            stage,
            total_ct,
            total_row_count,
            total_pct,
            subset_ct,
            subset_row_count,
            subset_pct
        ])

    # Build figure
    fig = go.Figure(data=[go.Sankey(
        arrangement='snap',  # keep positions fixed
        valueformat=".0f",
        node=dict(
            pad=NODE_PAD,
            thickness=NODE_THICKNESS,
            label=full_nodes_data['labels'],
            x=full_nodes_data['x'],
            y=full_nodes_data['y'],
            color=node_colors,
            line=dict(color='black', width=0.5),
            customdata=node_customdata,
            hovertemplate=(
                "<b>%{label}</b><br>"
                "Stage: %{customdata[0]}<br>"
                "Count: %{customdata[1]} of %{customdata[2]}<br>"
                "Percentage: %{customdata[3]:.1f}%<br>"
                "<br>"
                "SUBSET METRICS:<br>"
                "Count: %{customdata[4]} of %{customdata[5]}<br>"
                "Percentage: %{customdata[6]:.1f}%<extra></extra>"
            )
        ),
        link=dict(
            source=links_data['source'],
            target=links_data['target'],
            value=links_data['value'],
            label=links_data['label'],
            color=links_data['color'],
            hovertemplate=(
                "Path: %{label}<br>"
                "Count: %{value}<extra></extra>"
            )
        )
    )])

    fig.update_layout(
    title="Parallel Sets: Decision Journeys Across Phases (Entire Data in Grey, Highlight in Pink)",
    font=dict(family="'Source Code Pro', monospace", size=FONT_SIZE),
    height=SANKEY_HEIGHT,
    margin=dict(l=40, r=40, t=80, b=40)
)

    return fig, "\n".join(debug_messages)


# ------------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------------
if __name__ == '__main__':
    if df_full.empty:
        print("ERROR: The CSV is empty or could not be loaded. Check the path:", CSV_FILE_PATH)
    elif not full_nodes_data['labels']:
        print("ERROR: Sankey structure is invalid (missing stage columns?).")
    else:
        print("Dash app running at http://127.0.0.1:8050")
        app.run_server(debug=True)

## ChatGPT (2025-04-06T08:32:01.184904+00:00)

Here’s exactly what to change in your code to apply the **'Anonymous Pro'** font everywhere and fix the **dropdown filter layout** as requested.

---

### ✅ 1. Change font to "Anonymous Pro" everywhere

#### First: Add Google Fonts link (replacing the old one)

Find this line (near the start of your Dash app setup):

```python
app.css.append_css({"external_url": "https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap"})
```

Replace it with:

```python
app.css.append_css({"external_url": "https://fonts.googleapis.com/css2?family=Anonymous+Pro&display=swap"})
```

#### Next: Update all font references in `style` and layout

Find this line (end of the `app.layout` definition):

```python
], style={'fontFamily': "'Source Code Pro', monospace"})
```

Replace it with:

```python
], style={'fontFamily': "'Anonymous Pro', monospace"})
```

Also scroll down to the `fig.update_layout(...)` section and change this:

```python
font=dict(family="'Source Code Pro', monospace", size=FONT_SIZE),
```

To:

```python
font=dict(family="'Anonymous Pro', monospace", size=FONT_SIZE),
```

Now **everything on the page** (headings, tooltips, dropdowns, buttons) will use `Anonymous Pro`.

---

### ✅ 2. Set dropdown filters to wrap with fixed width and spacing

Find this block of code inside the `dropdown_filter_block(col)` function:

```python
    ], style={'width': '30%', 'display': 'inline-block', 'padding': '5px'})
```

Replace it with:

```python
    ], style={
        'width': '240px',
        'display': 'inline-block',
        'marginRight': '16px',
        'marginBottom': '24px',
        'verticalAlign': 'top'
    })
```

This sets:
- fixed width = `240px`
- horizontal spacing = `16px` (via `marginRight`)
- vertical spacing = `24px` (via `marginBottom`)
- makes them wrap by screen width

---

That's it for these two edits. Let me know the next batch when ready!

