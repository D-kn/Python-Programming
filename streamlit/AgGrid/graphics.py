import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np



def hist_plot(df, selected_col):
    if len(df)==0:
        st.write('No graphic to show.')
    else:
        if selected_col in df.select_dtypes(exclude='object').columns:
            fig = px.histogram(df, x=selected_col)
        else:
            fig = px.histogram(df, x=selected_col).update_xaxes(categoryorder='total ascending')
            fig.update_xaxes(tickangle=-45)
            fig.update_yaxes(title='Number of elements')
        st.plotly_chart(fig)

def scatter(df, var1, var2):
    fig = px.scatter(df, x=var2, y=var1) 
    st.plotly_chart(fig)

def box_plot(df, var1, var2, hue):
    if not var2 is None:
        fig = px.box(df, x=var2, y=var1, color=hue)
    else:
        fig = px.box(df, y=var1)
    st.plotly_chart(fig)

def pie_chart(df, var):
    fig = px.pie(df, var)
    st.plotly_chart(fig)

def target_corr1(df, target):
    _, m = df.shape
    for i in range(0, m, 4):
        fig = px.scatter_matrix(data=df,
                            x_vars=df.columns[i:i+4],
                            y_vars=target)
        st.plotly_chart(fig)

# def target_corr(df, target):
#     data = df.drop(target, axis=1)
#     _, m = df.shape
#     st.write(f'''##### Correlation of with "{target}" numerical variables ''')
#     for i in range(0, m, 5):
#         # fig = plt.figure(figsize=(12, 8))
#         fig = sns.pairplot(data=df,
#                     x_vars=data.columns[i:i+5],
#                     y_vars=target)
#         st.pyplot(fig)


def target_corr(df, target):
    data = df.drop(target, axis=1)
    _, m = df.shape
    st.write(f'''##### Correlation of with "{target}" numerical variables ''')
    for i in range(0, m, 5):
        # fig = plt.figure(figsize=(12, 8))
        fig = sns.pairplot(data=df,
                    x_vars=data.columns[i:i+5],
                    y_vars=target)
        st.pyplot(fig)


# Correlation with the target variable
def target_corr(df, target):
    data = df.drop(target, axis=1)
    _, m = df.shape
    st.write(f'''##### Correlation with '{target}' numerical variables ''')
    for i in range(0, m, 3):
        plt.figure(figsize=(8, 6))
        fig = sns.pairplot(data=df,
                    x_vars=data.columns[i:i+3],
                    y_vars=target)
        st.pyplot(fig)


def correlation_matrix(df):
    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(14, 8))
        sns.color_palette("Paired")
        ax = sns.heatmap(corr, mask=mask, vmax=1, vmin=-1, annot=True)
        st.pyplot(f, ax)

def multi_num(df, x, Y):
    '''
    -Y : a list of numerical variables
    -x : numerical variable to plot on x-axis
    '''
    fig = px.scatter(df, x=x, y=Y)
    st.plotly_chart(fig)
    


def espace_below(c):
    c.write('''####''')

