#!/bin/bash
# Add gemini CLI to PATH
export PATH="/Users/yaser-wyx/.nvm/versions/node/v24.13.1/bin:$PATH"

# Navigate to project directory
cd /Users/yaser-wyx/PycharmProjects/daily_robot_paper

# Run the python script using the virtual environment
# Log output to daily_run.log for debugging
/Users/yaser-wyx/PycharmProjects/daily_robot_paper/.venv/bin/python daily.py >> daily_run.log 2>&1
