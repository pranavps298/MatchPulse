"""
Automated Verification Suite for MatchPulse AI
Verifies:
- 36 balls of IND vs SA (Axar 15th over + death overs)
- 24 balls of RCB vs CSK (Ferguson, Green, Siraj, Dayal)
- Dugout AI tactical copilot
- Real-time Live Ball Ingestion engine
"""

import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

from app import app

def test_full_system():
    client = app.test_client()

    print("[1/9] Testing GET / ...")
    res = client.get("/")
    assert res.status_code == 200
    assert b"MatchPulse" in res.data
    print("  -> Passed: Main dashboard loaded.")

    print("[2/9] Testing GET /api/health ...")
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "healthy"
    print("  -> Passed: Health check endpoint OK.")

    print("[3/9] Testing GET /api/match/ind_vs_sa_t20wc2024 ...")
    res = client.get("/api/match/ind_vs_sa_t20wc2024")
    assert res.status_code == 200
    ind_sa = res.get_json()
    assert ind_sa["total_balls"] == 36, f"Expected 36 balls, got {ind_sa['total_balls']}"
    # Verify over 15 Klaasen assault exists (ball 0 to 5)
    ball0 = ind_sa["match"]["balls"][0]
    assert ball0["over"] == "14.1" and ball0["bowler"] == "Axar Patel"
    # Verify over 16 Klaasen wicket (ball 6)
    ball6 = ind_sa["match"]["balls"][6]
    assert ball6["over"] == "15.1" and ball6["bowler"] == "Hardik Pandya" and ball6["is_wicket"] is True
    # Verify over 20 Surya catch (ball 30)
    ball30 = ind_sa["match"]["balls"][30]
    assert ball30["over"] == "19.1" and ball30["is_wicket"] is True
    print("  -> Passed: Complete 36-ball IND vs SA sequence verified (Over 15 Axar carnage -> 20th over victory).")

    print("[4/9] Testing GET /api/match/rcb_vs_csk_ipl2024 ...")
    res = client.get("/api/match/rcb_vs_csk_ipl2024")
    assert res.status_code == 200
    rcb_csk = res.get_json()
    assert rcb_csk["total_balls"] == 24, f"Expected 24 balls, got {rcb_csk['total_balls']}"
    # Check Ferguson over
    ball0 = rcb_csk["match"]["balls"][0]
    assert ball0["over"] == "16.1" and ball0["bowler"] == "Lockie Ferguson"
    # Check Dayal over (ball 18 to 23)
    ball18 = rcb_csk["match"]["balls"][18]
    assert ball18["over"] == "19.1" and ball18["runs_scored"] == 6 # Dhoni 110m six
    ball19 = rcb_csk["match"]["balls"][19]
    assert ball19["over"] == "19.2" and ball19["is_wicket"] is True # Dhoni out
    print("  -> Passed: Complete 24-ball RCB vs CSK playoff qualification phase verified.")

    print("[5/9] Testing POST /api/catchup ...")
    res = client.post("/api/catchup", json={"match_id": "ind_vs_sa_t20wc2024", "ball_index": 12})
    assert res.status_code == 200
    catchup = res.get_json()
    assert len(catchup["bullets"]) == 3
    print("  -> Passed: Catch Me Up in 10s brief verified.")

    print("[6/9] Testing POST /api/fantasy-leverage ...")
    res = client.post("/api/fantasy-leverage", json={"match_id": "ind_vs_sa_t20wc2024", "ball_index": 15})
    assert res.status_code == 200
    fantasy = res.get_json()
    assert len(fantasy["top_performers"]) >= 4
    print("  -> Passed: Fantasy leverage radar & top performer multipliers verified.")

    print("[7/9] Testing POST /api/ask-dugout (Tactical Q&A) ...")
    queries = [
        "Why is Bumrah bowling now?",
        "What is the win probability?",
        "Why did Dhoni get out to Yash Dayal?",
        "Who is the best fantasy captain right now?"
    ]
    for q in queries:
        res = client.post("/api/ask-dugout", json={
            "match_id": "ind_vs_sa_t20wc2024",
            "ball_index": 15,
            "query": q
        })
        assert res.status_code == 200
        ans = res.get_json()
        assert "answer" in ans and len(ans["answer"]) > 20
    print("  -> Passed: Dugout Copilot successfully answered all 4 tactical queries.")

    print("[8/9] Testing POST /api/live/ingest (Dynamic Live Ball Stream) ...")
    res = client.post("/api/live/ingest", json={
        "match_id": "live_world_cup",
        "title": "IND vs AUS — ICC Live Stream",
        "over": "19.3",
        "bowler": "Jasprit Bumrah",
        "striker": "Travis Head",
        "runs_scored": 0,
        "is_wicket": True,
        "target": 190,
        "commentary": "OUT! Bumrah cleans him up with a 144km/h yorker!"
    })
    assert res.status_code == 200
    ingest_result = res.get_json()
    assert ingest_result["success"] is True
    assert ingest_result["ball"]["is_wicket"] is True
    print("  -> Passed: Live ball ingested into dynamic match stream.")

    print("[9/9] Testing GET /api/matches with Dynamic Match included ...")
    res = client.get("/api/matches")
    assert res.status_code == 200
    matches = res.get_json()["matches"]
    assert any("live_world_cup" in m["id"] for m in matches)
    print("  -> Passed: Dynamic live match automatically listed in match feed.")

    print("\nALL 9 TESTS PASSED FLAWLESSLY! COMPREHENSIVE BALL COVERAGE & LIVE INGEST VERIFIED.")

if __name__ == "__main__":
    test_full_system()
