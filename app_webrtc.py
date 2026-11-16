import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

# بيانات حسابك من Metered.ca
TURN_USERNAME = "ضع_اسم_المستخدم_هنا"
TURN_CREDENTIAL = "ضع_كلمة_المرور_هنا"

# إعدادات خادم TURN
rtc_config = {
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},  # خادم STUN من جوجل
        {
            "urls": ["turn:openrelay.metered.ca:80", "turn:openrelay.metered.ca:443"],
            "username": TURN_USERNAME,
            "credential": TURN_CREDENTIAL,
        },
    ]
}

st.title("📷 بصيرة Live — اختبار الكاميرا والمايك")
webrtc_streamer(
    key="basira-test",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=rtc_config,  # تمرير الإعدادات هنا
    media_stream_constraints={"video": True, "audio": True},
    async_processing=True,
)
