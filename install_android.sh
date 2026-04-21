#!/bin/bash

# Update package index and install necessary packages
sudo apt update && sudo apt install -y python python-pip git curl

# Clone the offline-ai-autopilot repository
git clone https://github.com/greeneyedbeautty/offline-ai-autopilot.git

# Change directory to the cloned repository
cd offline-ai-autopilot

# Install Python dependencies
pip install -r requirements.txt

# Install Ollama (assuming Ollama has a public installation command)
sudo apt install -y ollama

# Instructions for next steps
echo "Installation complete!"
echo "Next steps:" 
echo "1. Navigate to the offline-ai-autopilot directory."
echo "2. Run the application as per its documentation."