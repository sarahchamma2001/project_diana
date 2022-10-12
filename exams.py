import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from streamlit_option_menu import option_menu
import plotly.figure_factory as ff
import matplotlib.animation as animation

#Title
st.set_page_config(page_title='Students Performance on Exams',  layout='wide')

#header
t1, t2 = st.columns((0.4,1)) 
t2.title("Students Performance on Exams")


#### Creating Navigation Bar ####
#Hydralit Navbar
# define what option labels and icons to display
Menu = option_menu(None, ["Dataset",  "Dashboard"], 
    icons=['house', 'cloud-upload', "bar-chart-line","clipboard-check"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "purple"}})
# Dataset page

if Menu == "Dataset":
#data
# 2 Column Layouts of Same Size
    col4,col5 = st.columns([1,1])

    # First Column - Shows Description of EDA
    with col4:
        st.markdown("""
        <h3 class="f2 f1-m f-headline-l measure-narrow lh-title mv0">
         Know Your Data
         </h3>
         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;font-family: Sans Serif">
          This data set consists of the marks secured by the students in various subjects

Example Research Questions:

How effective is the test preparation course?

Which major factors contribute to test outcomes?

What would be the best way to improve student scores on each test?

What patterns and interactions in the data can you find? Let me know in the comments section below.
         </p>
            """,unsafe_allow_html = True)
        global eda_button
# Display customer churn animation
    with col5:
     df=pd.read_csv("exams.csv")
     st.dataframe(df)
# EDA page
df=pd.read_csv("exams.csv")
if Menu == "Dashboard":
  st.header("Visualizations")

#Visualization
  g1,g2,g3= st.columns((1,100,1))
  d1,d2,d3=st.columns((5, 1, 1))
  k1,k2,k3=st.columns((1, 1, 1))
  s1,s2=st.columns((1,1))
  w1,w2=st.columns((1,1))

  fig = px.histogram(df, x="parental level of education", y="math_score",
             color='gender', barmode='group', title= "Math Scores of the students depending on the level of education of the parents", height=400, color_discrete_sequence=px.colors.sequential.Agsunset)
  g2.plotly_chart(fig, use_container_width=True)
  g2.write("This bar chart shows that males are the ones with highest math scores compared to females. We can see a high difference on the scores of males and females with parents that went to high school or even got an associate’s degree. In other cases, the scores had only slight differences")
  
  fig2 = px.area(df, x="math_score", y="reading_score", color="race/ethnicity", line_group="test_preparation_course", title="Area Graph of the math and reading scores by race and by preparation of the course", color_discrete_sequence=px.colors.sequential.Agsunset)
  w1.plotly_chart(fig2, use_container_width=True)
  w1.write("This shows that students of group C who did not get prepared for the tests got the highest scores in both, math and reading.")

  score = r2.slider('Select the score', 66, 78)
  df1 = df[df["math_score"]==score]
  fig = px.sunburst(df1, path=['gender', 'race/ethnicity'], values='math_score',color_discrete_sequence=px.colors.sequential.Agsunset,
                  color='reading_score', hover_data=['parental level of education'], 
                  title="Chart of the reading and math scores of students depending on the parental level of education")
  
  w2.plotly_chart(fig, use_container_width=True)
  w2.write("Males and females of Group C got the highest scores in math but lowest scores in reading. In average, females scored better in reading than in math and males viceversa.")
  

  fig4 = px.ecdf(df, x="math_score", color="test_preparation_course",title= "Math scores depending on the test preparation of the course", color_discrete_sequence=px.colors.sequential.Agsunset)
  s1.plotly_chart(fig4, use_container_width=True)

  fig5 = px.ecdf(df, x="math_score", color="race/ethnicity", title="Line graph of the math scores depending on the race/ethnicity of the student", color_discrete_sequence=px.colors.sequential.Agsunset)
  s2.plotly_chart(fig5, use_container_width=True)

    
  d1.write("Choose the Pie Chart of the courses with the gender for the percentage:")
  math_score= d1.checkbox('math score')
  reading_score = d1.checkbox('reading score')
  writing_score = d1.checkbox('writing score')
   
  fig4=px.pie(df, values="math_score", names="gender", title='Math scores vs gender',color_discrete_sequence=px.colors.sequential.Agsunset)

  fig7 = px.pie(df, values="reading_score", names="gender", title='Reading scores vs gender', color_discrete_sequence=px.colors.sequential.Agsunset)

  fig6 = px.pie(df, values= "writing_score", names="gender", title='Writing scores vs gender', color_discrete_sequence=px.colors.sequential.Agsunset)
  if math_score:
        k1.plotly_chart(fig4, use_container_width=True)
  if reading_score:
        k2.plotly_chart(fig7, use_container_width=True)
  if writing_score:
        k3.plotly_chart(fig6, use_container_width=True)
