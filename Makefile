docker-build:
	docker build -t sample-library .

docker-run-it: docker-build
	docker run -it --rm -v $$PWD:/home/python/app sample-library

it: docker-run-it

main:
	python src/main.py

clean:
	rm -rf lib; mkdir lib; make main

fmt:
	python -m black .
