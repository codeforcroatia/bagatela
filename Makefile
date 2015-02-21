RUN_ARGS = -it --rm=true --volume "$$(pwd):/app"

.PHONY: development

development:
	@sudo docker run $(RUN_ARGS) google/python bin/bash
