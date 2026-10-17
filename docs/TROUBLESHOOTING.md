# Incident Triage & Troubleshooting Runbook — Synthetic Cognitive Architecture Studio

> **Severity Tier:** P1 - P3 SRE Operational Runbook  
> **Maintainer:** Talari Pradeep (Platform Architecture)

---

## Common Incident Signatures

### Incident 1: `Variational Free Energy Divergence (F > 10.0)`
- **Symptom & Alert:** Pipeline telemetry breaches critical threshold or logs failure signature.
- **Root Cause Analysis:** Rapidly fluctuating sensory entropy with extreme measurement noise.
- **Standard Operating Remediation:**
  ```bash
  # Step 1: Diagnose current state
  python main.py --diagnose

  # Step 2: Remediate configuration
  Dampen learning rate to 0.05 and recalibrate prior belief baseline in active inference loop.
  ```


### Incident 2: `System 2 Deliberation Starvation`
- **Symptom & Alert:** Pipeline telemetry breaches critical threshold or logs failure signature.
- **Root Cause Analysis:** Deliberation threshold set excessively high (>0.85), forcing noisy inputs into reflex mode.
- **Standard Operating Remediation:**
  ```bash
  # Step 1: Diagnose current state
  python main.py --diagnose

  # Step 2: Remediate configuration
  Adjust deliberation threshold to 0.65 via CLI or config file.
  ```


---

## Emergency Escalation Protocol
1. **L1 Triage:** Verify pod status via `kubectl get pods -l app=synthetic-cognitive-architecture`.
2. **L2 Deep Dive:** Check container logs via `kubectl logs -l app=synthetic-cognitive-architecture --tail=100`.
3. **L3 Incident Lead:** Contact `pradeeptalari14@gmail.com` for critical containment breaches.
