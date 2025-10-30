import streamlit as st
import json
import pandas as pd

# -----------------------------
# Helpers
# -----------------------------
def _extract_username_from_href(href: str | None) -> str | None:
    """https://www.instagram.com/_u/username 또는 /username 형태에서 username만 추출"""
    if not href or not isinstance(href, str):
        return None
    href = href.rstrip("/")
    parts = href.split("/")
    if not parts:
        return None
    # .../instagram.com/_u/<username>
    if len(parts) >= 2 and parts[-2] == "_u":
        return parts[-1]
    # .../instagram.com/<username>
    return parts[-1]

def _normalize(u: str | None) -> str | None:
    """비교용으로 정규화: 공백 제거, @ 제거, 소문자"""
    if not u or not isinstance(u, str):
        return None
    return u.strip().lstrip("@").lower()

def parse_following(following_json: dict) -> set[str]:
    """
    following.json 구조 예:
    {
      "relationships_following": [
        {
          "title": "username(있을 수도/없을 수도)",
          "string_list_data": [
            {"href": ".../_u/username" 또는 ".../username", "timestamp": ...}
          ]
        },
        ...
      ]
    }
    """
    results: set[str] = set()
    for entry in following_json.get("relationships_following", []):
        username = entry.get("title")
        if not username:
            data = entry.get("string_list_data", [])
            if data:
                # value가 없는 export가 많아서 href에서 파싱
                username = data[0].get("value") or _extract_username_from_href(data[0].get("href"))
        norm = _normalize(username)
        if norm:
            results.add(norm)
    return results

def parse_followers(followers_json: list) -> set[str]:
    """
    followers.json 구조 예:
    [
      {
        "string_list_data": [
          {"href": ".../username", "value": "username"(없을 수 있음), "timestamp": ...}
        ]
      },
      ...
    ]
    """
    results: set[str] = set()
    for entry in followers_json:
        data_list = entry.get("string_list_data", [])
        for data in data_list:
            username = data.get("value") or _extract_username_from_href(data.get("href"))
            norm = _normalize(username)
            if norm:
                results.add(norm)
    return results

def make_link_df(usernames: list[str]) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Username": usernames,
            "Profile": [f"https://instagram.com/{u}" for u in usernames],
        }
    )

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="팔로우/팔로워 관리 도구", page_icon="📊", layout="wide")

# --- 페이지 선택 ---
page = st.sidebar.radio("메뉴", ["📊 팔로우/팔로워 트래커"])
st.title("팔로우/팔로워 관리 도구")

# --- JSON 파일 업로드 + 세션 저장 ---
if page == "📊 팔로우/팔로워 트래커":
    col_up1, col_up2 = st.columns(2)
    with col_up1:
        following_file = st.file_uploader("📄 following.json", type="json", key="follow_file")
        if following_file:
            try:
                st.session_state.following_data = json.load(following_file)
                st.success("following.json 로드 완료")
            except Exception as e:
                st.error(f"following.json 파싱 오류: {e}")

    with col_up2:
        followers_file = st.file_uploader("📄 followers.json", type="json", key="follower_file")
        if followers_file:
            try:
                st.session_state.followers_data = json.load(followers_file)
                st.success("followers.json 로드 완료")
            except Exception as e:
                st.error(f"followers.json 파싱 오류: {e}")

    # --- 비교 ---
    if "following_data" in st.session_state and "followers_data" in st.session_state:
        try:
            following_set = parse_following(st.session_state.following_data)
        except Exception as e:
            st.error(f"팔로잉 파싱 중 오류: {e}")
            following_set = set()

        try:
            # followers.json은 리스트 최상위
            followers_set = parse_followers(st.session_state.followers_data)
        except Exception as e:
            st.error(f"팔로워 파싱 중 오류: {e}")
            followers_set = set()

        only_following = sorted(list(following_set - followers_set))
        only_followers = sorted(list(followers_set - following_set))

        tab1, tab2 = st.tabs(
            [
                "🟠 나만 팔로우 중",
                "🔵 나를 팔로우했지만 나는 안 함",
            ]
        )

        with tab1:
            st.write(f"총 **{len(only_following)}명**")
            df1 = make_link_df(only_following)
            st.data_editor(
                df1,
                column_config={"Profile": st.column_config.LinkColumn("🔗 인스타 프로필")},
                hide_index=True,
                disabled=True,
                use_container_width=True,
            )

        with tab2:
            st.write(f"총 **{len(only_followers)}명**")
            df2 = make_link_df(only_followers)
            st.data_editor(
                df2,
                column_config={"Profile": st.column_config.LinkColumn("🔗 인스타 프로필")},
                hide_index=True,
                disabled=True,
                use_container_width=True,
            )

    else:
        st.info("following.json 과 followers.json을 모두 업로드하면 비교가 시작됩니다.")
