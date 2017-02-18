IMAGE_NAME := bufferapp/looker-data-actions:beta

.DEFAULT_GOAL := run

.PHONY: build run push dev

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -it --rm -p 5000:5000 $(IMAGE_NAME)

push: build
	docker push $(IMAGE_NAME)

dev:
	docker run -v $(PWD)/server:/app -it --rm -p 5000:5000 $(IMAGE_NAME)
