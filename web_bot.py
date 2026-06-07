import streamlit as st
import streamlit.components.v1 as components
from google import genai
from google.genai import types
from PIL import Image

# 1. पेज का प्रीमियम डिज़ाइन
st.set_page_config(page_title="Adarsh AI Pro", page_icon="🧑‍💻", layout="wide")

# 2. मल्टीपल API Keys को लोड करना (API Rotation Logic)
try:
    api_keys = st.secrets["GEMINI_API_KEYS"].split(",")
except Exception as e:
    st.error("Secrets missing! Streamlit me Manage App -> Settings -> Secrets me jakar GEMINI_API_KEYS dalo.")
    st.stop()

if "current_key_index" not in st.session_state:
    st.session_state.current_key_index = 0

# 3. साइडबार - नेविगेशन मेन्यू (Super App Logic)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
    st.title("Adarsh Maurya")
    st.write("🤖 Artificial Intelligence & CS Enthusiast")
    st.markdown("---")
    
    # NAVIGATION MENU
    st.subheader("Explore Zones")
    app_mode = st.radio("Select Vibe:", ["🤖 AI & Creative Zone", "🗑️ The Mental Flush"], label_visibility="collapsed")
    st.markdown("---")
    
    st.markdown("**Connect with me:**")
    st.caption("💻 GitHub | 🌐 Instagram | 🚀 LinkedIn")


# ==========================================
# 🌌 ZONE 1: AI & CREATIVE ZONE (New Design & Voice)
# ==========================================
if app_mode == "🤖 AI & Creative Zone":
    
    # 🟢 NEW: ZZone 1 का UI CSS (Black/Yellow theme & Dark Voice)
    premium_css = """
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    
    /* Dark Calming Background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364); 
        background-size: cover; background-attachment: fixed;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] { background-color: rgba(10, 10, 10, 0.3) !important; backdrop-filter: blur(15px); }
    [data-testid="stSidebar"] * { color: #ffffff !important; }
    
    /* General Text safed */
    h1, h2, h3, p, span, div { color: #ffffff !important; }
    
    /* Chat Messages styling */
    .stChatMessage {
        background-color: rgba(20, 20, 20, 0.4) !important; backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 15px; padding: 15px; margin-bottom: 15px; color: white !important;
    }
    
    /* Bottom Text Chat Input styling */
    .stChatInputContainer { border: 2px solid #000000 !important; border-radius: 15px !important; background-color: #ffffff !important; }
    textarea { color: #000000 !important; -webkit-text-fill-color: #000000 !important; }
    textarea::placeholder { color: #000000 !important; opacity: 0.9 !important; }
    [data-testid="stChatInputSubmitButton"] { color: #000000 !important; }
    [data-testid="stChatInputSubmitButton"] svg { fill: #000000 !important; }
    
    /* 🟡 NEW: File Uploader (Black/Yellow Inside) */
    [data-testid="stFileUploader"] { 
        background-color: #000000 !important; /* Bahar ka box black */
        border-radius: 12px; padding: 10px !important; 
        border: 2px dashed #ffff00 !important; /* Pila dash border */
    }
    [data-testid="stFileUploadDropzone"] { 
        background-color: #000000 !important; /* Andar ka area black */
        border-radius: 8px !important;
    }
    /* Dropzone ke andar ka text aur SVG icon (Neon Yellow) */
    [data-testid="stFileUploadDropzone"] * { 
        color: #ffff00 !important; 
        fill: #ffff00 !important; 
        font-weight: 700 !important; 
    }
    [data-testid="stFileUploadDropzone"] button {
         background-color: #ffff00 !important; /* Button pila */
         border-color: #ffff00 !important;
    }
    [data-testid="stFileUploadDropzone"] button * {
        color: #000000 !important; /* Button text kaala for contrast */
    }

    /* 🎤 NEW: Dark Styling for Voice Box in Zone 1 */
    .stAudioInput {
        background-color: rgba(10, 10, 10, 0.6) !important;
        border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1);
        color: white !important;
    }
    .stAudioInput * { color: #ffffff !important; fill: #ffffff !important;}
    </style>
    """
    st.markdown(premium_css, unsafe_allow_html=True)

    # टॉप लेआउट: टाइटल और मिनी गेम
    col1, col3 = st.columns([0.65, 0.35])

    with col1:
        st.title("Adarsh Maurya AI 🤖")

    with col3:
        # Mini Game JavaScript
        game_html = """
        <!DOCTYPE html>
        <html><head><style>
          canvas { border: 1px solid rgba(255,255,255,0.2); background-color: rgba(10,10,10,0.5); border-radius: 10px; cursor: pointer; display: block; margin-top: 15px;}
          body { margin: 0; overflow: hidden; display: flex; justify(content): right;}
        </style></head><body>
        <canvas id="gameCanvas" width="280" height="80"></canvas>
        <script>
          const canvas = document.getElementById("gameCanvas"); const ctx = canvas.getContext("2d");
          let player = { x: 30, y: 50, width: 15, height: 15, dy: 0, gravity: 0.6, jumpPower: -8, isJumping: false };
          let obstacle = { x: 280, y: 50, width: 15, height: 15, dx: -4 };
          let score = 0; let isGameOver = false; let gameStarted = false; 
          let highScore = localStorage.getItem('adarshHighScore') || 0;

          function draw() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = "rgba(255, 255, 255, 0.7)"; ctx.font = "12px Arial"; ctx.fillText("Score: " + Math.floor(score), 10, 20);
            ctx.fillStyle = "rgba(255, 215, 0, 0.9)"; ctx.fillText("HI: " + Math.floor(highScore), 210, 20);

            if (!gameStarted) {
                ctx.fillStyle = "#00e5ff"; ctx.fillRect(player.x, player.y, player.width, player.height);
                ctx.fillStyle = "#ff003c"; ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
                ctx.fillStyle = "white"; ctx.font = "bold 16px Arial"; ctx.fillText("▶ START", 105, 45);
                return; 
            }
            if (isGameOver) { ctx.fillStyle = "white"; ctx.font = "12px Arial"; ctx.fillText("Game Over! Tap to Restart", 65, 45); return; }
            
            ctx.fillStyle = "#00e5ff"; ctx.fillRect(player.x, player.y, player.width, player.height);
            ctx.fillStyle = "#ff003c"; ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
            
            player.y += player.dy; if (player.y < 50) { player.dy += player.gravity; } else { player.y = 50; player.dy = 0; player.isJumping = false; }
            obstacle.x += obstacle.dx; if (obstacle.x < -20) { obstacle.x = canvas.width; obstacle.dx -= 0.1; }
            score += 0.1;
            
            if (player.x < obstacle.x + obstacle.width && player.x + player.width > obstacle.x && player.y < obstacle.y + obstacle.height && player.y + player.height > obstacle.y) { 
                isGameOver = true; 
                if (score > highScore) { highScore = score; localStorage.setItem('adarshHighScore', highScore); }
            }
            requestAnimationFrame(draw);
          }
          function jump(e) {
            if(e && e.type === "keydown" && e.code !== "Space") return;
            if (e && e.type === "keydown") e.preventDefault();
            if (!gameStarted) { gameStarted = true; draw(); return; }
            if (!player.isJumping && !isGameOver) { player.dy = player.jumpPower; player.isJumping = true; } 
            else if (isGameOver) { obstacle.x = canvas.width; obstacle.dx = -4; score = 0; isGameOver = false; draw(); }
          }
          window.addEventListener("keydown", jump); canvas.addEventListener("mousedown", jump); canvas.addEventListener("touchstart", jump);
          draw(); 
        </script>
        </body></html>
        """
        components.html(game_html, height=100)

    st.markdown("---")
    
    # 🟡 NEW: Image Section (Aesthetic Purple Upload Zone)
    st.markdown("### ✨ Shayari ke liye Photo dalein")
    uploaded_photo = st.file_uploader("➕ Upload Image", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    
    # Photo-to-Poetry Logic
    if uploaded_photo is not None:
        img = Image.open(uploaded_photo)
        
        # 🎤 NEW Voice Wala Box (Zone 1) - Dark Styled Box
        st.markdown("""
            <div style="background-color: rgba(10, 10, 10, 0.7); padding: 25px; border-radius: 15px; border: 1px solid rgba(255,255,255,0.1); text-align: center; margin-bottom: 20px;">
                <h4 style="color: #ffffff; margin-bottom: 15px;">Bol kr bhi bata skte ho... (Optional)</h4>
                <p style="color: gray; font-size: 14px;">Type karne ki zarurat nahi...</p>
            </div>
        """, unsafe_allow_html=True)
        # Voice Input Component
        audio_prompt_zone1 = st.audio_input("Bol ke type kro", key="zone1_voice_input")

        p_col1, p_col2 = st.columns([0.2, 0.8])
        with p_col1: st.image(img, caption="Vibe Check...", use_column_width=True)
        with p_col2:
            with st.spinner("tasveer ko padh kar vibe samajh raha hu..."):
                # Use standard Hinglish prompt. Logic can be added later for transcription if needed.
                shayari_prompt = "1. Pyaara compliment do. 2. Space chhod kar, 2-4 line ki aasan Hindi me Urdu words (sukoon, noor) mix karke deep shayari likho. Text Devnagari me ho."
                success = False
                for _ in range(len(api_keys)):
                    try:
                        client = genai.Client(api_key=api_keys[st.session_state.current_key_index])
                        response = client.models.generate_content(model='gemini-2.5-flash', contents=[img, shayari_prompt])
                        st.markdown(f"<div style='background: rgba(15,15,15,0.6); padding: 30px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.15); text-align: center; font-family: Georgia, serif; font-size: 2.0rem; font-weight: 500; color: #f1f5f9;'><i>{response.text.replace(chr(10), '<br>')}</i></div>", unsafe_allow_html=True)
                        success = True
                        break
                    except Exception:
                        st.session_state.current_key_index = (st.session_state.current_key_index + 1) % len(api_keys)
                if not success: st.error("API limit khatam.")
        st.markdown("---")

    # Bot Brain Prompt
    system_instruction = "तुम्हारा नाम 'Adarsh Maurya AI' है। एकदम WhatsApp वाले short forms (thk, kya, bhi) use karo. Emoji mat lagao. Sarcasm aur jokes ka use karo. Conversation ko aage badhao, counter questions pucho. essays mat likho, max 1-3 lines."
    
    # Initialize Chat
    if "chat_history" not in st.session_state: st.session_state.chat_history = []
    
    # Display History
    for msg in st.session_state.chat_history:
        avatar = "🧑‍💻" if msg["role"] == "user" else "🤖"
        with st.chat_message(msg["role"], avatar=avatar): st.markdown(msg["content"])
    
    # Input
    user_input = st.chat_input("yaha type kr bhai...")
    
    # API shifting Logic for Chat
    if user_input:
        with st.chat_message("user", avatar="🧑‍💻"): st.markdown(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        chat_success = False
        for _ in range(len(api_keys)):
            try:
                client = genai.Client(api_key=api_keys[st.session_state.current_key_index])
                response = client.models.generate_content(model='gemini-2.5-flash', contents=user_input, config=types.GenerateContentConfig(system_instruction=system_instruction, temperature=0.7))
                with st.chat_message("assistant", avatar="🤖"): st.markdown(response.text)
                st.session_state.chat_history.append({"role": "assistant", "content": response.text})
                chat_success = True
                break
            except Exception:
                st.session_state.current_key_index = (st.session_state.current_key_index + 1) % len(api_keys)
        if not chat_success: st.error("Quota Over!")


# ==========================================
# 🗑️ ZONE 2: THE MENTAL FLUSH (Vent Zone - No Change)
# ==========================================
elif app_mode == "🗑️ The Mental Flush":

    # Is page ka ekdam Dark, Void, Cinematic CSS
    flush_css = """
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    [data-testid="stAppViewContainer"] {
        background-color: #050505; /* Ekdam andhera (Void) */
        color: #ffffff;
    }
    [data-testid="stSidebar"] { background-color: rgba(10, 10, 10, 0.6) !important; backdrop-filter: blur(15px); border-right: 1px solid rgba(255, 255, 255, 0.05); }
    [data-testid="stSidebar"] * { color: #ffffff !important; }
    .flush-title { text-align: center; font-family: 'Courier New', monospace; font-size: 3rem; color: #444; text-shadow: 0 0 10px rgba(255,255,255,0.1); margin-bottom: 0px;}
    .flush-sub { text-align: center; color: #666; font-size: 1.2rem; margin-top: -10px; margin-bottom: 30px;}
    </style>
    """
    st.markdown(flush_css, unsafe_allow_html=True)
    
    st.markdown("<h1 class='flush-title'>THE MENTAL FLUSH</h1>", unsafe_allow_html=True)
    st.markdown("<p class='flush-sub'>Dump your mental garbage here. No one is judging.</p>", unsafe_allow_html=True)

    # DUSTBIN & ANIMATION LOGIC (HTML + JS + Audio)
    flush_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body { text-align: center; background: transparent; overflow: hidden; font-family: sans-serif; color: white;}
        .bin-container { position: relative; width: 400px; height: 350px; margin: 0 auto; overflow: hidden;}
        /* Dustbin Design */
        .dustbin { width: 140px; height: 160px; border: 4px solid #333; border-top: none; position: absolute; bottom: 10px; left: 130px; border-radius: 0 0 20px 20px; background: rgba(20,20,20,0.9); z-index: 10; cursor: pointer; transition: 0.3s; box-shadow: inset 0 -20px 30px rgba(0,0,0,0.8); }
        .dustbin:hover { box-shadow: 0 0 20px rgba(255,0,0,0.2); border-color: #555;}
        .lid { width: 150px; height: 12px; background: #444; position: absolute; top: -12px; left: -5px; border-radius: 5px; transform-origin: left; transition: transform 0.5s ease-in-out; }
        .dustbin.open .lid { transform: rotate(-75deg); background: #666;}
        /* Mic Design */
        .mic { position: absolute; font-size: 40px; top: 30px; left: 50px; opacity: 0; transition: 0.5s; z-index: 5; }
        .dustbin.open .mic { top: -60px; opacity: 1; animation: pulse 1.2s infinite alternate; }
        @keyframes pulse { 0% { transform: scale(1); text-shadow: 0 0 10px red;} 100% { transform: scale(1.1); text-shadow: 0 0 20px red;} }
        /* Word Animation */
        .word { position: absolute; font-size: 22px; font-weight: bold; color: #ff3333; opacity: 0; z-index: 2; text-shadow: 0 0 8px red; white-space: nowrap;}
        /* Button */
        #flushBtn { display: none; margin: 20px auto; padding: 15px 40px; background: #aa0000; color: white; border: 2px solid #ff0000; border-radius: 8px; font-size: 24px; cursor: pointer; font-family: 'Courier New', monospace; font-weight: bold; box-shadow: 0 0 15px rgba(255,0,0,0.5); transition: 0.3s;}
        #flushBtn:hover { background: #ff0000; transform: scale(1.05); box-shadow: 0 0 30px rgba(255,0,0,0.8); }
        #statusText { font-size: 16px; color: #888; margin-top: 10px; transition: 0.5s;}
    </style>
    </head>
    <body>

    <p id="statusText">Tap the dustbin to open the lid and activate the mic.</p>
    
    <div class="bin-container" id="container">
        <div class="dustbin" id="bin" onclick="toggleBin()">
            <div class="lid"></div>
            <div class="mic">🎙️</div>
        </div>
    </div>
    
    <button id="flushBtn" onclick="flushIt()">⚠️ DESTROY & FLUSH</button>

    <!-- Hidden Sound Effects -->
    <audio id="boomSound" src="https://assets.mixkit.co/active_storage/sfx/119/119-preview.mp3"></audio>
    <audio id="flushSound" src="https://assets.mixkit.co/active_storage/sfx/2568/2568-preview.mp3"></audio>

    <script>
        let bin = document.getElementById('bin');
        let statusText = document.getElementById('statusText');
        let flushBtn = document.getElementById('flushBtn');
        let boom = document.getElementById('boomSound');
        let flush = document.getElementById('flushSound');
        let isOpen = false;
        let recognition;
        let wordsDropped = 0;

        // Speech API Setup (Chrome only)
        if ('webkitSpeechRecognition' in window) {
            recognition = new webkitSpeechRecognition();
            recognition.continuous = true;
            recognition.interimResults = false;
            recognition.lang = 'hi-IN'; // Understands Hindi & Hinglish
            
            recognition.onresult = function(event) {
                for (let i = event.resultIndex; i < event.results.length; ++i) {
                    if (event.results[i].isFinal) {
                        let text = event.results[i][0].transcript.trim();
                        let words = text.split(' ');
                        words.forEach((w, index) => {
                            setTimeout(() => dropWord(w), index * 400); // Ek ek karke word girenge
                        });
                        wordsDropped += words.length;
                        
                        // Jaise hi kuch bola, thodi der baad Flush button dikha do
                        if(wordsDropped > 0 && isOpen) {
                            setTimeout(() => {
                                flushBtn.style.display = "block";
                            }, 1500);
                        }
                    }
                }
            };
            recognition.onerror = function(e) { console.log("Mic error:", e.error); }
        } else {
            statusText.innerText = "Bhai tera browser Speech API support nahi karta. Chrome use kar.";
        }

        function toggleBin() {
            if(!isOpen) {
                bin.classList.add('open');
                statusText.innerText = "Speak your heart out. Your words are flowing into the trash...";
                statusText.style.color = "#ff6666";
                isOpen = true;
                if(recognition) {
                    try { recognition.start(); } catch (e) { console.log("Already started"); }
                }
            } else {
                bin.classList.remove('open');
                statusText.innerText = "Bin Locked. Ready to Destroy?";
                statusText.style.color = "#888";
                isOpen = false;
                if(recognition) {
                    try { recognition.stop(); } catch (e) { console.log("Already stopped"); }
                }
            }
        }

        function dropWord(text) {
            let w = document.createElement('div');
            w.className = 'word';
            w.innerText = text;
            
            // Start position randomly on top
            let startX = 50 + Math.random() * 200; 
            w.style.left = startX + 'px';
            w.style.top = '0px';
            document.getElementById('container').appendChild(w);

            let startTime = performance.now();
            function animate(time) {
                let elapsed = time - startTime;
                let progress = elapsed / 2500; // Falling speed
                if (progress > 1) progress = 1;
                
                // Y-axis: Falls down
                let y = progress * 300;
                
                // X-axis: Sine Wave motion
                let x = startX + Math.sin(progress * Math.PI * 6) * 40; 
                
                // Funnel effect: Center inside bin at end
                if (progress > 0.7) { x = x + (180 - x) * ((progress - 0.7) * 3.33); }

                w.style.transform = `translate(${x - startX}px, ${y}px)`;
                
                // Fade in/out
                if(progress < 0.2) w.style.opacity = progress * 5;
                else if (progress > 0.8) w.style.opacity = (1 - progress) * 5;
                else w.style.opacity = 1;

                if (progress < 1) { requestAnimationFrame(animate); } else { w.remove(); }
            }
            requestAnimationFrame(animate);
        }

        function flushIt() {
            if(recognition) recognition.stop();
            bin.classList.remove('open');
            isOpen = false;
            
            boom.play();
            setTimeout(() => flush.play(), 600);
            
            // Screen Shake Animation
            document.body.animate([
                { transform: 'translate(5px, 5px) rotate(0deg)' },
                { transform: 'translate(-5px, -5px) rotate(-1deg)' },
                { transform: 'translate(-5px, 5px) rotate(1deg)' },
                { transform: 'translate(5px, -5px) rotate(0deg)' },
                { transform: 'translate(0px, 0px) rotate(0deg)' }
            ], { duration: 150, iterations: 6 });

            // Success Message
            flushBtn.style.display = "none";
            statusText.innerText = "The garbage has been cleared. Take a deep breath. You are light now. 🌊";
            statusText.style.color = "#00e5ff";
            
            // Reset
            setTimeout(() => {
                statusText.innerText = "Tap the dustbin to open the lid and activate the mic.";
                statusText.style.color = "#888";
                wordsDropped = 0;
            }, 6000);
        }
    </script>
    </body>
    </html>
    """
    components.html(flush_html, height=480)

    st.markdown("---")
    
    # 🧠 THE ADVICE ZONE (Empathetic Jugaad AI Friend)
    st.markdown("<h3 style='text-align: center; color: #555;'>Too heavy to flush? Let's talk it out.</h3>", unsafe_allow_html=True)
    
    if "advice_history" not in st.session_state: st.session_state.advice_history = []
    for msg in st.session_state.advice_history:
        avatar = "🧑‍💻" if msg["role"] == "user" else "🧠"
        with st.chat_message(msg["role"], avatar=avatar): st.markdown(msg["content"])

    advice_input = st.chat_input("I need advice...")
    if advice_input:
        with st.chat_message("user", avatar="🧑‍💻"): st.markdown(advice_input)
        st.session_state.advice_history.append({"role": "user", "content": advice_input})
        advice_system = (
            "You are a highly empathetic, wise, and calm psychologist/friend. Acknowledge user's pain gently. "
            "Provide practical, grounded, realistic Hinglish 'jugaad' solutions to help anxiety. essys mat likho, conversational short replies."
        )
        advice_success = False
        for _ in range(len(api_keys)):
            try:
                client = genai.Client(api_key=api_keys[st.session_state.current_key_index])
                response = client.models.generate_content(model='gemini-2.5-flash', contents=advice_input, config=types.GenerateContentConfig(system_instruction=advice_system, temperature=0.6))
                with st.chat_message("assistant", avatar="🧠"): st.markdown(response.text)
                st.session_state.advice_history.append({"role": "assistant", "content": response.text})
                advice_success = True
                break
            except Exception:
                st.session_state.current_key_index = (st.session_state.current_key_index + 1) % len(api_keys)
        if not advice_success: st.error("Quota Over.")
