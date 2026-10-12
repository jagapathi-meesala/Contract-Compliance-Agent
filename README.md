# Contract Compliance Agent

An OpenGAP-compatible, framework-independent agent for organizing contract obligations and compliance evidence from caller-provided information.

## Capabilities
- Extract and organize supplied obligations and deadlines
- Map obligations to evidence provided by the caller
- Identify obligations with missing or incomplete evidence
- Prepare a follow-up action plan
- Keep assumptions, ambiguities, and review needs visible

## Run locally

```bash
pytest -q
python3 verification/readiness_audit.py
opengap validate
```

No external legal database or contract repository is accessed. This agent supports document review and tracking; it does not replace qualified legal advice.
