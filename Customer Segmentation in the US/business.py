# libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# import data
df = pd.read_csv("SCFP2022.csv")

# creadit fearful group
df_cred_fear = df[df["TURNFEAR"] == 1]

## explore data
# Age
def get_age(normalize):
    age_dict = {
        1: "Under 35",
        2: "35 - 44",
        3: "45 - 54",
        4: "55 - 64",
        5: "65 - 74",
        6: "75 or Above"
    }
    
    age_df = (
        df["AGECL"]
        .groupby(df["TURNFEAR"]).value_counts(bool(normalize)).rename("count")
        .to_frame().reset_index())
    
    fig = px.bar(
        x= age_df["AGECL"], y= age_df["count"], color= age_df["TURNFEAR"].astype(str), barmode= "group",
        title= "Distribution of Ages"
    )
    
    legends = {"0": "False", "1": "True"}
    fig.for_each_trace(lambda t: t.update(name = legends[t.name],
                                      legendgroup = legends[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, legends[t.name])
                                     )
                  )
    fig.update_layout(
        xaxis = {"tickvals": list(age_dict.keys()), "ticktext": list(age_dict.values()), "title": "Age"},
        width= 790,
        height= 730,
        yaxis_title= "Frequency",
        legend_title= "Credit Fearful"
    )
    
    return fig

# Race
def get_race(normalize):
    race_dict = {
        1: "white non-Hispanic",
        2: "black / African American",
        3: "Hispanic",
        4: "Asian American / Pacific Islander",
        5: "Other"
    }
    # if flag == 1:
    #     race_cat = df["RACE"].replace(race_dict)
    # else:
    #     race_cat = df_cred_fear["RACE"].replace(race_dict)

    # race_counts = race_cat.value_counts(normalize= 1)
    # fig = px.bar(
    #     x= race_counts.index,
    #     y= race_counts,
    #     title= "Distribution of Race"
    # )
    # # fig.update(xaxis_title= "Ages")

    # fig.update_layout(
    #     width= 790,
    #     height= 730,
    #     xaxis_title= "Race",
    #     yaxis_title= "Frequency [count]",
    #     showlegend= False,
    #     # margin= dict(l= 5, r= 5, t= 0, b= 0)
    # )
    race_df = (
        df["RACE"].groupby(df["TURNFEAR"])
        .value_counts(normalize= bool(normalize)).rename("freq").to_frame().reset_index())
    fig = px.bar(
        x= race_df["RACE"], y= race_df["freq"], color= race_df["TURNFEAR"].astype(str), barmode= "group",
        title= "Distribution of Race"
    )

    legends = {"0": "False", "1": "True"}
    fig.for_each_trace(lambda t: t.update(name = legends[t.name],
                                          legendgroup = legends[t.name],
                                          hovertemplate = t.hovertemplate.replace(t.name, legends[t.name])
                                         )
                      )
    fig.update_layout(
        xaxis = {
            "tickvals": list(race_dict.keys()), "ticktext": list(race_dict.values()), "title": "Age",
            "tickangle": 30},
        yaxis_title= "Frequency",
        legend_title= "Credit Fearful"
    )
    
    return fig

# Income
def get_income(normalize):
    income_cat = {
        1: "0 - 20",
        2: "20 - 39.9",
        3: "40 - 59.9",
        4: "60 - 79.9",
        5: "80 - 89.9",
        6: "90 - 100"
    }

    # if flag== 1
    inc_df = (
        df["INCCAT"].groupby(df["TURNFEAR"]).value_counts(normalize= bool(normalize))
        .rename("freq").to_frame().reset_index()
    )

    fig = px.bar(
        x = inc_df["INCCAT"], y = inc_df["freq"], color= inc_df["TURNFEAR"].astype(str), barmode= "group",
        title= "Distribution of Income"
    )

    legends = {"0": "False", "1": "True"}
    fig.for_each_trace(lambda t: t.update(name= legends[t.name],
                                          legendgroup= legends[t.name],
                                          hovertemplate= t.hovertemplate.replace(t.name, legends[t.name])                                         ))
    
    fig.update_layout(
        xaxis= {"tickvals": list(income_cat.keys()), "ticktext": list(income_cat.values()), "title": "Income"},
        yaxis_title= "Frequency", legend_title= "Credit Fearful"
    )
    return fig

# Education
def get_educ(normalize):
    edu_df = (
        df["EDUC"]
        .groupby(df["TURNFEAR"])
        .value_counts(normalize= bool(normalize))
        .rename("freq")
        .to_frame()
        .reset_index()
    )

    fig = px.bar(
        x = edu_df["EDUC"], y = edu_df["freq"], color= edu_df["TURNFEAR"].astype(str), barmode= "group",
        title= "Distribution of Education Levels"
    )
    legends = {"0": "False", "1": "True"}
    fig.for_each_trace(lambda t: t.update(name= legends[t.name],
                                          legendgroup= legends[t.name],
                                          hovertemplate= t.hovertemplate.replace(t.name, legends[t.name])
                                         ))
    fig.update_layout(
        xaxis_title= "Education levels", yaxis_title= "Frequency", legend_title= "Credit Fearful"
    )
    return fig
    