import streamlit as st
import streamlit.components.v1 as components
from google import genai
from google.genai import types
from PIL import Image

# 1. पेज का प्रीमियम डिज़ाइन
st.set_page_config(page_title="Adarsh AI Pro", page_icon="🧑‍💻", layout="wide")

# 2. PREMIUM UI (Aesthetic Calming Background & Glassmorphism)
premium_css = """
<style>
/* Watermark aur upar/neeche ka menu gayab karo */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Dark Aesthetic & Calming Background (Aankho ko sukoon dene wala) */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); /* Deep calming midnight vibe */
    background-size: cover;
    background-attachment: fixed;
}

/* Transparent Sidebar (Glass Effect) */
[data-testid="stSidebar"] {
    background-color: rgba(10, 10, 10, 0.3) !important;
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

/* Sidebar aur sabhi text ko safed (White) karna */
[data-testid="stSidebar"] * {
    color: #ffffff !important;
}
h1, h2, h3, p, span, div {
    color: #ffffff !important;
}

/* Chat Messages me Glassmorphism */
.stChatMessage {
    background-color: rgba(20, 20, 20, 0.4) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
    color: white !important;
}

/* Chat Input Box (Fixed for White Bottom) */
.stChatInputContainer {
    border: 2px solid #000000 !important; 
    border-radius: 15px !important;
    background-color: #ffffff !important; 
}
textarea {
    color: #000000 !important; 
    -webkit-text-fill-color: #000000 !important;
}
textarea::placeholder {
    color: #000000 !important; 
    opacity: 0.9 !important;
}
[data-testid="stChatInputSubmitButton"] {
    color: #000000 !important;
}
[data-testid="stChatInputSubmitButton"] svg {
    fill: #000000 !important;
}

/* File Uploader styling (Chota aur compact) */
[data-testid="stFileUploader"] {
    background-color: rgba(20,20,20,0.4) !important;
    border-radius: 10px;
    padding: 5px;
    border: 1px solid rgba(255,255,255,0.2);
}
</style>
"""
st.markdown(premium_css, unsafe_allow_html=True)

# 3. साइडबार
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.title("Adarsh Maurya")
    st.write("🤖 Artificial Intelligence & CS Enthusiast")
    st.markdown("---")
    st.info("Bhai ka apna personal AI bot h ye. Ekdam raw aur real chatting krta h binna faltu k emojis k.")
    st.markdown("---")
    st.markdown("**Connect with me:**")
    st.caption("💻 GitHub | 🌐 Instagram | 🚀 LinkedIn")

# 4. मल्टीपल API Keys को लोड करना
try:
    api_keys = st.secrets["GEMINI_API_KEYS"].split(",")
except Exception as e:
    st.error("Secrets missing! API keys dalo.")
    st.stop()

if "current_key_index" not in st.session_state:
    st.session_state.current_key_index = 0

# 5. टॉप लेआउट: टाइटल, प्लस आइकन (Uploader) और मिनी गेम
col1, col2, col3 = st.columns([0.4, 0.25, 0.35])

with col1:
    st.title("Adarsh Maurya AI 🤖")

with col2:
    # Game ke theek left me plus icon wala uploader
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    uploaded_photo = st.file_uploader("➕ Shayari ke liye Photo dalein", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

with col3:
    # JavaScript + HTML Mini Game (Jumping Box)
    game_html = """
    <!DOCTYPE html>
    <html><head><style>
      canvas { border: 1px solid rgba(255,255,255,0.2); background-color: rgba(10,10,10,0.5); border-radius: 10px; cursor: pointer; display: block; margin-top: 15px;}
      body { margin: 0; overflow: hidden; display: flex; justify-content: right;}
    </style></head><body>
    <canvas id="gameCanvas" width="280" height="80"></canvas>
    <script>
      const canvas = document.getElementById("gameCanvas"); const ctx = canvas.getContext("2d");
      let player = { x: 30, y: 50, width: 15, height: 15, dy: 0, gravity: 0.6, jumpPower: -8, isJumping: false };
      let obstacle = { x: 280, y: 50, width: 15, height: 15, dx: -4 };
      let score = 0; let isGameOver = false;

      function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "rgba(255, 255, 255, 0.7)"; ctx.font = "12px Arial"; ctx.fillText("Score: " + Math.floor(score), 10, 20);
        if (isGameOver) { ctx.fillStyle = "white"; ctx.fillText("Game Over! Tap to Restart", 65, 45); return; }
        if (score < 10) { ctx.fillStyle = "rgba(255, 255, 255, 0.3)"; ctx.fillText("Space / Tap to Jump", 150, 20); }
        
        ctx.fillStyle = "#00e5ff"; ctx.fillRect(player.x, player.y, player.width, player.height);
        ctx.fillStyle = "#ff003c"; ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
        
        player.y += player.dy;
        if (player.y < 50) { player.dy += player.gravity; } else { player.y = 50; player.dy = 0; player.isJumping = false; }
        
        obstacle.x += obstacle.dx;
        if (obstacle.x < -20) { obstacle.x = canvas.width; obstacle.dx -= 0.1; }
        score += 0.1;
        
        if (player.x < obstacle.x + obstacle.width && player.x + player.width > obstacle.x &&
            player.y < obstacle.y + obstacle.height && player.y + player.height > obstacle.y) { isGameOver = true; }
        requestAnimationFrame(draw);
      }
      function jump(e) {
        if(e && e.type === "keydown" && e.code !== "Space") return;
        if (e && e.type === "keydown") e.preventDefault();
        if (!player.isJumping && !isGameOver) { player.dy = player.jumpPower; player.isJumping = true; } 
        else if (isGameOver) { obstacle.x = canvas.width; obstacle.dx = -4; score = 0; isGameOver = false; draw(); }
      }
      window.addEventListener("keydown", jump); canvas.addEventListener("mousedown", jump); canvas.addEventListener("touchstart", jump);
      draw();
    </script>
    </body></html>
    """
    components.html(game_html, height=100)

# 6. ✨ द शायरी इंजन (Vision AI with Compliment & Vibe Check) ✨
if uploaded_photo is not None:
    img = Image.open(uploaded_photo)
    st.markdown("---")
    
    p_col1, p_col2 = st.columns([0.2, 0.8])
    with p_col1:
        st.image(img, caption="Vibe Check...", use_column_width=True)
        
    with p_col2:
        with st.spinner("tasveer ko padh kar vibe samajh raha hu..."):
            shayari_text = ""
            # Updated Prompt: Pehle compliment, phir simple hindi me urdu words ke sath shayari
            shayari_prompt = (
                "Is photo ki vibe, emotion aur khubsurti ko dhyan se samjho. "
                "1. Sabse pehle photo ki vibe ke hisaab se ek chota sa pyaara aur modern compliment do (jaise: 'Wow, behad khubsurat tasveer!', 'Kya aesthetic vibe hai!', ya 'Badi sukoon bhari photo hai'). "
                "2. Fir ek line ka space chhod kar, 2 se 4 line ki ek deep aur aakhon me bas jane wali shayari likho. "
                "3. Shayari ki bhasha bilkul aasan Hindi honi chahiye jo aasaani se samajh aaye, lekin usme 'sukoon', 'noor', 'qurbat' jaise pyare Urdu lafz zaroor mix hon taaki vibe aaye. "
                "4. Pura text Devnagari script (Hindi alphabets) aur thodi bahut Hinglish me hona chahiye. Faltu ka koi explanation mat likhna."
            )
            
            success = False
            for _ in range(len(api_keys)):
                current_key = api_keys[st.session_state.current_key_index]
                client = genai.Client(api_key=current_key)
                try:
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[img, shayari_prompt]
                    )
                    shayari_text = response.text
                    success = True
                    break
                except Exception:
                    st.session_state.current_key_index = (st.session_state.current_key_index + 1) % len(api_keys)
                    continue
            
            if success:
                # 🟢 BADE SHABDON WALA ELEGANT BOX (Font Size Increased)
                elegant_box = f"""
                <div style="
                    background-color: rgba(15, 15, 15, 0.6); 
                    padding: 30px; 
                    border-radius: 12px; 
                    border: 1px solid rgba(255, 255, 255, 0.15); 
                    text-align: center; 
                    font-family: 'Georgia', serif; 
                    font-size: 2.0rem;  /* Bade aur clear font ke liye 2.0rem */
                    font-weight: 500;
                    line-height: 1.8; 
                    color: #f1f5f9;
                    box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
                    margin-top: 10px;
                ">
                    <i>{shayari_text.replace(chr(10), '<br>')}</i>
                </div>
                """
                st.markdown(elegant_box, unsafe_allow_html=True)
            else:
                st.error("Bhai API limit khatam ho gayi hai photo padhne ki.")
    st.markdown("---")


# 7. बॉट का दिमाग (चैट प्रॉम्प्ट)
system_instruction = (
    "तुम्हारा नाम 'Adarsh Maurya AI' है। तुम एक AI नहीं, बल्कि यूजर के सबसे करीबी, कूल और स्मार्ट बेस्ट फ्रेंड हो। "
    "STRICT RULE 1: Emoji ka use bilkul bhi nahi karna hai. Ekdam raw aur real text lagna chahiye. "
    "STRICT RULE 2: Hamesha WhatsApp chatting wale short forms aur abbreviations use karo. "
    "STRICT RULE 3: Bato ko boring mat hone do! Sirf 1-2 word me reply mat do. Conversation ko aage badhao, sarcasm aur jokes ka use karo. "
    "STRICT RULE 4: Lambe paragraph mat likhna. Maximum 1 se 3 line me apna mast reply dena. "
)

# 8. चैट हिस्ट्री और यूज़र इनपुट (API Rotation Logic ke sath)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    avatar = "🧑‍💻" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

user_input = st.chat_input("yaha type kr bhai...")

if user_input:
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    chat_success = False
    bot_reply = ""
    
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
            chat_success = True
            break
        except Exception:
            st.session_state.current_key_index = (st.session_state.current_key_index + 1) % len(api_keys)
            continue
                
    if not chat_success:
        bot_reply = "bhi aaj ka saara quota khtm ho gya h! ab kal aana."
        
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(bot_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
