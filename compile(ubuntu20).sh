#!/bin/bash

cp -r compilation\(ubuntu20\)/* .
sudo docker compose up
sudo cp /var/lib/docker/volumes/tictactoe_dist20/_data/TicTacToe\(ubuntu20\) .
rm Pipfile Pipfile.lock TicTacToe.spec Dockerfile docker-compose.yml
