# Donut Chart Legend Sync

## You (2025-04-08T23:07:29.583544+00:00)

✅ Goal

Ensure that donut chart legends remain visible below each donut, even when filters are applied and the data subset changes.

Each donut represents a categorical variable (from FILTER_COLUMNS), and its segments show the filtered distribution. Below each donut, a legend explains what each segment means (with color and percentage).
These legends should always be rendered and remain synchronized with the donut, even if the chart becomes sparse due to filtering.

⸻

📦 Return Format

Each donut (pie chart with hole) must have:
	•	A centered, wrapped title annotation
	•	A legend annotation below the donut, at least 16% below the bottom edge
	•	The legend must include:
	•	A bullet (●) with the matching color
	•	The segment label
	•	The percentage share of that segment

When a filter is applied:
	•	Donuts with no data should still render (if possible) with empty state
	•	Donuts with sparse data should still display the corresponding legend, even if it only contains one or two entries

⸻

🛡️ Guardrails (Things Not to Do)
	•	❌ Do not remove or suppress the legend annotation just because the category has fewer entries or a single entry
	•	❌ Do not collapse the donut or hide it entirely just because one category has no variation after filtering
	•	❌ Do not skip rendering annotations for performance — even if it seems “empty”, the legend is part of the interface and should persist
	•	❌ Do not use HTML-based legend blocks outside the plot — they must remain tightly coupled and visually aligned with the donut chart inside the figure
	•	❌ Do not overwrite or drop annotations during filter redraw unless you are preserving all previous ones + updating with new ones

⸻

🧠 Additional Context
	•	This is a Dash + Plotly app that uses make_subplots(rows=1, cols=n) and go.Pie(...) to render donut charts dynamically.
	•	The donut chart is redrawn every time filters are applied. It uses a dcc.Graph(id='donut-charts', ...) that is updated via callback.
	•	Each donut gets its title and legend via annotations added to the layout.
	•	The legend is rendered as a Plotly annotation, usually like:

annotations.append(dict(
    x=x_center,
    y=y_below,
    text=legend_text,
    ...
))

	•	The problem seems to occur when the value_counts() inside the filtered DataFrame becomes empty or very sparse (e.g., 1 item). It’s likely that the code skips building a legend if value_counts() has too few rows.
	•	In those cases, the donut still renders (even with 1 segment), but the legend annotation below it disappears.

⸻

🧪 Repro Steps
	1.	Load the full dashboard
	2.	Observe that all donut legends are visible under each donut
	3.	Apply a filter that narrows the dataset (e.g., select Cluster Label = 11)
	4.	Observe that many of the legends disappear, even though the donut ring is still rendered (and has 1–2 segments)

⸻


FULL CODE:


import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import dash
from dash import dcc, html, dash_table, callback_context
from dash.dependencies import Input, Output, State
import copy



"""
How to run this file

To RUN:
cd /Users/sakshatgoyal/Desktop/Strategic\ Decision\ Making\ Work/Data\ Viz\ experiment && \
python3 -m venv venv && \
source venv/bin/activate && \
python full_analyzer.py

-----
Modify the path based on your system.
-----

Optional Steps:
Install any required dependencies:
    pip install -r requirements.txt

Deactivate the virtual environment when done:
    deactivate

-----

"""
CSV_FILE_PATH = 'Tagging - Business Clusters - 4+4.csv'

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

# Custom labels for the stages (for display purposes):
CUSTOM_STAGE_LABELS = {
    'Tension Axis': 'Hidden tensions shaping the decision',
    'Ambiguity Type': 'The core ambiguity in the moment',
    'Framing Move': 'How meaning was made from uncertainty',
    'Friction Archetype': 'What resisted or blocked progress',
    'Stabilizer': 'What made the decision possible',
    'False Clarity': 'Was the clarity real or an illusion?',
    'Org Implication': 'How the org changed as a result'
}

# Contextual/Background columns used for filtering/highlighting:
FILTER_COLUMNS = [
    'Regulatory Scope',
    'Temporal Coupling Sensitivity',
    'Market Dispersion',
    'Capital Substrate Intensity',
    'Decomposability Gradient',
    'Temporal Value Elasticity',
    'Knowledge Codifiability'
    ,'Cluster Label'
]

# We allow all these columns to be used in the highlight filters:
ALL_FILTERABLE_COLUMNS = STAGE_COLUMNS + FILTER_COLUMNS

# ------------------------
# Color Constants
# ------------------------
# Node color when no filters are active
DEFAULT_NODE_COLOR = 'rgba(5, 51, 74, 1)'

# Link color when no filters are active
DEFAULT_LINK_COLOR = 'rgba(107, 158, 189, 0.8)'     

# Node color for highlight subset
HIGHLIGHT_NODE_COLOR = 'rgba(0, 0, 4, 1)'  

# Node color for non-highlight subset
NON_HIGHLIGHT_NODE_COLOR = 'rgba(160,160,160,0.2)'  

# Link color for highlight subset
HIGHLIGHT_LINK_COLOR = 'rgba(180, 0, 35, 0.5)'   

# Link color for non-highlight subset
NON_HIGHLIGHT_LINK_COLOR = 'rgba(160,160,160,0.2)'  

# Donut color scheme for each wedge (example palette):
DONUT_COLORS = [
    "#012749",  # dark
    "#8a3ffc",  # medium
    "#3ddbd9"   # light
]

# Sankey layout geometry:
NODE_PAD = 25
NODE_THICKNESS = 8
FONT_SIZE = 12

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
                df[col] = df[col].fillna('Unknown').astype(str).str.strip()

        # Add an ID for each row if none provided:
        if 'Module ID' not in df.columns:
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
# BUILD STATIC NODE LAYOUT (for selected stages) so Sankey node positions remain stable
# ------------------------------------------------------------------------------------
def prepare_sankey_nodes(df, stage_cols):
    """
    Create a fixed x,y layout for each (stage, category) pair.
    Returns a dict containing node label, x, y, stage, plus a node_map for references.
    """
    if df.empty:
        return {'labels': [], 'x': [], 'y': [], 'stages': []}, {}

    num_stages = len(stage_cols)
    if num_stages <= 1:
        return {'labels': [], 'x': [], 'y': [], 'stages': []}, {}

    stage_width = 1.0 / (num_stages - 1)
    all_nodes = []
    node_xpos = {}
    node_ypos = {}

    for i, stage in enumerate(stage_cols):
        unique_vals = sorted(df[stage].unique())
        x_pos = i * stage_width
        count_vals = len(unique_vals)
        if count_vals == 0:
            continue
        # Space them in [0..1], with small offsets
        y_step = 1.0 / (count_vals + 1)

        for j, val in enumerate(unique_vals):
            node_id = f"{stage}_{val}"
            all_nodes.append({
                'id': node_id,
                'label': val,
                'stage': stage
            })
            node_xpos[node_id] = x_pos
            node_ypos[node_id] = (j + 1) * y_step

    node_map = {nd['id']: idx for idx, nd in enumerate(all_nodes)}
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

# ------------------------------------------------------------------------------------
# BUILD THE LINK DATA
# ------------------------------------------------------------------------------------
def build_sankey_links(df, df_highlight, stage_cols, node_map):
    """
    Construct link data for the entire dataset + highlighted subset.
    If filters are active, produce 2 sets of links: highlight & remainder.
    If no filters, produce a single set of links with default color.
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
    # Check if any filter is actually active:
    any_filter_active = (not df_highlight.empty) and (len(df_highlight) < len(df))

    for i in range(num_stages - 1):
        s_col = stage_cols[i]
        t_col = stage_cols[i + 1]

        # Full dataset counts:
        full_gb = df.groupby([s_col, t_col]).size().reset_index(name='full_count')

        # Highlight subset counts:
        if df_highlight.empty:
            # If highlight is empty, no highlight links
            high_gb = pd.DataFrame(columns=[s_col, t_col, 'highlight_count'])
        else:
            high_gb = df_highlight.groupby([s_col, t_col]).size().reset_index(name='highlight_count')

        merged = pd.merge(full_gb, high_gb, on=[s_col, t_col], how='left').fillna({'highlight_count': 0})

        for _, row in merged.iterrows():
            s_val = row[s_col]
            t_val = row[t_col]
            total_ct = row['full_count']
            highlight_ct = row['highlight_count']
            remainder_ct = total_ct - highlight_ct

            s_id = f"{s_col}_{s_val}"
            t_id = f"{t_col}_{t_val}"
            if s_id not in node_map or t_id not in node_map:
                continue

            s_idx = node_map[s_id]
            t_idx = node_map[t_id]

            if any_filter_active:
                # 1) Highlight link
                if highlight_ct > 0:
                    links['source'].append(s_idx)
                    links['target'].append(t_idx)
                    links['value'].append(highlight_ct)
                    links['label'].append(f"{s_val} -> {t_val} (highlight)")
                    links['color'].append(HIGHLIGHT_LINK_COLOR)
                # 2) Remainder link
                if remainder_ct > 0:
                    links['source'].append(s_idx)
                    links['target'].append(t_idx)
                    links['value'].append(remainder_ct)
                    links['label'].append(f"{s_val} -> {t_val} (remainder)")
                    links['color'].append(NON_HIGHLIGHT_LINK_COLOR)
            else:
                # No filter => single set of links with default color
                links['source'].append(s_idx)
                links['target'].append(t_idx)
                links['value'].append(total_ct)
                links['label'].append(f"{s_val} -> {t_val}")
                links['color'].append(DEFAULT_LINK_COLOR)

    return links

# ------------------------------------------------------------------------------------
# Initialize the Dash app
# ------------------------------------------------------------------------------------
app = dash.Dash(__name__)
app.title = "Parallel Sets Highlighter"

# Build filter dropdowns
def dropdown_filter_block(col):
    return html.Div([
        html.Label(f"{col}:", style={'fontWeight': 'regular'}),
        dcc.Dropdown(
            id=f'filter-{col}',
            options=[{'label': v, 'value': v} for v in sorted(df_full[col].unique())]
                if col in df_full.columns else [],
            multi=True,
            placeholder=f"Filter by {col}..."
        )
    ], style={
        'width': '300px',
        'display': 'inline-block',
        'marginRight': '16px',
        'marginBottom': '24px',
        'verticalAlign': 'top'
    })

# Main layout
app.layout = html.Div([
    html.H1("Parallel Sets-Style Visualization with Highlighting"),

    dcc.Store(id='window-width'),

    html.Div([
        html.Label("Select Phases (Columns to Visualize):",
                   style={'fontWeight': 'regular', 'marginRight': '8px', 'fontFamily': "'Anonymous Pro', monospace"}),
        dcc.Dropdown(
            id='stage-selection',
            options=[{'label': col, 'value': col} for col in STAGE_COLUMNS],
            value=STAGE_COLUMNS,
            multi=True,
            style={'width': '600px'}
        )
    ], style={
        'marginBottom': '20px',
        'fontFamily': "'Anonymous Pro', monospace"
    }),

    html.Div([
        dropdown_filter_block(c) for c in ALL_FILTERABLE_COLUMNS
    ], style={
        'marginBottom': '20px',
        'fontFamily': "'Anonymous Pro', monospace"
    }),

    html.Div([
    dcc.Checklist(
        id='sankey-label-toggle',
        options=[{'label': ' Show Sankey Labels', 'value': 'show'}],
        value=['show'],
        labelStyle={'display': 'inline-block', 'marginRight': '12px'}
    )
], style={'marginBottom': '20px'}),

    html.Button('Reset All Selections', id='reset-button', n_clicks=0,
                style={'marginBottom': '20px', 'fontFamily': "'Anonymous Pro', monospace"}),

    dcc.Graph(
        id='donut-charts',
        config={'displayModeBar': False},
        style={'width': '100%', 'height': '400px'}
    ),

    html.Div([
    html.Div(id='stage-labels-container'),
    dcc.Graph(
        id='sankey-diagram',
        config={'displayModeBar': True},
        style={'width': '100%'}
    )
], id='sankey-container', style={
    'position': 'relative',
    'width': '100%',
    'fontFamily': "'Anonymous Pro', monospace"
}),

    html.Div(
        children=[
            html.Div(id='table-row-count', style={
                'fontWeight': 'regular',
                'margin': '10px 0',
                'fontFamily': "'Anonymous Pro', monospace"
            }),
            dash_table.DataTable(
                id='filtered-table',
                style_table={
                    'overflowX': 'auto',
                    'maxHeight': '400px',
                    'overflowY': 'auto'
                },
                style_cell={
                    'fontFamily': "'Anonymous Pro', monospace",
                    'minWidth': '120px',
                    'width': '120px',
                    'maxWidth': '180px',
                    'whiteSpace': 'normal',
                    'textAlign': 'left'
                },
                fixed_rows={'headers': True, 'data': 0}
            )
        ],
        style={'marginTop': '30px'}
    ),

    html.Div(id='debug-output', style={
        'marginTop': '20px',
        'whiteSpace': 'pre-wrap',
        'fontFamily': "'Anonymous Pro', monospace"
    })
], style={'fontFamily': "'Anonymous Pro', monospace"})

# ------------------------------------------------------------------------------------
# CLIENTSIDE CALLBACK to read window.innerWidth
# (Alternatively, you can use a window event listener approach. This is just one approach.)
# ------------------------------------------------------------------------------------
@app.callback(
    Output('window-width', 'data'),
    [Input('interval-resize', 'n_intervals')],
    prevent_initial_call=True
)
def update_window_size(_):
    """
    Triggers periodically to store the window.innerWidth in dash Store.
    We fetch it via clientside JS. The property is updated if changed.
    """
    # Clientside code snippet that returns current window width:
    # If no JS injection is allowed, an alternative is dash_extensions.
    # For brevity, returning a dummy number here. Replace with a real approach if needed.
    return 1200  # fallback if you can't do full clientside. Adjust as needed.

# ------------------------------------------------------------------------------------
# MAIN CALLBACK
#   1) Build Sankey figure
#   2) Build donut figure
#   3) Return debug info
#   4) Return filtered subset for table
#   5) Return row count label
# ------------------------------------------------------------------------------------
@app.callback(
    Output('sankey-diagram', 'figure'),
    Output('donut-charts', 'figure'),
    Output('debug-output', 'children'),
    Output('filtered-table', 'data'),
    Output('filtered-table', 'columns'),
    Output('table-row-count', 'children'),
    [
        Input(f'filter-{col}', 'value') for col in ALL_FILTERABLE_COLUMNS
    ] +
    [
        Input('reset-button', 'n_clicks'),
        Input('stage-selection', 'value'),
        Input('window-width', 'data')  # to dynamically set sankey height
        , Input('sankey-label-toggle', 'value')
    ]
)
def update_visuals(*args):
    """
    The callback updates:
    - Sankey diagram (with highlight logic)
    - Donut charts
    - The debug text
    - The table with the filtered rows
    - The row count label
    """
    ctx = callback_context
    num_filter_cols = len(ALL_FILTERABLE_COLUMNS)

    # Unpack inputs
    filter_vals_list = args[:num_filter_cols]
    reset_clicks = args[num_filter_cols]
    selected_stages = args[num_filter_cols + 1]
    window_width = args[num_filter_cols + 2] or 1200  
    label_toggle_vals = args[num_filter_cols + 3]
    show_labels = 'show' in label_toggle_vals# default

    # Determine whether the user hit "Reset" button
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else ""

    # If user clicked Reset, we ignore filter selections
    if triggered_id == 'reset-button':
        # Clear all filters
        filter_values = {col: [] for col in ALL_FILTERABLE_COLUMNS}
    else:
        filter_values = {}
        for col, val in zip(ALL_FILTERABLE_COLUMNS, filter_vals_list):
            filter_values[col] = val if val else []

    # Validate stage selection
    if not selected_stages or len(selected_stages) < 2:
        # Return early with a message
        no_sankey_fig = go.Figure()
        no_sankey_fig.update_layout(
            annotations=[dict(text="Please select at least 2 stages to display.",
                              showarrow=False, x=0.5, y=0.5, xanchor='center', yanchor='middle')]
        )
        # Also return empty donut figs, empty table
        return (no_sankey_fig, go.Figure(), "Insufficient stages selected.",
                [], [], "0 rows match current filters")

    # Subset highlight DataFrame based on filter values
    df_highlight = df_full.copy()
    for col, selected_vals in filter_values.items():
        if selected_vals:
            df_highlight = df_highlight[df_highlight[col].isin(selected_vals)]

    # Build node layout
    sankey_nodes_data, sankey_node_map = prepare_sankey_nodes(df_full, selected_stages)

    # Build links
    links_data = build_sankey_links(df_full, df_highlight, selected_stages, sankey_node_map)

    # Count total rows / subset
    total_row_count = len(df_full)
    subset_row_count = len(df_highlight)

    # Check if any filter is active
    any_filter_active = (subset_row_count < total_row_count)

    # Build node colors
    node_colors = []
    node_customdata = []
    for i, label in enumerate(sankey_nodes_data['labels']):
        stage = sankey_nodes_data['stages'][i]
        node_id = f"{stage}_{label}"

        # total in full set
        total_ct = df_full[df_full[stage] == label].shape[0]
        total_pct = (total_ct / total_row_count * 100) if total_row_count else 0

        # subset in highlight
        subset_ct = df_highlight[df_highlight[stage] == label].shape[0]
        subset_pct = (subset_ct / subset_row_count * 100) if subset_row_count else 0

        if any_filter_active:
            # If node is in highlight set => highlight color
            color = HIGHLIGHT_NODE_COLOR if subset_ct > 0 else NON_HIGHLIGHT_NODE_COLOR
        else:
            # No filters => single default color
            color = DEFAULT_NODE_COLOR

        node_colors.append(color)
        node_customdata.append([
            stage,
            total_ct,
            total_row_count,
            total_pct,
            subset_ct,
            subset_row_count,
            subset_pct
        ])

    # -- Create Sankey figure --
    sankey_fig = go.Figure(data=[go.Sankey(
        arrangement='snap',
        valueformat=".0f",
        node=dict(
            pad=NODE_PAD,
            thickness=NODE_THICKNESS,
            label=sankey_nodes_data['labels'] if show_labels else ['' for _ in sankey_nodes_data['labels']],
            x=sankey_nodes_data['x'],
            y=sankey_nodes_data['y'],
            color=node_colors,
            line=dict(color='rgba(0,0,0,0)', width=0),
            customdata=node_customdata,
            hovertemplate=(
                "<b style='font-size:16px;'>%{label}</b><br><br>"
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

    # Calculate the Sankey height based on window width => 16:9 ratio
    # Sankey Chart Layout padding
    sankey_height = (16/9) * window_width

    sankey_fig.update_layout(
        font=dict(family="'Anonymous Pro', monospace",size=FONT_SIZE),
        height=790,  # dynamic
        margin=dict(l=160, r=160, t=40, b=160)
    )

        # -- Build Donut Charts --


        
    # For each filter column, we show a donut of the highlight subset distribution

    def wrap_text(text, max_chars_per_line=14):
        """
        Breaks a string into multiple lines with <br>, ensuring each line
        is no longer than max_chars_per_line based on word boundaries.
        """
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            if len(current_line + " " + word) <= max_chars_per_line:
                current_line = (current_line + " " + word).strip()
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return "<br>".join(lines)
    n_cols = len(FILTER_COLUMNS)
    if n_cols == 0:
        donut_fig = go.Figure()
    else:
        donut_fig = make_subplots(
            rows=1, cols=n_cols,
            specs=[[{'type': 'domain'}]*n_cols]
        )

        annotations = []

        for idx, col in enumerate(FILTER_COLUMNS):
            if col not in df_highlight.columns:
                continue

            series = df_highlight[col]
            vc = series.value_counts()
            vc_sorted = vc.sort_values(ascending=True)

            labels = vc_sorted.index.tolist()
            values = vc_sorted.values.tolist()

            color_list = [DONUT_COLORS[i % len(DONUT_COLORS)] for i in range(len(labels))]

            # Add pie chart trace
            pie_trace = go.Pie(
                labels=labels,
                values=values,
                marker=dict(colors=color_list),
                hole=0.9,
                direction='clockwise',
                rotation=0,
                sort=False,
                textinfo='none',
                showlegend=False
            )
            donut_fig.add_trace(pie_trace, row=1, col=idx+1)

            # Extract the actual domain of this subplot's donut to calculate its center
            trace_idx = len(donut_fig.data) - 1
            domain = donut_fig.data[trace_idx].domain
            x_center = (domain['x'][0] + domain['x'][1]) / 2
            y_center = (domain['y'][0] + domain['y'][1]) / 2

            # Title goes at the exact center of the donut
           

            # Title goes at the exact center of the donut
            # Auto-wrapped centered title inside donut
            # Automatically insert line break for long titles
            wrapped_title = col
            words = col.split()
            wrapped_title = ""

            if len(words) <= 2:
                wrapped_title = col
            elif len(words) == 3:
                wrapped_title = f"{words[0]}<br>{words[1]} {words[2]}"
            elif len(words) == 4:
                wrapped_title = f"{words[0]} {words[1]}<br>{words[2]} {words[3]}"
            else:
                third = len(words) // 3
                second_third = 2 * third
                wrapped_title = (
                    " ".join(words[:third]) + "<br>" +
                    " ".join(words[third:second_third]) + "<br>" +
                    " ".join(words[second_third:])
                )

            # Centered annotation using native Plotly rendering
            wrapped_title = wrap_text(col, max_chars_per_line=12)
            annotations.append(dict(
                x=x_center,
                y=y_center,
                text=f"<b>{wrapped_title}</b>",
                showarrow=False,
                xanchor='center',
                yanchor='middle',
                font=dict(size=16, family="'Anonymous Pro', monospace", color='black'),
                align='center'
            ))
            # Create big-dot bullet legend lines
            total = sum(values)
            legend_lines = [
                f"<span style='font-size:18px;color:{color_list[i]}'>●</span> {label} – {value / total * 100:.1f}%"
                for i, (label, value) in enumerate(zip(labels, values))
            ]
            legend_text = "<br>".join(legend_lines)

            # Place legend 16% below bottom of donut
            y_below = domain['y'][0] - 0.16

            annotations.append(dict(
                x=x_center,
                y=y_below,
                text=legend_text,
                showarrow=False,
                xanchor='center',
                yanchor='top',
                font=dict(size=14, family="'Anonymous Pro', monospace"),
                align='center'
            ))

   

        donut_fig.update_layout(
            showlegend=False,
            margin=dict(t=40, b=180, l=20, r=20),  # make room for legends
            height=580,
            annotations=annotations
        )


    # -- Build Filtered Table --
    # Show all columns from original dataset
    table_cols = [{'name': c, 'id': c} for c in df_full.columns]
    table_data = df_highlight.to_dict('records')

    # Row count label
    row_count_label = f"{subset_row_count} rows match current filters"

    # Build debug text
    debug_lines = []
    debug_lines.append(f"Reset button clicks: {reset_clicks}")
    debug_lines.append("Current Filter Selections:")
    for col in ALL_FILTERABLE_COLUMNS:
        sel = filter_values[col]
        if sel:
            debug_lines.append(f"  {col}: {sel}")
    debug_lines.append(f"Highlighted subset: {subset_row_count} of {total_row_count} rows")

    return (
        sankey_fig,
        donut_fig,
        "\n".join(debug_lines),
        table_data,
        table_cols,
        row_count_label
    )

@app.callback(
    Output('stage-labels-container', 'children'),
    Input('stage-selection', 'value')
)
def update_stage_labels(selected_stages):
    if not selected_stages:
        return []

    num_stages = len(selected_stages)
    if num_stages == 0:
        return []

    spacing_pct = 100 / (num_stages - 1) if num_stages > 1 else 0
    left_pad_px = 160

    labels = []
    for i, stage in enumerate(selected_stages):
        display_label = CUSTOM_STAGE_LABELS.get(stage, stage)
        left_percent = i * spacing_pct
        labels.append(
            html.Div(display_label, style={
                'position': 'absolute',
                'transform': 'translateX(-50%)',
                'left': f'calc({left_percent:.4f}% + {left_pad_px}px - {left_percent / 100 * left_pad_px * 2:.4f}px)',
                'top': '0',
                'width': '280px',
                'textAlign': 'center',
                'fontWeight': 'regular',
                'whiteSpace': 'normal',
                'overflowWrap': 'break-word',
                'fontFamily': "'Anonymous Pro', monospace",
                'fontSize': '16px',
                'pointerEvents': 'none'
            })
        )

    return html.Div(labels, style={
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'width': '100%',
        'zIndex': 1,
        'paddingTop': '64px',
        'paddingBottom': '16px'
    })

# ------------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------------
if __name__ == '__main__':
    if df_full.empty:
        print("ERROR: No data loaded. Check the CSV path:", CSV_FILE_PATH)
    else:
        print("Running app on http://127.0.0.1:8050")
        app.run_server(debug=True)

## ChatGPT (2025-04-08T23:07:30.165385+00:00)

Below is one way to solve the problem. The key is to always add the legend annotation even when your filtered series is empty (or has just one value). In the donut‐chart loop you need to “inject” dummy data when the value counts come back empty. This ensures that both the pie (even if it looks “empty”) and its legend annotation are always created. One common approach is to do the following in your loop over FILTER_COLUMNS:

1. Check if the value count (vc) is empty.
2. If it is, set the trace’s labels to \["No Data"\] and its values to a dummy value (for example, \[1\]).  
3. Also create a matching color (for example, a neutral light–gray) and legend line showing “No Data – 0.0%”.  
4. Otherwise, do your normal processing.

Below is the modified excerpt of your donut chart building code with these changes:

---

```python
# For each filter column, show a donut for the highlight subset distribution.
for idx, col in enumerate(FILTER_COLUMNS):
    if col not in df_highlight.columns:
        continue

    series = df_highlight[col]
    vc = series.value_counts()
    
    if vc.empty:
        # If there is no data for this donut, use dummy data so that the donut
        # (and importantly its legend) still render.
        labels = ["No Data"]
        # Use a dummy value to create a full (or empty) donut ring.
        values = [1]
        # Use a neutral/light-gray color for the "No Data" segment.
        color_list = ["#d3d3d3"]
        # Directly create a legend line indicating no data.
        legend_lines = [f"<span style='font-size:18px;color:#d3d3d3'>●</span> No Data – 0.0%"]
    else:
        vc_sorted = vc.sort_values(ascending=True)
        labels = vc_sorted.index.tolist()
        values = vc_sorted.values.tolist()
        color_list = [DONUT_COLORS[i % len(DONUT_COLORS)] for i in range(len(labels))]
        total = sum(values)
        legend_lines = [
            f"<span style='font-size:18px;color:{color_list[i]}'>●</span> {label} – {value / total * 100:.1f}%"
            for i, (label, value) in enumerate(zip(labels, values))
        ]
    
    # Add pie chart trace (donut)
    pie_trace = go.Pie(
        labels=labels,
        values=values,
        marker=dict(colors=color_list),
        hole=0.9,
        direction='clockwise',
        rotation=0,
        sort=False,
        textinfo='none',
        showlegend=False
    )
    donut_fig.add_trace(pie_trace, row=1, col=idx+1)

    # Extract the domain for calculating the center of the donut.
    trace_idx = len(donut_fig.data) - 1
    domain = donut_fig.data[trace_idx].domain
    x_center = (domain['x'][0] + domain['x'][1]) / 2
    y_center = (domain['y'][0] + domain['y'][1]) / 2

    # Prepare a wrapped centered title annotation for the donut.
    wrapped_title = wrap_text(col, max_chars_per_line=12)
    annotations.append(dict(
        x=x_center,
        y=y_center,
        text=f"<b>{wrapped_title}</b>",
        showarrow=False,
        xanchor='center',
        yanchor='middle',
        font=dict(size=16, family="'Anonymous Pro', monospace", color='black'),
        align='center'
    ))

    # Assemble the legend text from the legend lines.
    legend_text = "<br>".join(legend_lines)
    # Place the legend 16% below the donut’s bottom edge.
    y_below = domain['y'][0] - 0.16

    annotations.append(dict(
        x=x_center,
        y=y_below,
        text=legend_text,
        showarrow=False,
        xanchor='center',
        yanchor='top',
        font=dict(size=14, family="'Anonymous Pro', monospace"),
        align='center'
    ))
```

---

### Explanation

- **Always Building an Annotation:**  
  No matter how many segments are in the donut, you always add two annotations: one for the donut’s (wrapped) title at the center and one for the legend below it. This keeps your user interface consistent.

- **Handling an Empty Filtered Subset:**  
  When the filtered DataFrame for that column is empty, `series.value_counts()` yields an empty Series. In this case, by setting  
  - `labels = ["No Data"]`  
  - `values = [1]` (dummy value)  
  - `color_list = ["#d3d3d3"]` (a neutral color)  
  you guarantee that a pie trace is still added. Then, the legend annotation is built with a descriptive message showing “No Data – 0.0%”.  
 
- **Color and Percentage Calculation:**  
  When data is present, the color list and legend percentages are computed normally.  
 
- **Legend Positioning:**  
  The code places the legend at a y coordinate calculated as `domain['y'][0] - 0.16`, ensuring that even when the donut has few segments the legend is still 16% below the donut’s lower edge.

### Final Note

Be sure to integrate this patch into your overall callback logic. This approach respects the guardrails:
- The legend is never skipped.
- The donut chart is always rendered (even with a “dummy” donut), and
- All annotations remain synchronized with the donut chart.

This solution should meet your requirements and keep the donut legends visible regardless of how sparse the data becomes when filters are applied.

