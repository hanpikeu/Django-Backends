#!/bin/bash
git reset --hard
git fetch
git pull

arguments=( "${@}" )
for argument in "${arguments[@]}"
do
  case "${argument}" in
    "-m")
    echo `pwd`
    bash stop_django.sh
    bash migrate_django.sh
    bash stop_django.sh
    ;;
    "-d")
    echo `pwd`
    bash stop_discord_bot.sh
    bash start_discord_bot.sh
    ;;
  esac
done