import streamlit as st
import pandas as pd

st.subheader("임원/부문장 KPI 결과")
st.text("- 고객 Painpoint 실적 조회")

input_user_name = st.text_input(label="User Password", value="")
st.caption("*User의 주민등록번호 뒷4자리를 입력해주십시오")

checkbox = st.checkbox('agree')
btn_clicked = st.button("Confirm", key='confirm_btn', disabled=(checkbox is False))

if btn_clicked:
    con = st.container()
    con.caption("Result")
    if not str(input_user_name):
        con.error("Input your ID please~")
    else:
        con.write(f"Hello~ {str(input_user_name)}님의 KPI 실적을 공유드립니다")
    
    st.text("당해년도 고객 Painpoint 실적")

    def main() :    
        df= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="2023_Painpoint_KPI") # CSV 파일 불러오고 df 변수에 저장
        df.set_index('Name', inplace=True)
        ds= df[df["Password"].astype(str).str.contains(input_user_name, case=True, na=False)]
        # da= ds.style.hide_index()
        st.dataframe(ds, width=2500,height=20)     
        

    if __name__ == '__main__' :
        main()  

    st.text("전년도 고객 Painpoint 실적")

    def main() :    
        df2= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="2022") # CSV 파일 불러오고 df 변수에 저장
        df2.set_index('Name', inplace=True)
        ds2= df2[df2["Password"].astype(str).str.contains(input_user_name, case=True, na=False)]
        # da= ds.style.hide_index()
        st.dataframe(ds2, width=2500,height=20)             

    if __name__ == '__main__' :
        main()

    st.success("Success")

# if st.button("search"):
#     df_result_search = df[df['name'].str.contains(name_search,case=False, na=False)]
#     df_result_search = df[df['password'].str.contains(password_search,case=False, na=False)]
                    
#     st.write("{} Records ".format(str(df_result_search.shape[0])))
#     st.dataframe(df_result_search)