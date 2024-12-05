import streamlit as st
import plotly.express as px 

st.set_page_config(

    layout="wide" ,
    page_title= "frist_dash_board"
)
df = px.data.tips()

## to creat the side bar
x=st.sidebar.checkbox("Show Data" , False , key=1) ## the False here mean i make the square behind the "Show Data" without check mark



day =st.sidebar.selectbox("select day", df['day'].unique()) ## selectbox here like drop down minue and the name of it selectday
# and the df['day'].unique ==> to make the data unique in the drop minue 


time= st.sidebar.selectbox('Select Meal Time', df['time'].unique()) ## also like the above one 

size = st.sidebar.radio("size", sorted(df['size'].unique()) , 5 , horizontal=True )

if  x :   ## ===>> here mean if x mean if i put on x on the dashboard or put check mark # so this one it depends on the first thing
    # that i make it from above in the x variable 
    st.header("Dataset at the dash board")
    st.dataframe(df.head(8))


## any page in streamlit can be divided into columns 

col1 , col2 , col3 = st.columns([5,2,5])

with col1 :   ## mean inside col1
    new_df1 = df[df['day'] == day] ### so here in this one , it when click on the day he want it will appear the data of 
    #of that day  in the histogram down 

    
    fig = px.histogram(new_df1, x = 'total_bill', color = 'sex',
                       title=f'totalt bill for {day}day'.title(), width = 700)

    
    st.plotly_chart(fig,use_container_width=True) ### is a function inside plotly to turn on the figures on streamlit 
    new_df1 = df[df['size'] == size]
    fig = px.pie(new_df1, names = 'time', color = 'sex',
                 title=f'count of each meal time according to {size} dishes'.title()).update_traces(textinfo='value')
    st.plotly_chart(fig,use_container_width=True)

with col3 : 
    new_df2 = df[df['time']==time]
    fig2= px.scatter(new_df2, x ="total_bill", y ="tip",template="presentation",title=f'correlation between total bill and tip on {time}')
    st.plotly_chart(fig2 , use_container_width=True)
