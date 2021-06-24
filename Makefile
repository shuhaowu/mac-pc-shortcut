.PHONY: clean

rules.json: rules/*.json common/*.json compile-rules.py
	python3 compile-rules.py >$@

clean:
	rm -f rules.json
