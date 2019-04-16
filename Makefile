.PHONY: build
build:
	python setup.py bdist_wheel --module signalfx_gcf
	python setup.py bdist_wheel --module signalfx_lambda

.PHONY: clean
clean:
	rm -rf dist
	rm -rf build
	rm -rf signalfx_serverless_*.egg-info
