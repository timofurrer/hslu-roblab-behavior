.PHONY: doc

doc:
	PYTHONPATH=$$PYTHONPATH:. python schoolboy/core.py doc/fsm.png
