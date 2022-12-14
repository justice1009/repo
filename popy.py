import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np


st.set_page_config(layout="wide")


st.sidebar.header('๐Menu')
name = st.sidebar.selectbox('KPI ์ค์ ', ['[Select]', '๊ณ ๊ฐ Painpoint ์ค์ ', "์์ฌํ์ง์ง์"])
name2 = st.sidebar.selectbox('์์ธ์กฐํ', ['[Select]', '๊ณ ๊ฐ Painpoint ์์ธ'])

# st.sidebar.subheader('๊ณ ๊ฐ๊ฐ์นํ์ ๋ถ๋ฌธ/')
# st.sidebar.subheader('ํ์ง๊ฒฝ์ํ')

if name == '๊ณ ๊ฐ Painpoint ์ค์ ':
    st.subheader("์์/๋ถ๋ฌธ์ฅ KPI ๊ฒฐ๊ณผ")
    st.text("โ  ๊ณ ๊ฐ Painpoint ์ค์  ์กฐํ")

    input_user_name = st.text_input(label="User Password", value="")
    st.caption("*User์ ์ฃผ๋ฏผ๋ฑ๋ก๋ฒํธ ๋ท4์๋ฆฌ๋ฅผ ์๋ ฅํด์ฃผ์ญ์์ค")

    checkbox = st.checkbox('agree')
    btn_clicked = st.button("Confirm", key='confirm_btn', disabled=(checkbox is False))             

    if btn_clicked:
        con = st.container()
        con.caption("Result")
        if not str(input_user_name):
            con.error("Input your ID please~")
        else:
            con.write(f"Hello~ {str(input_user_name)}๋์ KPI ์ค์ ์ ๊ณต์ ๋๋ฆฝ๋๋ค")
        
        st.text("โ  ๋นํด๋๋ ๊ณ ๊ฐ Painpoint ์ค์ ")

        def main() :    
            df= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="2023_Painpoint_KPI") # CSV ํ์ผ ๋ถ๋ฌ์ค๊ณ  df ๋ณ์์ ์ ์ฅ
            df.set_index('Name', inplace=True)
            ds= df[df["Password"].astype(str).str.contains(input_user_name, case=True, na=False)]
            

            def draw_color_cell(x,color):
                color = f'background-color:{color}'
                return color
 
            
            ds= ds.style.applymap(draw_color_cell,color="#ffccff",subset=pd.IndexSlice[:,[' PPM(22๋) ']]).set_precision(2) 
            # ds= df.style.set_precision(2) 
            #8cffaa
            st.dataframe(ds, width=2500,height=20)     
            

        if __name__ == '__main__' :
            main()  

        st.text("โ  ์ ๋๋ ๊ณ ๊ฐ Painpoint ์ค์ ")

        def main() :    
            df2= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="2022") # CSV ํ์ผ ๋ถ๋ฌ์ค๊ณ  df ๋ณ์์ ์ ์ฅ
            df2.set_index('Name', inplace=True)
            ds2= df2[df2["Password"].astype(str).str.contains(input_user_name, case=True, na=False)]
            # da= ds.style.hide_index()

            def draw_color_cell(x,color):
                color = f'background-color:{color}'
                return color
 
            
            ds2= ds2.style.applymap(draw_color_cell,color='#fff0f5',subset=pd.IndexSlice[:,[' PPM(21๋) ']]).set_precision(2) 
            #์์๊ณผ ์์ซ์  ์ ์ฉ

            st.dataframe(ds2, width=2500,height=20)                        

            
        if __name__ == '__main__' :
            main()

        st.success("Success")

    if name2 == '๊ณ ๊ฐ Painpoint ์์ธ':        
        st.markdown("##### ๊ณ ๊ฐ Painpoint ์์ธ ๋ด์ญ")
        st.text("โ  ์กฐํ ๊ฒฐ๊ณผ")
        
        dfx= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="2023_Painpoint_KPI") # CSV ํ์ผ ๋ถ๋ฌ์ค๊ณ  df ๋ณ์์ ์ ์ฅ
        # df.set_index('Name', inplace=True)              

        
        # Password์์ Name ๊ฐ๊ณ  ์ค๊ธฐ ex)1001-> ์ดํ์ 
        ds= dfx["Name"][dfx["Password"].astype(str).str.contains(input_user_name, case=True, na=False)]
        dspp= ds.iloc[0] #ds๋ series์ ๊ทธ๋์ ๊ฐ์ ๊ฐ๊ณ  ์์ผํจ. 
        # dspp

        dfs= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="22PP_Detail")            
        dfx= dfs.astype(str)
                    

        dx = dfx[(dfx["์ฌ์๋ถ์ฅ"]==dspp)|(dfx["๋ง์ผํ1"]==dspp)|(dfx["๋ง์ผํ2"]==dspp)|(dfx["๋ง์ผํ3"]==dspp)|
        (dfx["R&D1"]==dspp)|(dfx["R&D2"]==dspp)|(dfx["R&D3"]==dspp)|(dfx["R&D4"]==dspp)|(dfx["R&D5"]==dspp)|(dfx["R&D6"]==dspp)|
        (dfx["๋์์ธ1"]==dspp)|(dfx["๋์์ธ2"]==dspp)|(dfx["ํฌ์ฅ์ฐ๊ตฌ"]==dspp)|(dfx["๊ตฌ๋งค"]==dspp)|
        (dfx["์์ฐ1"]==dspp)|(dfx["์์ฐ2"]==dspp)|(dfx["์์ฐ3"]==dspp)|(dfx["์์(์ด๊ด)"]==dspp)|(dfx["์์(๋ถ๋ฌธ์ฅ)"]==dspp)|
        (dfx["CRO"]==dspp)|(dfx["CROA"]==dspp)|(dfx["CROB"]==dspp)]           
                    
        # ํ์ํ ์ด๋ง ๋ฐ์ท
        # dxx= dx.drop(["์ ํ๋ฅBW","์ฌ์๋ถ์ฅ","๋ง์ผํ1","๋ง์ผํ2","๋ง์ผํ3",
        # "R&D1","R&D2","R&D3","R&D4","R&D5","R&D6",
        # "๋์์ธ1","๋์์ธ2","ํฌ์ฅ์ฐ๊ตฌ","๊ตฌ๋งค","์์ฐ1","์์ฐ2",
        # "์์ฐ3","์์(์ด๊ด)","์์(๋ถ๋ฌธ์ฅ)","CEO๋ณด๊ณ ","๊ณผ์  ID","๋น๊ณ ",
        # "๋นํด๋์ ์กฐ","์์๋ณด๊ณ ","ํ๊ฐ๋์","์ ํ๊ตฌ๋ถ","์ค์๋",
        # "๊ธด๊ธ์ฑ","๊ณผ์ ๋ถ๋ฅ ์ ์","๊ณผ์ ๋ถ๋ฅ"], axis=1, inplace=True)              

        dxx=dx.loc[:,["VOC ์ ์๋ฒํธ", "VOC๋ฑ๋ก์ผ", "๋์", "์ฌ์๊ตฐ", "์ฌ์๋ถ", "๋ธ๋๋", "์ ํ์ฝ๋", "์ ํ๋ช","๊ท๊ฒฉ", "๋ถ๋ง๋ด์ฉ", "์ต์ข ์์ธ์ ํ",
        "์ ํ๊ตฐ","์ ํ๋ฅ","์ฉ๊ธฐ", "์ ์กฐ์ผ","์ ํต๊ธฐํ", "LOT์ ๋ณด", "์ถ์๋์","โจ์ ์ ํ์ฌ๋ถ", 
        "์๋ด์ ํ", "โ ์ ์กฐ์", "โก์ ์กฐ์์์ธ์ ํ", "์ต์ข ๊ท์ฑ์", "โข๊ณต์ฅ/ํ๋ ฅํ์ฌ๋ช", "์/๋ถ์์ฌํ๋ ฅํ์ฌ",
        "โฃ๊ณ ๊ฐ๋ถ๋ง์ ํ", "โค์ด๋ฌผํผ์์ ํ", "โฅ์ธ๋ถ ์ด๋ฌผ๋ด์ญ","๊ฐ๋ด์ฌ๋ถ", "๊ตฌ์์ฒ ์ ํ", "โฆ6๋์์ฌ์์ญ", "VOC ์ ํ", "22๋์ ์กฐ ๊ณต์ ์ด๋ฌผ", "์ฌ์๊ตฐ๋ณ๊ตฌ๋ถ",
        "๋ฐ์์ง์ญ", "์ ํ๊ตฌ์์ฒ","๋ณ๊ฒฝ์ด๋ ฅ"]]          

        
        def draw_color_cell(x,color):
                color = f'background-color:{color}'
                return color
        
        # ๊ทธ๋ฆฌ๋์ ์๊น์ํ๊ธฐ
        dxxz= dxx.style.applymap(draw_color_cell,color='#FFFAF0',subset=pd.IndexSlice[:,['์ ํ๋ช', "๋ถ๋ง๋ด์ฉ"]])             
               
        st.dataframe(dxxz, width=2500,height=300)              
        
        # st.dataframe(df_display.round(2))
        
        @st.cache
        def convert_dxx(dxx):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return dxx.to_csv().encode('CP949')

        csv = convert_dxx(dxx)
        st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='Painpoint_dx.csv',
        mime='text/csv')                              

        st.error("๐๊ณ ๊ฐ painpoint๋"+" "+str(len(dxx))+"๊ฑด ์ ์๋์์ต๋๋ค.")
     
 
if name == '์์ฌํ์ง์ง์':
    st.subheader("์์ฌํ์ง์ง์ ๊ฒฐ๊ณผ")
    st.text("โ  ์์ฌํ์ง์ง๋จ ์์ธ ์กฐํ")

    input_user_name = st.text_input(label="User Password", value="")
    st.caption("*User์ ์ฃผ๋ฏผ๋ฑ๋ก๋ฒํธ ๋ท4์๋ฆฌ๋ฅผ ์๋ ฅํด์ฃผ์ญ์์ค")

    checkbox = st.checkbox('agree')
    btn_clicked = st.button("Confirm", key='confirm_btn', disabled=(checkbox is False))             

    if btn_clicked:
        con = st.container()
        con.caption("Result")
        if not str(input_user_name):
            con.error("Input your ID please~")
        else:
            con.write(f"Hello~ {str(input_user_name)}๋์ KPI ์ค์ ์ ๊ณต์ ๋๋ฆฝ๋๋ค")
        
        # st.text("๋นํด๋๋ ๊ณ ๊ฐ Painpoint ์ค์ ")

        def main() :    
            df= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="22_RQ") # CSV ํ์ผ ๋ถ๋ฌ์ค๊ณ  df ๋ณ์์ ์ ์ฅ
            df.set_index('๊ตฌ๋ถ', inplace=True)
            ds= df[df["Password"].astype(str).str.contains(input_user_name, case=True, na=False)]
            

            def draw_color_cell(x,color):
                color = f'background-color:{color}'
                return color
            ds= ds.style.applymap(draw_color_cell,color='#fff0f5',subset=pd.IndexSlice[:, ['22๋ ํ๋ฐ๊ธฐ ๊ฒฐ๊ณผ', "22๋ ํ๋ฐ๊ธฐ ๋ฑ๊ธ"]]).set_precision(0) 
            st.dataframe(ds, width=1100,height=20)     

            st.text("๐ ์/ํ๋ฐ๊ธฐ ์ง์ ์ฒ๋")

            df= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="22_RQd") # CSV ํ์ผ ๋ถ๋ฌ์ค๊ณ  df ๋ณ์์ ์ ์ฅ
            df.set_index('๊ตฌ๋ถ', inplace=True)
            dss= df[df["Password"].astype(str).str.contains(input_user_name, case=True, na=False)]
            def draw_color_cell(x,color):
                color = f'background-color:{color}'
                return color
            dss= dss.style.applymap(draw_color_cell,color='#fff8f6',subset=pd.IndexSlice[:, ['์๋ฐ๊ธฐ_5์ ', '์๋ฐ๊ธฐ_4์ ','์๋ฐ๊ธฐ_3์ ', '์๋ฐ๊ธฐ_2์ ','์๋ฐ๊ธฐ_1์ ', 'ํ๋ฐ๊ธฐ_5์ ', 'ํ๋ฐ๊ธฐ_4์ ', 'ํ๋ฐ๊ธฐ_3์ ', 'ํ๋ฐ๊ธฐ_2์ ', 'ํ๋ฐ๊ธฐ_1์ ']])


            st.dataframe(dss, width=1100,height=20)     
            
            st.text("โ๏ธ 9๊ฐ ๋ฑ๊ธ ๊ธฐ์ค")
            dt= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="22_RQdd") # CSV ํ์ผ ๋ถ๋ฌ์ค๊ณ  df ๋ณ์์ ์ ์ฅ
            dt.set_index('์ธ์ฆ ๋ฑ๊ธ', inplace=True)
            
            def draw_color_cell(x,color):
                color = f'background-color:{color}'
                return color
        
            # ๊ทธ๋ฆฌ๋์ ์๊น์ํ๊ธฐ
            dt= dt.style.applymap(draw_color_cell,color='#FFFAF0',subset=pd.IndexSlice[:,['์ธ์ฆ ์ ์', "์ ์"]])   

            st.dataframe(dt, width=500,height=210)     




        if __name__ == '__main__' :
            main()  




# st.markdown("# Main page ๐")
# st.sidebar.markdown("# Main page ๐")

# # pages/page_2.py

# import streamlit as st

# # st.markdown("# Page 2 โ๏ธ")
# st.sidebar.markdown("# Page 2 โ๏ธ")  

# pages/page_3.py

# import streamlit as st

# st.markdown("# Page 3 ๐")
# st.sidebar.markdown("# Page 3 ๐")
