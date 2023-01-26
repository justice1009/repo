import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np


st.set_page_config(layout="wide")


st.sidebar.header('🎈Menu')
name = st.sidebar.selectbox('KPI 실적', ['[Select]', '품질경영', "위기관리"])
# name2 = st.sidebar.selectbox('상세조회', ['[Select]', '고객 Painpoint 상세'])
# pd.set_option('display.max.colwidth', 800)

if name == '[Select]':

    st.subheader("■ 위기관리부문/ 품질경영팀")     
    def main() :    
        img = Image.open('qulity.png')
        st.image(img, width=650)
    if __name__ == "__main__" :
        main()

    def main() :    
        img = Image.open('qulity3.jpg')
        st.image(img, width=800)
    if __name__ == "__main__" :
        main()    

if name == '품질경영':
    st.subheader("■ KPI 실적 모니터링_품질")     
    option2 = st.selectbox(
    'What year would you like to view??',
    ('[연도 선택]','22년', '23년', '24년'))    

    option = st.selectbox(
    'What quarter would you like to view??',
    ('[분기 선택]','1분기', '2분기', '3분기', '4분기'))
    st.write('You selected:',  option2, option)
    
    if option2 == '22년':                
        if option == '3분기':
            def main() :    
                # pd.set_option('display.max.columns', 200)
                df= pd.read_excel("KPI2022.xlsx", sheet_name="3분기") # CSV 파일 불러오고 df 변수에 저장                        
                # # CSS to inject contained in a string
                # hide_table_row_index = """
                # <style>
                # thead tr th:first-child {display:none}
                # tbody th {display:none}
                # </style>
                # """
                # # Inject CSS with Markdown
                # st.markdown(hide_table_row_index, unsafe_allow_html=True)

                ds= df.fillna('')                            
                
                

                def draw_color_cell(x,color):
                    color = f'background-color:{color}'
                    return color
                
                ds= ds.style.applymap(draw_color_cell,color="#FFFAF0",subset=pd.IndexSlice[:,['22년 목표','3분기 실적','전년동기 대비']]).set_precision(2) 


                

                st.dataframe(ds, width=2500,height=420)     


                def convert_df(df):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return df.to_csv().encode('CP949')

                csv = convert_df(df)
                st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Painpoint_dx.csv',
                mime='text/csv')                                   

                st.success("🎈 KPI 실적 모니터링 결과가 조회되었습니다.")
                    

            if __name__ == '__main__' :
                main()  

        if option == '1분기':
            def main() :    
                # pd.set_option('display.max.columns', 200)
                df= pd.read_excel("KPI2022.xlsx", sheet_name="1분기") # CSV 파일 불러오고 df 변수에 저장        
                ds= df.fillna('')        
                # ds.set_index('Part', inplace=True)
                ds.style.set_properties(color="black", align="right")                  

                def draw_color_cell(x,color):
                    color = f'background-color:{color}'
                    return color
                
                ds= ds.style.applymap(draw_color_cell,color="#FFFAF0",subset=pd.IndexSlice[:,['22년 목표','1분기 실적','전년동기 대비']]).set_precision(2) 
                st.dataframe(ds, width=2500,height=420)     

                def convert_df(df):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return df.to_csv().encode('CP949')

                csv = convert_df(df)
                st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Painpoint_dx.csv',
                mime='text/csv')                                   

                st.success("🎈 KPI 실적 모니터링 결과가 조회되었습니다.")                   

            if __name__ == '__main__' :
                main()  

        if option == '2분기':
            def main() :    
                # pd.set_option('display.max.columns', 200)
                df= pd.read_excel("KPI2022.xlsx", sheet_name="2분기") # CSV 파일 불러오고 df 변수에 저장        
                ds= df.fillna('')        
                # ds.set_index('Part', inplace=True)
                ds.style.set_properties(color="black", align="right")                  

                def draw_color_cell(x,color):
                    color = f'background-color:{color}'
                    return color
                
                ds= ds.style.applymap(draw_color_cell,color="#FFFAF0",subset=pd.IndexSlice[:,['22년 목표','2분기 실적','전년동기 대비']]).set_precision(2) 
                st.dataframe(ds, width=2500,height=420)     

                def convert_df(df):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return df.to_csv().encode('CP949')

                csv = convert_df(df)
                st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Painpoint_dx.csv',
                mime='text/csv')                                   

                st.success("🎈 KPI 실적 모니터링 결과가 조회되었습니다.")                   

            if __name__ == '__main__' :
                main()  


        if option == '4분기':
            def main() :    
                # pd.set_option('display.max.columns', 200)
                df= pd.read_excel("KPI2022.xlsx", sheet_name="4분기") # CSV 파일 불러오고 df 변수에 저장        
                ds= df.fillna('')        
                # ds.set_index('Part', inplace=True)
                ds.style.set_properties(color="black", align="right")                  

                def draw_color_cell(x,color):
                    color = f'background-color:{color}'
                    return color
                
                ds= ds.style.applymap(draw_color_cell,color="#FFFAF0",subset=pd.IndexSlice[:,['22년 목표','4분기 실적', '전년동기 대비']]).set_precision(2) 
                st.dataframe(ds, width=2500,height=420)     

                def convert_df(df):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun
                    return df.to_csv().encode('CP949')

                csv = convert_df(df)
                st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Painpoint_dx.csv',
                mime='text/csv')                                   

                st.success("🎈 KPI 실적 모니터링 결과가 조회되었습니다.")                   

            if __name__ == '__main__' :
                main()  

