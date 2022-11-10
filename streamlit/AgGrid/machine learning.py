# Librairies importations
import gc
# gc.collect()
from EDA import * 
from st_viz_types import * 


def main():
    # file uploading
    st.sidebar.info('Upload a file 👇')
    data = st.sidebar.file_uploader(label=' ', type='xlsx')

    if not data is None:
        st.cache(suppress_st_warning=False)
        def upload_file():
            df = pd.read_excel(data)
            return df

        df = upload_file()

        menu = ['EDA', 'Pandas Profiling (Automatic Viz)', 'Machine Learning', 'About']
        menu_ = st.sidebar.selectbox('Menu', menu, help="'Pandas Profiling' is an automatic Visualization")
        if menu_ == menu[0]:
            exp_data_analysis(df)
        elif menu_ == menu[1]:
            if st.button('Generate the report'):
                data_profiling(df)
        elif menu == menu[2]:
            st.write('Machine Learning')
        else: 
            st.write(''' ### About ''')


if __name__ == '__main__':
    main()


