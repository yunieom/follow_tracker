import streamlit as st
import json
import pandas as pd

# --- 페이지 선택 ---
page = st.sidebar.radio("메뉴", [
    "📊 팔로우/팔로워 트래커",
])

st.title("팔로우/팔로워 관리 도구")

# --- JSON 파일 올바르기 + 세션에 저장 ---
if page == "📊 팔로우/팔로워 트래커":
    following_file = st.file_uploader("📄 following.json", type="json", key="follow_file")
    if following_file:
        st.session_state.following_data = json.load(following_file)

    followers_file = st.file_uploader("📄 followers.json", type="json", key="follower_file")
    if followers_file:
        st.session_state.followers_data = json.load(followers_file)

def render_link_table(usernames: list[str], header_label: str = "계정 (@아이디)"):
    """인스타 아이디 리스트를 클릭 가능한 마크다운 테이블로 렌더링"""
    if not usernames:
        st.markdown("> 표시할 계정이 없어요.")
        return
    # 마크다운 테이블 한 줄씩 생성
    rows = "\n".join([f"| [@{u}](https://instagram.com/{u}) |" for u in usernames])
    md = f"| {header_label} |\n|---|\n{rows}"
    st.markdown(md, unsafe_allow_html=True)

# --- 팔로우/팔로워 비교 ---
if page == "📊 팔로우/팔로워 트래커":
    if "following_data" in st.session_state and "followers_data" in st.session_state:
        following_json = st.session_state.following_data
        followers_json = st.session_state.followers_data

        following = {
            entry["string_list_data"][0]["value"]
            for entry in following_json.get("relationships_following", [])
        }
        followers = {
            entry["string_list_data"][0]["value"]
            for entry in followers_json
        }

        only_following = sorted(list(following - followers))
        only_followers = sorted(list(followers - following))

        tab1, tab2 = st.tabs(["🟠 나만 팔로우 중", "🔵 나를 팔로우했지만 나는 안 함"])

        with tab1:
            st.write(f"총 {len(only_following)}명")
            df1 = pd.DataFrame({
                "Username": only_following,
                "Profile": [f"https://instagram.com/{u}" for u in only_following]
            })
            st.data_editor(
                df1,
                column_config={
                    "Profile": st.column_config.LinkColumn("Instagram 계정"),
                },
                hide_index=True,
                disabled=True,  # 수정 불가능
            )

        with tab2:
            st.write(f"총 {len(only_followers)}명")
            df2 = pd.DataFrame({
                "Username": only_followers,
                "Profile": [f"https://instagram.com/{u}" for u in only_followers]
            })
            st.data_editor(
                df2,
                column_config={
                    "Profile": st.column_config.LinkColumn("Instagram 계정"),
                },
                hide_index=True,
                disabled=True,
            )

    else:
        st.warning("following.json 과 followers.json 파일을 업로드해주세요.")
