import streamlit as st

# 브롤러 데이터 (간단히 3명만 예시)
brawlers = {
    "Shelly": {
        "description": "Close to mid-range fighter with shotgun.",
        "image_url": "https://static.brawlify.com/profile/portrait/shelly.png",
        "health": 3600,
        "attack_damage": 600
    },
    "Colt": {
        "description": "Long-range shooter with dual revolvers.",
        "image_url": "https://static.brawlify.com/profile/portrait/colt.png",
        "health": 2800,
        "attack_damage": 720
    },
    "Jessie": {
        "description": "Mid-range fighter with energy orb attack.",
        "image_url": "https://static.brawlify.com/profile/portrait/jessie.png",
        "health": 3200,
        "attack_damage": 640
    }
}

st.title("브롤스타즈 브롤러 선택기")

selected_brawler = st.selectbox("브롤러를 선택하세요", list(brawlers.keys()))

if selected_brawler:
    brawler = brawlers[selected_brawler]
    st.image(brawler["image_url"], width=200)
    st.write(f"**설명:** {brawler['description']}")
    st.write(f"**체력:** {brawler['health']}")
    st.write(f"**공격력:** {brawler['attack_damage']}")
