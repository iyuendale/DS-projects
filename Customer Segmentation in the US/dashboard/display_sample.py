from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash
import plotly.graph_objects as go
import numpy as np
import random






app = Dash(external_stylesheets= [dbc.themes.FLATLY])

# app.layout = html.Div()
# app.layout = dbc.Container(html.P("My awesome dashboard will be here.",
#                                   style= {"color": "#010103"}),
#                            fluid= True,
#                            className= "dashboard-container",
#                            style= {
#                                "background-color": "#ffffff",
#                                "border-color": "#010103"
#                            }
#                           )


# graph
fig = go.Figure(
    go.Scattergl(x= np.random.randn(1000),
                 y= np.random.randn(1000),
                 mode= "markers",
                 marker= dict(
                     color= random.sample(["#ecf0f1"] * 500 +
                                          ["#3498db"] * 500, 1000),
                     line_width= 1)
                ))

fig.update_layout(plot_bgcolor= "#010103",
                  width= 790,
                  height= 730,
                  xaxis_visible= False,
                  yaxis_visible= False,
                  showlegend= False,
                  margin= dict(l= 0, r= 0, t= 0, b= 0))

app.layout = dbc.Container([
    html.Div(
        [
            # The "welcome" and description container
            html.Div([
                html.H1([
                    html.Span("Welcome"),
                    html.Br(),
                    html.Span("to my beautiful dashboard!")
                ]),
                html.P("This dashboard prototype shows how to create an effective layout.")
            ],
                style= {
                    "vertical-alignment": "top",
                    "height": 260
                }),
            # the buttons container
            html.Div([
                # Graph and Table buttons
                html.Div(dbc.RadioItems(
                    className= "btn-group",
                    inputClassName= "btn-check",
                    labelClassName= "btn btn-outline-light",
                    labelCheckedClassName= "btn btn-light",
                    options= [
                        {"label": "Graph", "value": 1},
                        {"label": "Table", "value": 2}
                    ],
                    value= 1,
                    style= {"width": "100%"},
                ),
                    style= {"width": 206}),
                # About button
                html.Div(dbc.Button(
                    "About",
                    className= "btn btn-info",
                    n_clicks= 0
                ),
                    style= {"width": 104})
            ],
            style= {
                "margin-left": 15,
                "margin-right": 15,
                "display": "flex"
            }),
            # a group of three dropdowns
            html.Div([
                html.Div([html.H2("Unclearable Dropdown:"),
                          dcc.Dropdown(
                              options= [
                                  {"label": "Option A", "value": 1},
                                  {"label": "Option B", "value": 2},
                                  {"label": "Option C", "value": 3},
                              ],
                              value= 1,
                              clearable= False,
                              optionHeight= 40,
                              className= "customDropdown"
                          )]),
                html.Div([html.H2("Unclearable Dropdown:"),
                          dcc.Dropdown(
                              options= [
                                  {"label": "Option A", "value": 1},
                                  {"label": "Option B", "value": 2},
                                  {"label": "Option C", "value": 3},
                              ],
                              value= 2,
                              clearable= False,
                              optionHeight= 40,
                              className= "customDropdown"
                          )]),
                html.Div([html.H2("Clearable Dropdown:"),
                          dcc.Dropdown(
                              options= [
                                  {"label": "Option A", "value": 1},
                                  {"label": "Option B", "value": 2},
                                  {"label": "Option C", "value": 3},
                              ],
                              clearable= True,
                              optionHeight= 40,
                              className= "customDropdown"
                          )])
            ],
                style= {
                    "margin-left": 15,
                    "margin-right": 15,
                    "margin-top": 30
                }),
            # image
            html.Div(
                html.Img(src= "assets/R.jfif",
                    style= {
                        "margin-left": 15,
                        "margin-right": 15,
                        "margin-top": 30,
                        "width": 310,
                        "height": 200
                    })
            ),
        ],
        style= {
            "width": 340,   ###
            "margin-left": 35,
            "margin-top": 35,
            "margin-bottom": 35
        }),

    # second container
    html.Div(
        [
            # graph
            html.Div(dcc.Graph(figure= fig), style= {"width": 790}),
            # output
            html.Div([
                html.H2("Output 1:"),
                html.Div(className= "Output"),
                html.H2("Output 2:"),
                html.Div(html.H3("Selected Values"), className= "Output")
            ],
                style= {"width": 200}),
        ],
        style= {
            "width": 990,
            "margin-right": 35,
            "margin-top": 35,
            "margin-bottom": 35,
            "display": "flex"
        })
],
   fluid= True,
   className= "dashboard-container",
   style= {"display": "flex"}
)