import streamlit as st
from streamlit_navigation_bar import st_navbar



#-------CSS------------------------

# setting the page configurations
st.set_page_config(page_title="RESOLUTE TASKS", page_icon="🖥️", layout="wide")


# changing the backgroung colour
# def MyBG_colour(wch_colour): 
#     my_colour = f"<style> .stApp {{background-color: {wch_colour};}} </style>"
#     st.markdown(my_colour, unsafe_allow_html=True)

# MyBG_colour("#E0F1FC")

# Changing the sidebar colour
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #2E3B4E;
    }
</style>
""", unsafe_allow_html=True)

# Remove the extra space from above
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0px;
                    padding-bottom: 5rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

# removing the top white coloured block
st.markdown("""
<style>
.st-emotion-cache-12fmjuu {
    height: 0rem;
}
.st-emotion-cache-h4xjwg {
            height: 0rem;
            }
.st-emotion-cache-1pbsqtx{
            color: rgb(0,0,0) }
.st-emotion-cache-mnu3yk{
           color: rgb(0,0,0) }
</style>
""",
unsafe_allow_html=True)

# Changing the font color in sidebar or selected and unselected
st.markdown("""
<style>
.st-emotion-cache-1rtdyuf { 
    color: rgb(240,240,240);
}
</style>
""",
unsafe_allow_html=True)

st.markdown("""
<style>
.st-emotion-cache-6tkfeg {     
    color: rgb(200,200,200);}
.st-emotion-cache-1f3w014{
        color: rgb(0,0,0);}


</style>
""",
unsafe_allow_html=True)

# Changing the heading in sidebar 
st.markdown("""
<style>
.st-emotion-cache-oq308l { 
    color: rgb(255,255,255);
    font-size: 28px;
    font-weight: bold;
}
</style>
""",
unsafe_allow_html=True)









#---------------CSS--------------------


sumarizer = st.Page("task5.py", title="5.Sumarizer", icon="🤏🏽")

QNA = st.Page("task6.py", title="6.Question & Answer", icon="📃")

basic = st.Page("task3.py", title="3.Basic Python", icon="📅")

classification = st.Page("task2.py", title="2.Classfier", icon="📥")

cluster = st.Page("task1.py", title="1.Cluster", icon="💹")


pg = st.navigation(
        {
            "COMPULSARY": [cluster,classification,basic],
            "OPTIONALS": [sumarizer,QNA],
        }

)

pg.run()
