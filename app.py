"""
MatchPulse AI — Live Tactical & Fantasy Match Companion
Flask Backend Application
"""

import os
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from data.matches import MATCHES
from ai_engine import ai_engine
from live_service import live_service

app = Flask(__name__)
CORS(app)

# Cache for real live match states
LIVE_MATCH_CACHE = {}

# Load optional .env file if present
try:
    from dotenv import load_dotenv
    load_dotenv()
    if os.environ.get("GEMINI_API_KEY"):
        ai_engine.set_api_key(os.environ.get("GEMINI_API_KEY"))
    if os.environ.get("CRICAPI_KEY"):
        live_service.cricapi_key = os.environ.get("CRICAPI_KEY")
except Exception:
    pass

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "MatchPulse AI",
        "has_gemini_key": bool(ai_engine.gemini_api_key),
        "live_matches_available": len(LIVE_MATCH_CACHE)
    })

@app.route("/api/matches")
def get_matches():
    match_list = []
    
    # 1. Fetch real-world live matches from LiveCricketService
    try:
        real_lives = live_service.fetch_live_matches()
        for item in real_lives:
            # Build full match state and cache
            state = live_service.generate_live_match_state(item)
            LIVE_MATCH_CACHE[item["id"]] = state
            match_list.append({
                "id": state["id"],
                "title": state["title"],
                "venue": state["venue"],
                "date": state["date"],
                "match_type": "Real Live Feed",
                "description": state["description"],
                "total_balls": len(state["balls"]),
                "start_over_text": state["start_over_text"],
                "first_innings": state["first_innings"],
                "team_batting": state["team_batting"],
                "team_bowling": state["team_bowling"],
                "team_batting_short": state["team_batting_short"],
                "team_bowling_short": state["team_bowling_short"],
                "is_live": True
            })
    except Exception as e:
        print("Live match sync error:", e)

    # 2. Historical Thriller Matches (36-ball & 24-ball complete sequences)
    for match_id, data in MATCHES.items():
        match_list.append({
            "id": data["id"],
            "title": data["title"],
            "venue": data["venue"],
            "date": data["date"],
            "match_type": data["match_type"],
            "description": data["description"],
            "total_balls": len(data["balls"]),
            "start_over_text": data["start_over_text"],
            "first_innings": data["first_innings"],
            "team_batting": data["team_batting"],
            "team_bowling": data["team_bowling"],
            "team_batting_short": data["team_batting_short"],
            "team_bowling_short": data["team_bowling_short"],
            "is_live": False
        })
    
    # 3. Dynamic ingested matches
    for match_id, data in ai_engine.dynamic_matches.items():
        match_list.append({
            "id": data["id"],
            "title": f"🔴 {data['title']}",
            "venue": data["venue"],
            "date": data["date"],
            "match_type": "Live Stream",
            "description": data["description"],
            "total_balls": len(data["balls"]),
            "start_over_text": data["start_over_text"],
            "first_innings": data["first_innings"],
            "team_batting": data["team_batting"],
            "team_bowling": data["team_bowling"],
            "team_batting_short": data["team_batting_short"],
            "team_bowling_short": data["team_bowling_short"],
            "is_live": True
        })
    return jsonify({"matches": match_list})

@app.route("/api/match/<match_id>")
def get_match(match_id):
    if match_id in LIVE_MATCH_CACHE:
        match = LIVE_MATCH_CACHE[match_id]
    else:
        match = ai_engine.get_match_data(match_id)
    if not match:
        return jsonify({"error": "Match not found"}), 404
    
    return jsonify({
        "match": match,
        "total_balls": len(match["balls"])
    })

@app.route("/api/match/<match_id>/ball/<int:ball_index>")
def get_ball(match_id, ball_index):
    if match_id in LIVE_MATCH_CACHE:
        match = LIVE_MATCH_CACHE[match_id]
    else:
        match = ai_engine.get_match_data(match_id)
    if not match:
        return jsonify({"error": "Match not found"}), 404
    
    balls = match["balls"]
    if ball_index < 0 or ball_index >= len(balls):
        return jsonify({"error": "Ball index out of bounds"}), 400
    
    ball = balls[ball_index]
    return jsonify({
        "ball": ball,
        "ball_index": ball_index,
        "total_balls": len(balls),
        "is_first": ball_index == 0,
        "is_last": ball_index == len(balls) - 1
    })

@app.route("/api/catchup", methods=["POST"])
def catchup():
    data = request.get_json() or {}
    match_id = data.get("match_id", "ind_vs_sa_t20wc2024")
    if match_id in LIVE_MATCH_CACHE:
        ai_engine.dynamic_matches[match_id] = LIVE_MATCH_CACHE[match_id]
    ball_index = int(data.get("ball_index", 0))
    summary = ai_engine.generate_catchup(match_id, ball_index)
    return jsonify(summary)

@app.route("/api/fantasy-leverage", methods=["POST"])
def fantasy_leverage():
    data = request.get_json() or {}
    match_id = data.get("match_id", "ind_vs_sa_t20wc2024")
    if match_id in LIVE_MATCH_CACHE:
        ai_engine.dynamic_matches[match_id] = LIVE_MATCH_CACHE[match_id]
    ball_index = int(data.get("ball_index", 0))
    leverage = ai_engine.get_fantasy_leverage(match_id, ball_index)
    return jsonify(leverage)

@app.route("/api/ask-dugout", methods=["POST"])
def ask_dugout():
    data = request.get_json() or {}
    match_id = data.get("match_id", "ind_vs_sa_t20wc2024")
    if match_id in LIVE_MATCH_CACHE:
        ai_engine.dynamic_matches[match_id] = LIVE_MATCH_CACHE[match_id]
    ball_index = int(data.get("ball_index", 0))
    query = data.get("query", "").strip()
    client_api_key = data.get("api_key", "").strip() or None

    if not query:
        return jsonify({"answer": "Please ask a question about match tactics, win probabilities, or fantasy captaincy!"})

    response = ai_engine.chat_dugout(match_id, ball_index, query, client_api_key)
    return jsonify(response)

@app.route("/api/live/ingest", methods=["POST"])
def live_ingest():
    """
    Ingest a live ball in real time from any live cricket match feed.
    """
    data = request.get_json() or {}
    result = ai_engine.ingest_live_ball(data)
    return jsonify(result)

@app.route("/api/set-gemini-key", methods=["POST"])
def set_gemini_key():
    data = request.get_json() or {}
    key = data.get("api_key", "").strip()
    ai_engine.set_api_key(key)
    return jsonify({
        "success": True,
        "has_key": bool(key)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"MatchPulse AI server starting on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
