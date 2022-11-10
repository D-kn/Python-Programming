# Librairies importations
import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
from graphics import *


def exp_data_analysis(df):
    cols = df.columns.to_list()
    select_cols = st.sidebar.multiselect('Choose Columns :', cols, cols)
    out = df[select_cols]
    
    # Showing our dataset with AgGrid
    gb = GridOptionsBuilder.from_dataframe(out)
    gb.configure_pagination(enabled=True)
    gb.configure_default_column(editable=True, groupable=True)
    # with st.expander('Data view'):
    st.write('''### Data view''')
    select_mode = st.radio(label='Selection Type', options=['single', 'multiple'])
    c1, _ = st.columns([1, 2])
    select_theme = c1.selectbox(label='Theme', options=['streamlit', 'light', 'dark', 'blue', 'fresh', 'material'])
   
    gb.configure_selection(selection_mode=select_mode, use_checkbox=True)
    gridOptions = gb.build()
    grid_table = AgGrid(
        out,
        gridOptions=gridOptions, 
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        reload_data=True,
        enable_enterprise_modules=True,
        height=350, 
        width='100%',
        data_return_mode='AS_INPUT', 
        allow_unsafe_jscode=True, 
        theme=select_theme
    )

    selected = grid_table["selected_rows"]
    data = pd.DataFrame(selected) 
   
    if len(data) != 0: 
        st.write(''' ##### Filtered Dataframe ''')  
        st.dataframe(data) 
    else: pass
        

    
    # grouping variable by categories
    num_df, cat_df = out.select_dtypes(exclude='object'), out.select_dtypes(include='object')
    num_cols, cat_cols = num_df.columns.to_list(), cat_df.columns.to_list()

    target = st.sidebar.selectbox('Target variable :', num_cols)
    viz_list =  ['Numerical Variables', 'Categorical Distribution', 'Correlation with target']
    viz_type = st.sidebar.selectbox('visualization type :', viz_list)
    st.write('---')


    # Data exploratory
    with st.expander('Data visualization'):
        c1, c2 = st.columns([2, 2])
        # Numerical variable
        if viz_type == viz_list[0]:
            all_plot = st.sidebar.checkbox('Plots all figures') # Plots all figures
            var1 = c1.selectbox('Select variable : ', num_cols)
            espace_below(c2)
            corr_with=c2.checkbox('Visusalize with another variable')
            if corr_with:
                var2 = c1.selectbox('Select x-axis variable :', out.columns.to_list())
                if var2 in out.select_dtypes(exclude='object').columns:
                    scatter(out, var1, var2)
                    st.write('---')
                else: 
                    _func = c2.checkbox('Display based on', help='Choose a variable to Visualize according to')
                    hue=None
                    if _func:
                        hue=c2.selectbox('Choose variable :  ', [k for k in cat_cols if k is not var1])
                    box_plot(out, var1, var2, hue=hue)
            else: 
                if all_plot:
                    for num_col in num_cols:
                        hist_plot(num_df, num_col)
                        st.write('---')
                        box_plot(num_df, num_col, None, None)
                else:
                    st.write(f"Histogram of '{var1}'")
                    hist_plot(num_df, var1)
                    box_plot(num_df, var1, None, None)

        if viz_type == viz_list[1]:
            all_plot = st.sidebar.checkbox('Plots all distributions')
            espace_below(st)
            if all_plot:
                st.write('''#### Bar Plots''')
                for cat_col in cat_cols:
                    hist_plot(cat_df, cat_col)
                    st.write('---')
                    pie_chart(cat_df, cat_col)
            else:
                var = c1.selectbox('Select variable (to show on x-axis) ', cat_cols)
                st.write('''#### Bar Plots''')
                hist_plot(cat_df, var)
                st.write('---')
                st.write('''#### Pie Chats ''')
                pie_chart(cat_df, var)
        # Correlation with target variable
        if viz_type == viz_list[2]:
            target_corr(num_df, target)
            st.write('----')
            st.write('Correlation Matrix')
            correlation_matrix(num_df)
        else: pass

    with st.expander('Mulvariate analysis'):
        c1, c2 = st.columns([1, 1])
        mono = c2.selectbox('Select x-axis variable : ', num_cols)
        num_cols_without_mono = [col for col in num_cols if col != mono]
        multi = c1.multiselect('Select variables on y-axis: ', num_cols_without_mono, num_cols_without_mono[:4], help='Select one or more')
        multi_num(num_df, mono, multi)

    with st.expander('Correlation visualtions'):
        st.write('Correlation')

    with st.expander('Regression visualisations'):
        st.write('Regression')
    