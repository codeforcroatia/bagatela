IMAGE = codeacross-bagatela
RUN_ARGS = -it --rm=true --volume "$$(pwd):/app"

.PHONY: shell crawl build

shell:
	@sudo docker run $(RUN_ARGS) $(IMAGE) /bin/bash

crawl:
	@sudo docker run $(RUN_ARGS) $(IMAGE) /usr/local/bin/scrapy crawl procurement

build:
	@sudo docker build --tag=$(IMAGE) .
