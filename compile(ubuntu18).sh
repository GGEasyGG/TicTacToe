#!/bin/bash

cp -r compilation\(ubuntu18\)/* .
sudo docker compose up
sudo cp /var/lib/docker/volumes/tictactoe_dist18/_data/TicTacToe\(ubuntu18\) .
rm Pipfile Pipfile.lock TicTacToe.spec Dockerfile docker-compose.yml