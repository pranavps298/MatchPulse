# 🏏 MatchPulse AI — Live Tactical & Fantasy Match Companion
> **Deployed and accessible via** : https://matchpulse-78o8.onrender.com/ 
> **Dream11 Forward Deployed Engineer (FDE) Intern Assignment**  
> *Author:* Pranav P S ([@pranavps298](https://github.com/pranavps298))  
> *Submission Form:* [Dream11 Assignment Submission](https://forms.gle/s3dxPxAd8Jw7w3an7)

---

## 📋 The Official Submission Note (< 200 Words)

> **What fan problem are you solving?**  
> During live cricket matches, fans face context blindness and second-screen fatigue. Broadcast commentary is generic, scorecards only show cold numbers, and fans tuning in late (e.g. over 15) struggle to reconstruct why momentum swung. Concurrently, millions of Dream11 fantasy players cannot visualize the real-time fantasy point impact or captaincy leverage of micro-events (e.g. death-over dot balls vs boundary traps).  
>  
> **How does your solution help?**  
> MatchPulse AI provides a live tactical & fantasy companion with:  
> 1. *"Catch Me Up in 10s"*, generating an instant 3-bullet narrative on game state, tactical pivots, and what to watch next.  
> 2. *Tactical Ball Decrypter*, decoding delivery physics, seam movement, and batter matchup flaws.  
> 3. *Fantasy Leverage Radar*, tracking live Dream11 point swings and captaincy multipliers.  
> 4. *Dugout AI Copilot* for real-time natural language fan Q&A.  
>  
> **Which AI tools did you use?**  
> Google Gemini 1.5 Flash API (with prompt-engineered live match context injection), domain-driven heuristic tactical evaluation engines, dynamic Win Probability regression modeling, and Flask + Tailwind CSS with Web Audio API for interactive broadcast playback.

*(Word Count: 182 words — strictly within the 200-word limit)*

---

## ⚡ What is MatchPulse AI?

MatchPulse AI transforms the passive sports viewing experience into an interactive, intelligence-driven command center. Built specifically with the **Dream11 Forward Deployed Engineer** ethos, it bridges live match emotions with tactical physics and fantasy sports decision-making.

### 🌟 Core Capabilities
1. **⚡ Catch Me Up in 10s (Smart Catch-Up Engine)**:
   - For fans who were stuck in traffic, meetings, or stepped away for 10 overs.
   - Automatically breaks down the storyline into 3 sharp digest bullets: *The Match Story*, *The Tactical Pivot*, and *Next 12 Balls Watchlist*.
2. **🧠 Tactical Ball Decrypter ("Why Did That Happen?")**:
   - Goes beyond superficial broadcast commentary.
   - Decodes bowler release velocity, pitch length (e.g. 6.8m Good Length), line, field placement traps, and matchup statistics (e.g., *Klaasen strike rate vs 125 km/h off-cutters drops to 112*).
   - Features an interactive **Mini Pitch Impact Radar** visualizing ball landing coordinates.
3. **🎯 Dream11 Fantasy Leverage Radar**:
   - Calculates real-time fantasy point deltas for every dot ball, boundary, and dismissal.
   - Tracks **Captain / Vice-Captain (2x / 1.5x) leverage swings** across millions of user fantasy lineups.
   - Dynamic Live Match MVP leaderboard.
4. **🎙️ Dugout AI Copilot**:
   - Interactive conversational assistant answering tactical and fantasy queries in real time.
   - Dual-engine architecture:
     - **Live Mode**: Calls Google Gemini API when an API key is provided.
     - **Offline Resilient Mode**: Built-in heuristic cricket domain expert engine ensuring **zero latency, zero 500 errors, and 100% reliability** during live interview demos.
5. **🔴 Real-Time Live Ball Ingestion Engine**:
   - Fans or API webhooks can stream *any* live ball from ongoing international or domestic matches.
   - Ingesting a ball dynamically updates pitch physics, Win Probability curves, Dream11 points, and feeds the Dugout AI Copilot instantly!
6. **🏏 Complete Match Datasets & Synthesized Stadium Audio**:
   - **IND vs SA — T20 World Cup 2024 Final** (Complete **36-ball** sequence: Over 15 Klaasen 24-run assault on Axar $\to$ Hardik breakthrough $\to$ Bumrah magic $\to$ Surya's iconic catch).
   - **RCB vs CSK — IPL 2024 Playoff Decider** (Complete **24-ball** death phase: Lockie Ferguson 149 km/h bouncers $\to$ Green removing Dube $\to$ Siraj over $\to$ Yash Dayal's final over vs Dhoni).
   - Web Audio API synthesizer generating stadium atmosphere, bat cracks, and wicket cheers without external audio file dependencies.

---

## 🏗️ Architecture & Technology Stack

```
   ┌─────────────────────────────────────────────────────────┐
   │                  MatchPulse Web UI                      │
   │  (HTML5 / Tailwind CSS / Chart.js / Web Audio API)      │
   └──────────────────────────┬──────────────────────────────┘
                              │ REST JSON API
   ┌──────────────────────────▼──────────────────────────────┐
   │                  Flask 3.1 Backend                      │
   │                     (app.py)                            │
   └─────────────┬───────────────────────────┬───────────────┘
                 │                           │
   ┌─────────────▼─────────────┐ ┌───────────▼───────────────┐
   │    Match & Ball Physics   │ │      MatchPulse AI Engine │
   │       (data/matches.py)   │ │       (ai_engine.py)      │
   └───────────────────────────┘ └───────┬───────────┬───────┘
                                         │           │
                     ┌───────────────────▼──┐     ┌──▼──────────────────┐
                     │ Google Gemini API    │     │ Tactical Domain     │
                     │ (gemini-1.5-flash)   │     │ Heuristic Engine    │
                     └──────────────────────┘     │ (100% Offline Safe) │
                                                  └─────────────────────┘
```

- **Backend**: Python 3.13, Flask 3.1, Flask-CORS, Requests, Python-dotenv
- **Frontend**: Responsive Tailwind CSS (Stadium Dark Mode), Vanilla JavaScript, Chart.js, Lucide Icons, HTML5 Web Audio API
- **AI / Modeling**: Google Gemini 1.5 Flash + Heuristic Win Predictor & Tactical Matchup Knowledge Engine

---

## 🚀 Quickstart: Run Locally

### 1. Clone & Navigate
```bash
git clone https://github.com/pranavps298/CricketAI.git
cd CricketAI
```

### 2. Install Dependencies (or use existing Python environment)
```bash
pip install -r requirements.txt
```

### 3. Launch the Server
```bash
python app.py
```
Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser!

### 4. Run Automated Verification Tests
```bash
python test_api.py
```
All 8 automated tests verify end-to-end endpoints, catch-up generation, fantasy leverage, and AI copilot accuracy.

---

## 🌐 Deploy to Cloud (Free in 2 Minutes)

### Option A: Render (Recommended)
1. Push this repository to GitHub: `git push -u origin main`
2. Go to [Render.com](https://render.com) $\to$ **New Web Service** $\to$ Connect your repo.
3. Configure:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app` (or `python app.py`)
4. Click **Deploy** to receive your live submission URL!

### Option B: Railway / PythonAnywhere
- For PythonAnywhere: Upload the folder, point the WSGI file to `app.py`, and your app is live.

---

## 🎙️ Virtual Demo Round Talking Points (For Interview)

When presenting to the Dream11 team during the demo round, structure your walkthrough as follows:

1. **The Fan-First Hook (60 seconds)**:
   - *"When watching sports, fans aren't looking at scorecards in isolation—they're reacting to tension, arguing in group chats, and stressing over their Dream11 rank. Traditional broadcasts give 1990s commentary ('They need boundaries here!'). MatchPulse bridges this gap by decoding the tactical WHY and connecting it to fantasy leverage."*
2. **Interactive Walkthrough (90 seconds)**:
   - Show **IND vs SA T20 WC Final at ball 15.1**: Click *Play*, watch Klaasen's wicket, point out how the *Tactical Decrypter* explains the off-cutter speed drop from 140 to 123 km/h.
   - Click **"Catch Me Up in 10s"** to show how late-joining fans get a 3-bullet briefing in under 5 seconds.
   - Highlight the **Fantasy Leverage Radar**: Show how Hardik and Bumrah's death wickets created a +74 pt swing for Captaincy selections.
   - Ask the **Dugout AI Copilot** a live question: *"Why did Bumrah bowl round the wicket to Jansen?"*
3. **Forward Deployed Engineer Mindset (30 seconds)**:
   - Explain your architectural decision for **dual-engine AI**: *"In production, LLM APIs can face rate limits or latency spikes. As an FDE, I designed a resilient fallback heuristic engine so that even if the API key is absent or offline, the user experience never degrades."*

---

## 📄 License
MIT License. Built with passion for Dream11.
