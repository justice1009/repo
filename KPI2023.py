import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np


st.set_page_config(layout="wide")


st.sidebar.header('🎈Menu')
name = st.sidebar.selectbox('KPI 실적', ['[Select]', '품질경영', "위기관리"])
# name2 = st.sidebar.selectbox('상세조회', ['[Select]', '고객 Painpoint 상세'])
pd.set_option('display.max.colwidth', 1000)

if name == '품질경영':

    st.subheader("■ KPI 실적 모니터링_품질")     
    def main() :    
        # pd.set_option('display.max.columns', 200)
        df= pd.read_excel("KPI2022.xls", sheet_name="KPI실적모니터링") # CSV 파일 불러오고 df 변수에 저장        
        ds= df.fillna('')        
        # ds.set_index('Part', inplace=True)
        ds.style.set_properties(color="black", align="right")  
        

        def draw_color_cell(x,color):
            color = f'background-color:{color}'
            return color

        
        ds= ds.style.applymap(draw_color_cell,color="#FFFAF0",subset=pd.IndexSlice[:,['3분기 목표','21년 3분기 누계 실적']]).set_precision(2) 

        st.dataframe(ds, width=2500,height=500)     


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
