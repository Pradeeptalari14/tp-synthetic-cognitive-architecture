#!/usr/bin/env python3
"""
Synthetic Cognitive Architecture Engine
Global Workspace Theory (GWT) Blackboard & Karl Friston Active Inference Loop.
"""
from typing import Dict, List, Tuple, Any, Optional
import numpy as np
import time

class SensoryPercept:
    def __init__(self, sensor_id: str, vector: np.ndarray, entropy: float):
        self.sensor_id = sensor_id
        self.vector = vector
        self.entropy = entropy
        self.timestamp = time.time()

class GlobalWorkspaceBlackboard:
    def __init__(self, dimension: int = 256, deliberation_threshold: float = 0.65):
        self.dimension = dimension
        self.deliberation_threshold = deliberation_threshold
        self.active_broadcast: Optional[SensoryPercept] = None
        self.episodic_history: List[Dict[str, Any]] = []

    def compete_for_workspace(self, percepts: List[SensoryPercept]) -> SensoryPercept:
        """Winner-take-all attention competition based on salience & surprise."""
        if not percepts:
            raise ValueError("No sensory percepts provided.")
        bids = [np.linalg.norm(p.vector) * (1.0 + p.entropy) for p in percepts]
        winner_idx = int(np.argmax(bids))
        self.active_broadcast = percepts[winner_idx]
        return self.active_broadcast

    def route_cognitive_mode(self, percept: SensoryPercept) -> Tuple[str, float]:
        """Dual-Process System 1 (Reflex) vs System 2 (Deliberative) router."""
        confidence = 1.0 / (1.0 + percept.entropy)
        if confidence >= self.deliberation_threshold:
            return "System1_Neural_Reflex", confidence
        return "System2_Deliberative_Search", confidence

class ActiveInferenceAgent:
    def __init__(self, prior_belief: float = 0.5):
        self.prior_belief = prior_belief
        self.blackboard = GlobalWorkspaceBlackboard()

    def compute_variational_free_energy(self, sensory_obs: float) -> float:
        """F = KL(Q(s) || P(s)) - E_Q[log P(o|s)]"""
        prediction_error = sensory_obs - self.prior_belief
        free_energy = 0.5 * (prediction_error ** 2)
        return float(round(free_energy, 4))

    def step(self, observations: List[SensoryPercept]) -> Dict[str, Any]:
        winner = self.blackboard.compete_for_workspace(observations)
        mode, confidence = self.blackboard.route_cognitive_mode(winner)
        fe = self.compute_variational_free_energy(float(winner.entropy))
        
        learning_rate = 0.15
        self.prior_belief += learning_rate * (winner.entropy - self.prior_belief)
        
        return {
            "winner_sensor": winner.sensor_id,
            "mode": mode,
            "confidence": round(confidence, 3),
            "free_energy": fe,
            "updated_prior": round(self.prior_belief, 3)
        }

if __name__ == "__main__":
    print("🧠 Initializing Synthetic Cognitive Architecture Studio Engine...")
    agent = ActiveInferenceAgent()
    percepts = [
        SensoryPercept("Sensor_Ingress", np.random.randn(256), entropy=0.12),
        SensoryPercept("Sensor_Database_Latency", np.random.randn(256), entropy=0.45),
        SensoryPercept("Sensor_Security_Anomaly", np.random.randn(256), entropy=0.88)
    ]
    result = agent.step(percepts)
    print("✅ Cognitive cycle complete:")
    for k, v in result.items():
        print(f"  • {k}: {v}")
