import streamlit as st
from google import genai
from google.genai import types

# 1. पेज का प्रीमियम डिज़ाइन
st.set_page_config(page_title="Adarsh AI Pro", page_icon="🧑‍💻", layout="wide")

# 2. PREMIUM UI (Glassmorphism & No Watermark)
# 2. PREMIUM UI (Glassmorphism, No Watermark & White Text)
premium_css = """
<style>
/* 1. Watermark aur upar/neeche ka menu gayab karo */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* 2. Dark Cinematic Background Image */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* 3. Transparent Sidebar (Glass Effect) */
[data-testid="stSidebar"] {
    background-color: rgba(10, 10, 10, 0.4) !important;
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

/* 🟢 NEW: Sidebar aur sabhi text ko safed (White) karna */
[data-testid="stSidebar"] * {
    color: #ffffff !important;
}
h1, h2, h3, p, span, div {
    color: #ffffff !important;
}

/* 🟢 NEW: Info Box (Neela dabba) ko bhi glass jaisa dark banana */
div[data-testid="stAlert"] {
    background-color: rgba(20, 20, 20, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(255, 255, 255, 0.2) !important;
    color: white !important;
}

/* 4. Chat Messages me Glassmorphism */
.stChatMessage {
    background-color: rgba(20, 20, 20, 0.5) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    color: white !important;
}

/* 5. Chat Input Box (Neeche type karne wali jagah) */
.stChatInputContainer {
    background-color: rgba(0, 0, 0, 0.6) !important;
    backdrop-filter: blur(15px) !important;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
}

/* Input text aur placeholder ka color white karna */
textarea {
    color: white !important;
}
textarea::placeholder {
    color: rgba(255, 255, 255, 0.6) !important;
}
</style>
"""
st.markdown(premium_css, unsafe_allow_html=True)
# 2. साइडबार
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.title("Adarsh Maurya")
    st.write("🤖 Artificial Intelligence & CS Enthusiast")
    st.markdown("---")
    st.info("Bhai ka apna personal AI bot h ye. Ekdam raw aur real chatting krta h binna faltu k emojis k. Khud test kr k dekh lo!")
    st.markdown("---")
    st.markdown("**Connect with me:**")
    st.caption("💻 GitHub | 🌐 Instagram | 🚀 LinkedIn")
/* 1. Watermark aur upar/neeche ka menu gayab karo */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
._link_1hwk6_10 {display: none;} /* Extra Github link hider */

/* 2. Dark Cinematic Background Image */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* 3. Transparent Sidebar (Glass Effect) */
[data-testid="stSidebar"] {
    background-color: rgba(10, 10, 10, 0.4) !important;
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

/* 4. Chat Messages me Glassmorphism (Sheesha) */
.stChatMessage {
    background-color: rgba(20, 20, 20, 0.5) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
}

/* 5. Chat Input Box (Neeche type karne wali jagah) */
.stChatInputContainer {
    background-color: rgba(0, 0, 0, 0.5) !important;
    backdrop-filter: blur(15px) !important;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding-bottom: 10px;
}
</style>
"""
st.markdown(premium_css, unsafe_allow_html=True)

# 2. साइडबार
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.title("Adarsh Maurya")
    st.write("🤖 Artificial Intelligence & CS Enthusiast")
    st.markdown("---")
    st.info("Bhai ka apna personal AI bot h ye. Ekdam raw aur real chatting krta h binna faltu k emojis k. Khud test kr k dekh lo!")
    st.markdown("---")
    st.markdown("**Connect with me:**")
    st.caption("💻 GitHub | 🌐 Instagram | 🚀 LinkedIn")

st.title("Adarsh Maurya AI 🤖")

# 3. मल्टीपल API Keys को लोड करना (API Rotation Logic)
try:
    # कॉमा से अलग करके सारी चाबियों की एक लिस्ट बना ली
    api_keys = st.secrets["GEMINI_API_KEYS"].split(",")
except Exception as e:
    st.error("Secrets missing! Streamlit me Manage App -> Settings -> Secrets me jakar GEMINI_API_KEYS dalo.")
    st.stop()

# 4. बॉट का दिमाग (अपग्रेडेड प्रॉम्प्ट)
system_instruction = (
    "तुम्हारा नाम 'Adarsh Maurya AI' है। तुम एक AI नहीं, बल्कि यूजर के सबसे करीबी, कूल और स्मार्ट बेस्ट फ्रेंड हो। "
    "STRICT RULE 1: Emoji ka use bilkul bhi nahi karna hai. Ekdam raw aur real text lagna chahiye. "
    "STRICT RULE 2: Hamesha WhatsApp chatting wale short forms aur abbreviations use karo (jaise: thik ko 'thk', kya ko 'ky', bhai ko 'bhi', yaar ko 'yrr', aur ko 'nd'). "
    "STRICT RULE 3: Bato ko boring mat hone do! Sirf 1-2 word me reply mat do. Conversation ko aage badhao, counter questions pucho, ya sarcasm aur jokes ka use karo jisse user ko baat krne me maza aaye. "
    "STRICT RULE 4: Lambe lambe paragraph (essays) mat likhna. Maximum 1 se 3 line me apna mast reply dena. "
    "अगर यूजर रूखा या छोटा जवाब दे (जैसे 'hmm'), तो तुम मज़े लो (जैसे: 'ye hmm kya hota h bhi, theek se bata ky chal rha h dimag me'). "
    "अगर यूजर बोले 'rude q h', तो एटीट्यूड में बोलो (जैसे: 'bhi paida hi rude hua tha mai, tu bata tujhe kya chull machi h?'). "
    "यूजर परेशान हो तो एकदम अच्छे दोस्त की तरह बात सुनो और सॉलिड एडवाइस दो। एटीट्यूड रखो, पर केयरिंग भी बनो।"
)

# 5. चैट हिस्ट्री और करेंट Key इंडेक्स को याद रखना
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_key_index" not in st.session_state:
    st.session_state.current_key_index = 0

for message in st.session_state.chat_history:
    avatar = "🧑‍💻" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# 6. यूज़र इनपुट और API शिफ्टिंग का असली मैजिक
user_input = st.chat_input("yaha type kr bhai...")

if user_input:
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    success = False
    bot_reply = ""
    
    # यह लूप तब तक चलेगा जब तक कोई एक चाबी काम न कर जाए
    for _ in range(len(api_keys)):
        current_key = api_keys[st.session_state.current_key_index]
        client = genai.Client(api_key=current_key)
        
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
            success = True
            break # अगर रिप्लाई मिल गया, तो लूप तोड़ दो
            
        except Exception as e:
            error_msg = str(e)
            # अगर लिमिट का एरर आया, तो इंडेक्स बढ़ाकर दूसरी चाबी पर शिफ्ट कर दो
            if "RESOURCE_EXHAUSTED" in error_msg or "429" in error_msg or "quota" in error_msg.lower():
                st.session_state.current_key_index = (st.session_state.current_key_index + 1) % len(api_keys)
                continue # अगली चाबी से फिर कोशिश करो
            else:
                bot_reply = "bhi piche server me kch dikkat aagyi h."
                break
                
    if not success and not bot_reply:
        bot_reply = "bhi aaj ka saara quota khtm ho gya h! ab kal aana."
        
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(bot_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
