build:
	set -e
	sudo docker build -t carlosvalarezo/pokeberries .

run: build
	set -e
	sudo docker run -itp 5000:5000 --rm --name pokeberries \
	-e FLASK_DEBUG=True \
	-e APP_PORT=5000 \
	-e PYTHONPATH=/api \
	-e POKEMON_URI=https://pokeapi.co/api/v2/berry \
	-e BERRY_LIMIT=20 \
	-e BERRY_OFFSET=0 \
	-v ${PWD}/api:/api carlosvalarezo/pokeberries

test:
	set -e
	sudo docker build --target dev -t carlosvalarezo/pokeberries .
	sudo docker run -itp 5000:5000 --rm --name pokeberries \
	-v ${PWD}/api:/api carlosvalarezo/pokeberries python -m pytest
