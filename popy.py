import streamlit as st
import pandas as pd
from PIL import Image




st.set_page_config(layout="wide")

# def main() :    
#     img = Image.open('guide.png')
#     st.image(img)

# if __name__ == "__main__" :
#     main()

st.sidebar.header('🎈Menu')
name = st.sidebar.selectbox('KPI 실적', ['[Select]', '고객 Painpoint 실적', "안심품질지수"])
name2 = st.sidebar.selectbox('상세조회', ['[Select]', '고객 Painpoint 상세', "안심품질진단결과 상세"])


if name == '고객 Painpoint 실적':
    st.subheader("임원/부문장 KPI 결과")
    st.text("■ 고객 Painpoint 실적 조회")

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

if name2 == '고객 Painpoint 상세':        
    st.subheader("임원/부문장 KPI_고객PP 상세 조회")
    st.text("■ 고객 Painpoint 상세 조회")

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
                con.write(f"Hello~ {str(input_user_name)}님의 고객Painpoint 상세 내용을 공유드립니다")
            
            # st.text("당해년도 고객 Painpoint 실적")

            def main() :    
                dfx= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="2023_Painpoint_KPI") # CSV 파일 불러오고 df 변수에 저장
                # df.set_index('Name', inplace=True)              

    
                # Password에서 Name 갖고 오기 ex)1001-> 이형석 
                ds= dfx["Name"][dfx["Password"].astype(str).str.contains(input_user_name, case=True, na=False)]
                dspp= ds.iloc[0] #ds는 series임 그래서 값을 갖고 와야함. 
                # dspp

                dfs= pd.read_excel("2023_Painpoint_KPI2.xlsx", sheet_name="22PP_Detail")            
                dfx= dfs.astype(str)
                

                dx = dfx[(dfx["사업부장"]==dspp)|(dfx["마케팅1"]==dspp)|(dfx["마케팅2"]==dspp)|(dfx["마케팅3"]==dspp)|
                (dfx["R&D1"]==dspp)|(dfx["R&D2"]==dspp)|(dfx["R&D3"]==dspp)|(dfx["R&D4"]==dspp)|(dfx["R&D5"]==dspp)|(dfx["R&D6"]==dspp)|
                (dfx["디자인1"]==dspp)|(dfx["디자인2"]==dspp)|(dfx["포장연구"]==dspp)|(dfx["구매"]==dspp)|
                (dfx["생산1"]==dspp)|(dfx["생산2"]==dspp)|(dfx["생산3"]==dspp)|(dfx["영업(총괄)"]==dspp)|(dfx["영업(부문장)"]==dspp)]           
                
                # 필요한 열만 발췌
                # dxx= dx.drop(["제품류BW","사업부장","마케팅1","마케팅2","마케팅3",
                # "R&D1","R&D2","R&D3","R&D4","R&D5","R&D6",
                # "디자인1","디자인2","포장연구","구매","생산1","생산2",
                # "생산3","영업(총괄)","영업(부문장)","CEO보고","과제 ID","비고",
                # "당해년제조","임원보고","평가대상","제품구분","중요도",
                # "긴급성","과제분류 점수","과제분류"], axis=1, inplace=True)  

                dxx=dx.loc[:,["VOC 접수번호", "VOC등록일", "년월", "사업군", "사업부", "브랜드", "제품코드", "제품명",
                "제품군","제품류","용기", "제조일","유통기한", "LOT정보", "출시년월","⑨신제품여부", "불만내용",
                "상담유형", "①제조원", "②제조원원인유형", "최종 귀책원", "최종 원인유형", "③공장/협력회사명", "원/부자재협력회사",
                "④고객불만유형", "⑤이물혼입유형", "⑥세부 이물내역","개봉여부", "구입처 유형", "⑦6대안심영역", "VOC 유형", "22년제조 공정이물", "사업군별구분",
                "발생지역", "제품구입처","변경이력"]]          
            
                st.dataframe(dxx, width=2500,height=300)      
                
                def convert_dxx(dxx):
                        return dxx.to_csv().encode('CP949')

                csv = convert_dxx(dxx)

                st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='Painpoint내역.csv',
                mime='text/csv')
                st.subheader("고객 painpoint는"+" "+str(len(dx))+"건 접수되었습니다.")           
                    

            if __name__ == '__main__' :
                main()
 




# st.markdown("# Main page 🎈")
# st.sidebar.markdown("# Main page 🎈")

# # pages/page_2.py

# import streamlit as st

# # st.markdown("# Page 2 ❄️")
# st.sidebar.markdown("# Page 2 ❄️")  

# pages/page_3.py

# import streamlit as st

# st.markdown("# Page 3 🎉")
# st.sidebar.markdown("# Page 3 🎉")
