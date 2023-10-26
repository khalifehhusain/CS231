# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
import os





def func1(s):
    
    st.write(s)
    dictD={
        'first column': [1, 2, 3, 4],
        'second column': [123, -20, 3, 24],
        'third column': [7 ,8 ,9, 10]}

    data=pd.DataFrame(dictD)
    st.write(data)


def button(line):
    button_list=[]
    
    col=line.split("  ")
    
    temp=col[0].split(":")
    

    col[0]=temp[1][9:]
    
    x=temp[0].split()
    st.write( "Cluster no  "+x[0][:-1]+" with ("+x[1]+") people")
    
    

    ele=col.pop()

    k=0
    while k<len(col):
    
      col_b = st.columns(3)
    
      for i in range(3):
          with col_b[i]:
              
                     
                 st.button(col[k])
                 button_list.append(col[k])
                 k+=1
                 if k>= len(col):
                     break
    return button_list


def cluster():
    bottom_list_all=[]
    url="http://moss.stanford.edu/results/6/7588194204467/match"
    
    
    
    file = open(r"C:\Users\Husain\Dropbox\dropox\231-Material\Moss\Moss_community_prc.txt","r")
    if file:
            i=0
            t="           "
            for line in file:
                if i==0:
                    
                    st.write(line)
                    i=1
                    
                elif line[0]=="#":
                    
                    
                    st.write(":red["+line+"]")
                    
                elif line[0].isdigit():
                    
                    
                    bottom_list_all=bottom_list_all+button(line)
                    txt = st.text_area(line[:6])
                    
                    
                elif line[0]=="-":
                    
                    st.write(line)
                    
                elif line[0].isalpha():
                    
                    x=line.split() 
                    st.markdown("["+x[-1]+": ]("+url+x[-1]+".html)"+x[0]+t+":green["+x[1]+"]"+x[2]+":green["+x[3]+"]"+":red["+x[4]+"]")
                    
            #print(f"{x[0]+t+x[1] : <40}{x[2]+t+x[3] : <40}{x[4] : >6}")
            
            
    file.close()
    return bottom_list_all
    
#bal=cluster()


def adj_list():
    ch=" "
    
    file = open(r"C:\Users\Husain\Dropbox\dropox\231-Material\Moss\adj_file.txt","r")
    

    if file:   
        for line in file:
            if line[0].isdigit() or line[0].isalpha() or line[0]=="-":
             
                 if line[0].isdigit():
                      st.write("-"*30)
                      x=line.split()
                      st.header(":green["+x[0]+"_ _"+x[1]+x[2]+x[3]+"]")
                      st.write("-"*30)
                 elif line[0]=="M":
                     
                     x=line.split()
        
                     st.write(x[0][5:]+":blue["+x[1]+"]"+x[2][5:]+":blue["+x[3]+"]"+":red["+x[4]+"]")
        file.close()


def buttons():
        col1,col2=st.columns(2)
        with col1:
            if st.button("Clusters"):
                cluster()
        with col2:
            if st.button("Adj List"):
                st.empty()
                adj_list()


# def file_upload():
    
 
#     st.title("Hello world!")

#     uploaded_file = st.file_uploader("Choose a file")
#     print(uploaded_file,type(uploaded_file))
#     if uploaded_file is not None:
#       df = pd.read_csv(uploaded_file)
#       st.write(df)

def iterate_tables():
     
  
            url="http://moss.stanford.edu/results/6/7588194204467/match"
            file=open(r"C:\Users\Husain\Dropbox\dropox\231-Material\Moss\Moss_community_prc.txt","r")
            # s=file.read()
            # print(type(s))
            # st.write(s)
            t="\t"
            for line in file:
                
                if line[0].isalpha():
                    x=line.split()
               
                    st.markdown("["+x[-1]+": ]("+url+x[-1]+".html)"+x[0]+t+x[1]+x[2]+x[3]+x[4])
                    
                    #print(f"{x[0]+t+x[1] : <40}{x[2]+t+x[3] : <40}{x[4] : >6}")
                else:
                    st.write(line)
       
    

def side_bar():
    
    sideb = st.sidebar
    if sideb.button("Clusters"):
        cluster()
        
    if sideb.button("Adj List"):
        adj_list()
    
    
    

side_bar()

# Create an empty container
# placeholder = st.empty()

# actual_email = "email1"
# actual_password = "password1"

# # Insert a form in the container
# with placeholder.form("login"):
#     st.markdown("#### Enter your credentials")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")
#     submit = st.form_submit_button("Login")

# if submit and email == actual_email and password == actual_password:
#     # If the form is submitted and the email and password are correct,
#     # clear the form/container and display a success message
#     placeholder.empty()
#     st.success("Login successful")
#     #-----------------------------------------------------------------------------
#     # try:
#     #         file=open("from-Moss.txt", "r")
#     #         iterate_tables(file)
#     # except:
#     #iterate_tables()
            
#     #func1("this is a test")
#     iterate_tables()

#     x = st.slider('x')  # 👈 this is a widget
#     st.write(x, 'squared is', x * x)

#     if st.checkbox('Show dataframe'):
#         chart_data = pd.DataFrame(
#            np.random.randn(20, 3),
#            columns=['a', 'b', 'c'])

#         chart_data

#     df = pd.DataFrame({
#         'first column': [1, 2, 3, 4],
#         'second column': [10, 20, 30, 40]
#         })

#     option = st.selectbox(
#         'Which number do you like best?',
#          df['first column'])

#     'You selected: ', option

#     add_selectbox = st.sidebar.selectbox(
#         'How would you like to be contacted?',
#         ('Email', 'Home phone', 'Mobile phone')
#     )

#     # Add a slider to the sidebar:
#     add_slider = st.sidebar.slider(
#         'Select a range of values',
#         0.0, 100.0, (25.0, 75.0)
#     )

#     left_column, right_column = st.columns(2)
#     # You can use a column just like st.sidebar:
#     left_column.button('Press me!')

#     # Or even better, call Streamlit functions inside a "with" block:
#     with right_column:
#         chosen = st.radio(
#             'Sorting hat',
#             ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#         st.write(f"You are in {chosen} house!")
        
#     st.radio("Pick one", ["cats", "dogs"])

#     st.write("check out this [link](http://moss.stanford.edu/results/2/2869761642973/")
#     #-------------------------------------------------------------------------------------
# elif submit and email != actual_email and password != actual_password:
#     st.error("Login failed")
# else:
#     pass