docker-build:
	docker build -t sample-library .

docker-run-it: docker-build
	docker run -it --rm -v $$PWD:/home/python/app sample-library

it: docker-run-it

main: clean
	python src/main.py

clean:
	rm -rf lib; mkdir lib; touch lib/README.md

fmt:
	python -m black .
