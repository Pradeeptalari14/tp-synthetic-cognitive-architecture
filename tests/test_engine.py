import pytest
import numpy as np
from cognitive_engine import SensoryPercept, GlobalWorkspaceBlackboard, ActiveInferenceAgent

def test_sensory_percept_init():
    p = SensoryPercept("test_sensor", np.ones(256), entropy=0.25)
    assert p.sensor_id == "test_sensor"
    assert p.entropy == 0.25
    assert len(p.vector) == 256

def test_winner_take_all_competition():
    bb = GlobalWorkspaceBlackboard()
    p1 = SensoryPercept("s1", np.ones(256) * 0.1, entropy=0.1)
    p2 = SensoryPercept("s2", np.ones(256) * 1.5, entropy=0.8)
    winner = bb.compete_for_workspace([p1, p2])
    assert winner.sensor_id == "s2"
    assert bb.active_broadcast == p2

def test_dual_process_routing():
    bb = GlobalWorkspaceBlackboard(deliberation_threshold=0.65)
    p_low_entropy = SensoryPercept("reflex", np.ones(256), entropy=0.1)
    mode, conf = bb.route_cognitive_mode(p_low_entropy)
    assert mode == "System1_Neural_Reflex"
    assert conf > 0.65

    p_high_entropy = SensoryPercept("deliberate", np.ones(256), entropy=0.9)
    mode, conf = bb.route_cognitive_mode(p_high_entropy)
    assert mode == "System2_Deliberative_Search"
    assert conf < 0.65

def test_active_inference_step():
    agent = ActiveInferenceAgent(prior_belief=0.5)
    percepts = [
        SensoryPercept("sensor_alpha", np.random.randn(256), entropy=0.3),
        SensoryPercept("sensor_beta", np.random.randn(256), entropy=0.7)
    ]
    res = agent.step(percepts)
    assert "winner_sensor" in res
    assert res["free_energy"] >= 0.0
    assert 0.0 <= res["confidence"] <= 1.0
