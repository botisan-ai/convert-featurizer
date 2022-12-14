-include .env.local
export

executor:
	pipenv run jina executor --uses config.yml --port $$EXECUTOR_PORT

flow:
	pipenv run jina flow --uses featurizer.yml

publish:
	pipenv run jina hub push --public .
