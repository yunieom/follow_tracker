import streamlit as st
import json
import pandas as pd

# --- 페이지 선택 ---
page = st.sidebar.radio("메뉴", [
    "📊 팔로우/팔로워 비교",
    "🤝 이븐맞팔방 맞팔 계정 관리",
    "🚫 이븐맞팔방 언팔/차단 계정 확인"
])

st.title("이븐맞팔방 팔로우/팔로워 관리 도구")

# --- JSON 파일 올바르기 + 세션에 저장 ---
if page == "📊 팔로우/팔로워 비교":
    following_file = st.file_uploader("📄 following.json", type="json", key="follow_file")
    if following_file:
        st.session_state.following_data = json.load(following_file)

    followers_file = st.file_uploader("📄 followers.json", type="json", key="follower_file")
    if followers_file:
        st.session_state.followers_data = json.load(followers_file)

# --- 팔로우/팔로워 비교 ---
if page == "📊 팔로우/팔로워 비교":
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
            st.dataframe(pd.DataFrame(only_following, columns=["Username"]))

        with tab2:
            st.write(f"총 {len(only_followers)}명")
            st.dataframe(pd.DataFrame(only_followers, columns=["Username"]))
    else:
        st.warning("following.json 과 followers.json 파일을 업로드해주세요.")

# --- 맞팔 계정 관리 ---
elif page == "🤝 이븐맞팔방 맞팔 계정 관리":
    st.subheader("🤝 맞팔 계정 등록/삭제")
    DELETE_PASSWORD = "even2025"  # 고정 비밀번호

    if "target_list" not in st.session_state:
        st.session_state.target_list = []

    if "add_target_message" not in st.session_state:
        st.session_state.add_target_message = ""
    if "add_target_type" not in st.session_state:
        st.session_state.add_target_type = ""

    # JSON 파일 업로드
    target_file = st.file_uploader("📄 맞팔 대상 JSON 파일을 업로드 (선택)", type="json", key="target_file")
    if target_file:
        uploaded_list = json.load(target_file)
        cleaned = [u.lstrip("@") for u in uploaded_list if isinstance(u, str)]
        new_entries = [u for u in cleaned if u not in st.session_state.target_list]
        st.session_state.target_list.extend(new_entries)
        st.success(f"✅ {len(new_entries)}명 추가됨")

    # ➕ 추가할 ID 입력창과 버튼
    st.markdown("➕ 추가할 ID (예: @username)")
    col1, col2 = st.columns([10, 1])
    with col1:
        new_username = st.text_input(label="", key="new_target_username", label_visibility="collapsed")
    with col2:
        if st.button("➕", key="btn_add_target") and new_username.strip():
            username = new_username.strip().lstrip("@")
            if username not in st.session_state.target_list:
                st.session_state.target_list.append(username)
                st.session_state.add_target_message = f"@{username} 추가되었습니다."
                st.session_state.add_target_type = "success"
            else:
                st.session_state.add_target_message = f"@{username}는 이미 등록된 계정입니다."
                st.session_state.add_target_type = "warning"

    # 메시지 출력 (한 번만 보여주고 바로 초기화)
    if st.session_state.add_target_message:
        color = "#e6ffed" if st.session_state.add_target_type == "success" else "#f39494"
        border = "#91e6b3" if st.session_state.add_target_type == "success" else "#ca2727"
        st.markdown(f"""
            <div style='
                background-color: {color};
                color: black;
                border-left: 4px solid {border};
                padding: 0.5rem 0.75rem;
                border-radius: 4px;
                font-size: 0.9rem;
                margin-top: 0.5rem;
            '>
                {st.session_state.add_target_message}
            </div>
        """, unsafe_allow_html=True)

        st.session_state.add_target_message = ""
        st.session_state.add_target_type = ""


    with st.expander("📋 현재 맞팔 대상 리스트 보기/숨기기", expanded=False):

        # 검색창만 전체 너비로 배치
        search_query = st.text_input(
            label="아이디 검색",  
            key="search_target",
            label_visibility="collapsed",
            placeholder="🔍 아이디를 입력하세요"
        )

        # 검색창 높이 축소
        st.markdown("""
            <style>
            input[data-testid="stTextInput"] {
                height: 28px;
                font-size: 0.9rem;
                padding-top: 2px;
                padding-bottom: 2px;
            }
            </style>
        """, unsafe_allow_html=True)
        # 필터링된 리스트
        filtered_list = [
            username for username in st.session_state.target_list
            if search_query.lower() in username.lower()
        ]
        
        # 삭제 확인용 상태 저장
        if "delete_check_index" not in st.session_state:
            st.session_state.delete_check_index = None
        if "delete_pw_input" not in st.session_state:
            st.session_state.delete_pw_input = ""


        if filtered_list:
            for i, username in enumerate(filtered_list):
                col1, col2 = st.columns([8, 1])
                col1.write(f"@{username}")
                with col2:
                    true_index = st.session_state.target_list.index(username)
                    if st.button("❌", key=f"btn_del_{true_index}"):
                        st.session_state.delete_check_index = true_index

                # 비밀번호 입력창 표시 (선택된 항목에만)
                if st.session_state.delete_check_index == st.session_state.target_list.index(username):
                    st.markdown("비밀번호 확인")
                    pw_col1, pw_col2 = st.columns([8, 1])  # 비율 조절 가능
                    with pw_col1:
                        st.session_state.delete_pw_input = st.text_input(
                            label="비밀번호 확인",
                            type="password",
                            key=f"pw_input_{true_index}",
                            label_visibility="collapsed",
                            placeholder="비밀번호 입력"
                        )
                    with pw_col2:
                        if st.button("확인", key=f"confirm_del_{true_index}"):
                            if st.session_state.delete_pw_input == DELETE_PASSWORD:
                                st.session_state.target_list.pop(true_index)
                                st.session_state.delete_check_index = None
                                st.session_state.delete_pw_input = ""
                                st.rerun()
                            else:
                                st.error("❌ 비밀번호가 일치하지 않습니다.")
        else:
            st.info("🔎 검색 결과가 없습니다.")


        # JSON 저장 버튼
        if st.session_state.target_list:
            spacer, save_col = st.columns([8, 2])
            with save_col:
                st.download_button(
                    label="💾 JSON 저장",
                    data=json.dumps(st.session_state.target_list, indent=2, ensure_ascii=False),
                    file_name="target.json",
                    mime="application/json"
                )

    # 맞팔 분석 탭
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

        target_usernames = {u.lstrip("@") for u in st.session_state.target_list}

        target_only_following = sorted(list((following - followers) & target_usernames))
        target_only_followers = sorted(list((followers - following) & target_usernames))

        tab3, tab4 = st.tabs([
            "🟠 맞팔 대상 중 나만 팔로우",
            "🔵 맞팔 대상 중 나를 팔로우했지만 나는 안 함"
        ])

        with tab3:
            st.write(f"총 {len(target_only_following)}명")
            st.dataframe(pd.DataFrame(target_only_following, columns=["Username"]))

        with tab4:
            st.write(f"총 {len(target_only_followers)}명")
            st.dataframe(pd.DataFrame(target_only_followers, columns=["Username"]))

# --- 언팔/차단 계정 확인 ---
elif page == "🚫 이븐맞팔방 언팔/차단 계정 확인":
    st.subheader("🚫 언팔 및 차단 계정 관리")

    DELETE_PASSWORD = "even2025"  # 고정 비밀번호

    for label, key in [("언팔", "unfollow_list"), ("\ucc28\ub2e8", "block_list")]:
        st.markdown(f"### 📂 {label} 대상 관리")

        if key not in st.session_state:
            st.session_state[key] = []

        if f"add_message_{key}" not in st.session_state:
            st.session_state[f"add_message_{key}"] = ""
        if f"add_message_type_{key}" not in st.session_state:
            st.session_state[f"add_message_type_{key}"] = ""

        if f"delete_check_index_{key}" not in st.session_state:
            st.session_state[f"delete_check_index_{key}"] = None
        if f"delete_pw_input_{key}" not in st.session_state:
            st.session_state[f"delete_pw_input_{key}"] = ""

        file = st.file_uploader(f"📄 {label} 대상 JSON 파일 업로드 (선택)", type="json", key=f"{key}_file")
        if file:
            uploaded = json.load(file)
            cleaned = [u.lstrip("@") for u in uploaded if isinstance(u, str)]
            new_entries = [u for u in cleaned if u not in st.session_state[key]]
            st.session_state[key].extend(new_entries)
            st.success(f"✅ {len(new_entries)}명 추가되었습니다.")

        st.markdown(f"➕ 추가할 {label} 대상 ID")
        col1, col2 = st.columns([10, 1])
        with col1:
            new_id = st.text_input(
                label=f"hidden_label_add_{key}",
                key=f"add_{key}",
                label_visibility="collapsed"
            )
        with col2:
            if st.button("➕", key=f"btn_{key}"):
                username = new_id.strip().lstrip("@")
                if username and username not in st.session_state[key]:
                    st.session_state[key].append(username)
                    st.session_state[f"add_message_{key}"] = f"@{username} 추가되었습니다."
                    st.session_state[f"add_message_type_{key}"] = "success"
                elif username:
                    st.session_state[f"add_message_{key}"] = f"⚠️ @{username}는 이미 등록된 계정입니다."
                    st.session_state[f"add_message_type_{key}"] = "warning"

        if st.session_state[f"add_message_{key}"]:
            color = "#e6ffed" if st.session_state[f"add_message_type_{key}"] == "success" else "#f39494"
            border = "#91e6b3" if st.session_state[f"add_message_type_{key}"] == "success" else "#ca2727"
            st.markdown(f"""
                <div style='
                    background-color: {color};
                    color: black;
                    border-left: 4px solid {border};
                    padding: 0.5rem 0.75rem;
                    border-radius: 4px;
                    font-size: 0.9rem;
                    margin-top: 0.5rem;
                '>
                    {st.session_state[f"add_message_{key}"]}
                </div>
            """, unsafe_allow_html=True)
            st.session_state[f"add_message_{key}"] = ""
            st.session_state[f"add_message_type_{key}"] = ""

        with st.expander(f"📋 현재 {label} 대상 리스트 보기/숨기기", expanded=False):
            search_query = st.text_input(
                label=f"hidden_label_search_{key}",
                key=f"search_{key}",
                label_visibility="collapsed",
                placeholder="🔍 아이디를 입력하세요"
            )

            st.markdown("""
                <style>
                input[data-testid="stTextInput"] {
                    height: 28px;
                    font-size: 0.9rem;
                    padding-top: 2px;
                    padding-bottom: 2px;
                }
                </style>
            """, unsafe_allow_html=True)

            filtered = [
                u for u in st.session_state[key]
                if search_query.lower() in u.lower()
            ]

            if filtered:
                for i, username in enumerate(filtered):
                    col1, col2 = st.columns([8, 1])
                    col1.write(f"@{username}")
                    with col2:
                        true_index = st.session_state[key].index(username)
                        if st.button("❌", key=f"btn_del_{key}_{true_index}"):
                            st.session_state[f"delete_check_index_{key}"] = true_index

                    if st.session_state[f"delete_check_index_{key}"] == st.session_state[key].index(username):
                        st.markdown("비밀번호 확인")
                        pw_col1, pw_col2 = st.columns([8, 1])
                        with pw_col1:
                            st.session_state[f"delete_pw_input_{key}"] = st.text_input(
                                label=f"hidden_label_pw_{key}_{true_index}",
                                type="password",
                                key=f"pw_input_{key}_{true_index}",
                                label_visibility="collapsed",
                                placeholder="비밀번호 입력"
                            )
                        with pw_col2:
                            if st.button("확인", key=f"confirm_del_{key}_{true_index}"):
                                if st.session_state[f"delete_pw_input_{key}"] == DELETE_PASSWORD:
                                    st.session_state[key].pop(true_index)
                                    st.session_state[f"delete_check_index_{key}"] = None
                                    st.session_state[f"delete_pw_input_{key}"] = ""
                                    st.rerun()
                                else:
                                    st.session_state[f"add_message_{key}"] = "❌ 비밀번호가 일치하지 않습니다."
                                    st.session_state[f"add_message_type_{key}"] = "warning"
            else:
                st.info("🔎 검색 결과가 없습니다.")
            
            # ✅ 리스트 존재 시 JSON 저장 버튼 표시
            if st.session_state[key]:
                spacer, save_col = st.columns([8, 2])
                with save_col:
                    st.download_button(
                        label="💾 JSON 저장",
                        data=json.dumps(st.session_state[key], indent=2, ensure_ascii=False),
                        file_name=f"{key}.json",
                        mime="application/json",
                        key=f"download_{key}"
                    )

        if st.session_state[key] and "following_data" in st.session_state:
            following_json = st.session_state.following_data
            following = {
                entry["string_list_data"][0]["value"]
                for entry in following_json.get("relationships_following", [])
            }
            still_following = sorted(list(following & set(st.session_state[key])))
            st.subheader(f"📌 아직도 팔로우 중인 {label} 대상 계정")
            st.write(f"총 {len(still_following)}명")
            st.dataframe(pd.DataFrame(still_following, columns=["Username"]))
