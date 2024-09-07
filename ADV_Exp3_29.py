import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

# Load dataset
data = pd.read_csv('C:\\Users\\deepr\\OneDrive\\COLLEGE\\SEM-07\\ADV\\Exp03\\covid_19_data.csv')
df = data.dropna(subset=['Province/State'])

# Ensure 'Recovered' has non-negative values
df['Recovered'] = df['Recovered'].apply(lambda x: x if x > 0 else 0)


st.sidebar.title("Filter")
country = st.sidebar.multiselect("Select Country", options=df["Country/Region"].unique())
province = st.sidebar.multiselect("Select Province/State", options=df["Province/State"].unique())

# Input of user selection
if country:
    df = df[df["Country/Region"].isin(country)]
if province:
    df = df[df["Province/State"].isin(province)]

# Basic Visualizations
st.subheader("Basic Charts")

# Bar chart
st.write("### Bar Chart")
bar_chart = px.bar(df, x='Province/State', y='Confirmed', title="Bar Chart of Confirmed Cases")
st.plotly_chart(bar_chart)

# Pie chart 
st.write("### Pie Chart")
pie_chart = px.pie(df, values='Deaths', names='Country/Region', title="Deaths by Country/Region")
st.plotly_chart(pie_chart)

# Histogram 
st.write("### Histogram")
histogram = px.histogram(df, x='Confirmed', nbins=10, title="Distribution of Confirmed Cases")
st.plotly_chart(histogram)

# Scatter plot 
st.write("### Scatter Plot")
scatter = px.scatter(df, x='Confirmed', y='Deaths', color='Country/Region', title="Scatter Plot of Confirmed vs Deaths")
st.plotly_chart(scatter)

# Timeline Chart 
st.write("### Timeline Chart")
timeline = px.line(df, x='ObservationDate', y='Confirmed', title="Timeline of Confirmed Cases")
st.plotly_chart(timeline)

# Bubble plot
st.write("### Bubble Plot")
bubble_plot = px.scatter(df,x='Confirmed',y='Deaths',size='Recovered',color='Country/Region',title="Bubble Plot of Cases",hover_name='Country/Region',log_x=True, size_max=60 )

# Display the plot
st.plotly_chart(bubble_plot)



# Advanced Visualizations
st.subheader("Advanced Charts")

df['Country/Province'] = df['Country/Region'] + " / " + df['Province/State']

# Treemap
word_chart = px.treemap(df, path=['Country/Region', 'Province/State'], values='Confirmed', title="Confirmed Cases by Province/State")
st.plotly_chart(word_chart)

# Box and Whisker Plot 
st.write("### Box and Whisker Plot")
box_plot = px.box(df, x="Country/Region", y="Confirmed", title="Confirmed Cases per Country")
st.plotly_chart(box_plot)

# Violin Plot 
st.write("### Violin Plot")
violin_plot = px.violin(df, x="Country/Region", y="Confirmed", title="Confirmed vs Deaths")
st.plotly_chart(violin_plot)

# 3D Plot - Confirmed, Deaths, and Recovered
st.write("### 3D Chart")
chart_3d = px.scatter_3d(df, x='Confirmed', y='Deaths', z='Recovered', color='Country/Region', title="3D Chart of Cases")
st.plotly_chart(chart_3d)

# Line Plot
st.write("### Line Chart")
line_chart = px.line(df, x="ObservationDate", y="Confirmed", title="Confirmed Cases Over Time")
st.plotly_chart(line_chart)

# Waterfall Plot
st.write("### Waterfall Chart")
waterfall = px.bar(df, x='Province/State', y='Confirmed', title="Waterfall Chart of Confirmed Cases")
st.plotly_chart(waterfall)