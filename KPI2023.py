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

    
    # st.subheader("")     
    # st.subheader("[LG 생활건강 8대 품질 지침]")     
    # st.markdown("  ■ 소비자들이 안심할 수 있는 품질의 제품만을 연구하고, 구매하고, 만들어, 출하합니다.")
    # st.markdown("  ■ 모든 제품의 품질 기준은 고객관점에서 결정되어야 하고, 예상 리스크를 철저하게 점검 및 개선해야 합니다.")
    # st.markdown("  ■ 내부 관리 기준에 적합하지 않은 제품은 Release를 보류하고, 원인 분석 및 개선 조치 후 다음 프로세스를 진행합니다.") 
    # st.markdown("  ■ 제품 설계시 기본 프로세스를 준수하지 않는 임의 개발일정 단축 및 검증시험 Skip은 금지합니다.") 
    # st.markdown("  ■ 양산시 승인된 원부자재만을 사용하고, 처방 및 검사항목의 신뢰성을 확보 후 합격 판정합니다.") 
    # st.markdown("  ■ 원료 및 제품 보관시 특성에 맞는 적정한 환경에서 보관되고, 선입선출이 이루어지도록 관리합니다.") 
    # st.markdown("  ■ 자사 및 협력회사의 4M 등 중요 변경사항은 반드시 품질 Risk를 확인하고 검증하여야 합니다.")
    # st.markdown("  ■ 시장에서 발생하는 고객불만 등 Issue 사항은 반드시 검사항목과 연계하여 관리되어야 하며, 근본 개선 대책을 철저히 수립, 실행하고, 재발여부를 지속 모니터링 해야 합니다.") 

if name == '품질경영':
    st.subheader("■ KPI 실적 모니터링_품질")     

    col1, col2 = st.columns(2)

    with col1:
        option2 = st.selectbox(
        '- What year would you like to view??',
        ('[연도 선택]','22년', '23년', '24년'))    
    with col2:
        option = st.selectbox(
        '- What quarter would you like to view??',
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

