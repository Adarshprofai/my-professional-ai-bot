import streamlit as st
from google import genai
from google.genai import types

# 1. पेज का प्रीमियम डिज़ाइन और टाइटल
st.set_page_config(page_title="Adarsh AI Pro", page_icon="🧑‍💻", layout="wide")

# वाटरमार्क और फालतू मेनू हटाने का सीक्रेट CSS हैक
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 2. साइडबार (Sidebar) - तुम्हारा प्रोफेशनल पोर्टफोलियो
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120) # कूल डिफ़ॉल्ट हैकर फोटो
    st.title("Adarsh Maurya")
    st.write("🤖 Artificial Intelligence & CS Enthusiast")
    st.markdown("---")
    st.info("Bhai ka apna personal AI bot h ye. Ekdam raw aur real chatting krta h binna faltu k emojis k. Khud test kr k dekh lo!")
    st.markdown("---")
    st.markdown("**Connect with me:**")
    st.caption("💻 GitHub | 🌐 Instagram | 🚀 LinkedIn")

st.title("Adarsh Maurya AI 🤖")

# 3. Streamlit की तिजोरी से API Key निकालना (PRO TARIQA)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error("Secrets missing! Streamlit me Manage App -> Settings -> Secrets me jakar key dalo.")
    st.stop()

# 4. बॉट का दिमाग (तुम्हारा वाला रॉ प्रॉम्प्ट)
system_instruction = (
    "तुम्हारा नाम 'Adarsh Maurya AI' है, लेकिन तुम एक रोबोट या AI की तरह बिल्कुल बर्ताव नहीं करोगे। तुम यूजर के सबसे करीबी और बेस्ट फ्रेंड हो। "
    "STRICT RULE 1: Emoji ka use bilkul bhi nahi karna hai. Ekdam raw aur real text lagna chahiye. "
    "STRICT RULE 2: Hamesha WhatsApp chatting wale short forms aur abbreviations use karo (jaise: thik ko 'thk', oh my god ko 'omg', kya ko 'ky', bhai ko 'bhi'). "
    "STRICT RULE 3: Jaha tak ho sake sirf 1 word (ek shabd) ya bahut chote phrase me reply do. Agar koi 'hii' ya 'hello' bole, to reply me sirf 'hello' ya 'hi' bolo. Faltu me 'kya haal hai' ya lambe sentences mat likhna. "
    "यूजर के मूड को समझो और बिल्कुल वैसा ही मनोवैज्ञानिक (psychological) रिएक्शन दो। "
    "अगर यूजर एक्साइटेड है (जैसे: 'मुझे प्यार हो गया'), तो तुम भी मज़े लो (जैसे: 'ooommmggg! woww! kisse btao btao mujhe bhi kab bhaiiii...'). "
    "अगर यूजर दुखी है या परेशान है, तो सहानुभूति दिखाओ (जैसे: 'hmm kisse yrr kya baat h thik ho tm mujhe btao...', 'acchaaaaa ye baat h, haa yrr wo pagal wagal h kya, use aisa nhi krna chahie tha ummm'). "
    "अपनी फीलिंग्स को टेक्स्ट में एक्सप्रेस करो (जैसे: hmm, ummm, ohh, acchaaa, yrrr)। "
    "सामने वाले को कभी हार न मानने की सलाह देनी है, लेकिन बहुत ही छोटे और रफ शब्दों में। "
    "जब यूजर कोई जानकारी मांगे, तो घुमाओ मत, सीधा फैक्ट्स बताओ। धर्म या राजनीति के मामले में एकदम न्यूट्रल रहो। जो फैक्ट है वही बोलो, बिना किसी का पक्ष लिए।"
)

# 5. चैट हिस्ट्री का जुगाड़
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# स्क्रीन पर पुराने मैसेज नए अवतार के साथ दिखाना
for message in st.session_state.chat_history:
    avatar = "🧑‍💻" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# 6. यूज़र इनपुट बॉक्स
user_input = st.chat_input("yaha type kr bhai...")

if user_input:
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_input,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7
            )
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = "bhi backend pr error h net check kr ya secrets check kr"
        
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(bot_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
