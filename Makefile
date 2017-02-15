
NAME = bufferapp/looker-data-actions:beta

.PHONY: all build run dev

all: run

build:
	docker build -t $(NAME) .

run:
	docker run -it --rm -p 5000:5000 $(NAME)


push:
	docker push $(NAME)


dev:
	docker run -v $(PWD)/server:/app -it --rm -p 5000:5000 $(NAME)
