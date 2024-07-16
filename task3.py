import streamlit as st
import pandas as pd

st.header(":blue[Python Basics] ",divider='blue')

file = st.file_uploader("Please upload the dataframe : ",type="xlsx",accept_multiple_files=False)

if file:

    df = pd.read_excel(file)
    st.write("Your dataframe is : ")
    st.write(df)


    df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
    df['position'] = df['position'].str.lower()
    
    df = df.sort_values(by='datetime')
    
    ## Total Duration
    
    df['time_diff'] = df['datetime'].diff()
    df['duration'] = df['time_diff'].shift(-1).fillna(pd.Timedelta(seconds=0))
    
    inside_df = df[df['position'] == 'inside']
    outside_df = df[df['position'] == 'outside']
    
    inside_duration = inside_df.groupby(df['datetime'].dt.date)['duration'].sum()
    outside_duration = outside_df.groupby(df['datetime'].dt.date)['duration'].sum()
    
    result_df = pd.DataFrame({
        'date': inside_duration.index,
        'inside_duration': inside_duration.values,
        'outside_duration': outside_duration.reindex(inside_duration.index, fill_value=pd.Timedelta(seconds=0)).values
    })
    st.write("##### Datewise total duration for each inside and outside.")
    st.write("streamlit.dataframe does not display exact time for example (for 1 day 8 hours it shows a day)")
    st.dataframe(result_df.head())

    ## No. of Placing and picking
    activity_counts = df.groupby(['date', 'activity']).size().reset_index(name='count')
    
    pivot_table = activity_counts.pivot(index='date', columns='activity', values='count').fillna(0)
    
    pivot_table.columns = ['number_of_picked', 'number_of_placed']
    
    result_df = pivot_table.reset_index()
    
    st.write("##### Datewise number of picking and placing activity done.")
    st.write(result_df)