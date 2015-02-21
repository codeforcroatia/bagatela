IMAGE = codeacross-bagatela
RUN_ARGS = -it --rm=true --volume "$$(pwd):/app"

.PHONY: development build

development:
	@sudo docker run $(RUN_ARGS) $(IMAGE) /bin/bash

build:
	@sudo docker build --tag=$(IMAGE) .
