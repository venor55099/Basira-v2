import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.set_page_config(page_title="بصيرة Live - اختبار", page_icon="📷")
st.title("📷 بصيرة Live — اختبار الكاميرا والمايك")
st.write("اضغط على زرار START، واسمح للمتصفح بالوصول للكاميرا والمايك.")

webrtc_streamer(
    key="basira-test",
    mode=WebRtcMode.SENDRECV,
    media_stream_constraints={
        "video": True,
        "audio": True,
    },
    async_processing=True,
)

st.success("لو شوفت نفسك في الكاميرا، الأساس شغال ✅")
