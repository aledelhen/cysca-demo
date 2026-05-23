.PHONY: test install-skill activate

test:
	gauge run specs

install-skill:
	./scripts/install-codex-skill.sh

activate:
	@echo "Run: source .venv/bin/activate"
