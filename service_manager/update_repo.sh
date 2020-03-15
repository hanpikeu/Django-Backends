#!/bin/bash
git reset --hard
git fetch
git pull

arguments=( "${@}" )
for argument in "${arguments[@]}"
do
  case "${argument}" in
    "-p")
    bash service_manager/update_pip.sh
    ;;
    "-m")
    bash service_manager/stop_django.sh
    bash service_manager/migrate_django.sh
    bash service_manager/stop_django.sh
    ;;
    "-d")
    bash service_manager/stop_discord_bot.sh
    bash service_manager/start_discord_bot.sh
    ;;
  esac
done