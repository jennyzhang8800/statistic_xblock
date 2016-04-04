#!/bin/bash

local_time=$(date '+%Y-%m-%d_%H:%M:%S')
tt=Update:
commit_message=${tt}${local_time}
cd /var/www/zyni/statistic_xblock/
git pull -u origin master
git add .
git commit -m ${commit_message}
git push -u origin master

