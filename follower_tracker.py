import streamlit as st
import json
import pandas as pd

st.title("Instagram Follower Tracker")
st.write("팔로워/팔로잉 json 업로드 후 차이 비교")

# 파일 업로드
following_file = st.file_uploader("📤 following.json", type="json")
followers_file = st.file_uploader("📤 followers.json", type="json")
target_file = st.file_uploader("📤 맞팔하고 싶은 계정 리스트 (target.json)", type="json")

if following_file and followers_file:
    # JSON 로드
    following_json = json.load(following_file)
    followers_json = json.load(followers_file)

    # 유저네임 추출
    following = {
        entry["string_list_data"][0]["value"]
        for entry in following_json.get("relationships_following", [])
    }
    followers = {
        entry["string_list_data"][0]["value"]
        for entry in followers_json
    }

    # 기본 비교
    only_following = sorted(list(following - followers))
    only_followers = sorted(list(followers - following))

    # 탭 나누기
    tab1, tab2, tab3, tab4 = st.tabs([
        "🟠 나만 팔로우 중",
        "🔵 나를 팔로우했지만 나는 안 함",
        "🟠 맞팔 대상 중 나만 팔로우",
        "🔵 맞팔 대상 중 나를 팔로우했지만 나는 안 함"
    ])

    with tab1:
        st.subheader("🟠 나만 팔로우 중")
        st.write(f"총 {len(only_following)}명")
        st.dataframe(pd.DataFrame(only_following, columns=["Username"]))

    with tab2:
        st.subheader("🔵 나를 팔로우했지만 나는 안 함")
        st.write(f"총 {len(only_followers)}명")
        st.dataframe(pd.DataFrame(only_followers, columns=["Username"]))

    # 맞팔 체크용
    if target_file:
        target_list = json.load(target_file)
        target_usernames = {u.lstrip("@") for u in target_list}

        # 맞팔 대상 중에서 나만 팔로우
        target_only_following = sorted(list((following - followers) & target_usernames))
        target_only_followers = sorted(list((followers - following) & target_usernames))

        with tab3:
            st.subheader("🟠 맞팔 대상 중 나만 팔로우")
            st.write(f"총 {len(target_only_following)}명")
            st.dataframe(pd.DataFrame(target_only_following, columns=["Username"]))

        with tab4:
            st.subheader("🔵 맞팔 대상 중 나를 팔로우했지만 나는 안 함")
            st.write(f"총 {len(target_only_followers)}명")
            st.dataframe(pd.DataFrame(target_only_followers, columns=["Username"]))
    else:
        with tab3:
            st.info("📥 맞팔 대상 JSON 파일을 업로드하면 이 탭이 활성화됩니다.")
        with tab4:
            st.info("📥 맞팔 대상 JSON 파일을 업로드하면 이 탭이 활성화됩니다.")

# 언팔 대상 계정 체크
unfollow_file = st.file_uploader("📤 언팔할 계정 리스트 (unfollow_target.json)", type="json")

if unfollow_file:
    unfollow_list = json.load(unfollow_file)
    unfollow_usernames = {u.lstrip("@") for u in unfollow_list}

    # 아직 팔로우 중인 언팔 대상 계정만 필터링
    still_following_unfollows = sorted(list(following & unfollow_usernames))

    st.markdown("---")
    st.subheader("🚫 아직도 팔로우 중인 언팔 대상 계정")
    st.write(f"총 {len(still_following_unfollows)}명")
    st.dataframe(pd.DataFrame(still_following_unfollows, columns=["Username"]))