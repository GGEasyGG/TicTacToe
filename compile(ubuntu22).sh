#!/bin/bash

cp -r compilation\(ubuntu22\)/* .
sudo docker compose up
sudo cp /var/lib/docker/volumes/tictactoe_dist22/_data/TicTacToe\(ubuntu22\) .
rm Pipfile Pipfile.lock TicTacToe.spec Dockerfile docker-compose.yml
