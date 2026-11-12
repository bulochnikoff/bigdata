from pathlib import Path
text = (Path(__file__).parent / "лаб6_deployment.yaml").read_text(encoding="utf-8")
assert "replicas: 8" in text
assert "replicas: 2" in text
assert "checkpoint" in text
print("manifest ok")
