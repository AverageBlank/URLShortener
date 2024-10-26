#!/bin/bash

# Create a .env file if it doesn't exist
if [ ! -f ".env" ]; then
    touch .env
fi

# Function to setup URI and key
get_input() {
    local prompt="$1"
    local key="$2"
    
    while true; do
        if grep -q "^$key=" .env; then
            echo "Value for '$key' already exists in the .env file."
            read -p "Would you like to view or edit it? (n to move to next) (v/e/n): " action
            if [[ "$action" == "v" ]]; then
                current_value=$(grep "^$key=" .env | cut -d '=' -f 2-)
                echo "$key is currently set to: $current_value"
            elif [[ "$action" == "e" ]]; then
                read -p "Enter new value for $key (Press Enter to keep current value): " input_value
                if [ -z "$input_value" ]; then
                    echo "Keeping current value: $current_value"
                else
                    sed -i "s|^$key=.*|$key=$input_value|" .env
                fi
            elif [[ "$action" == "n" ]]; then
                break
            else
                echo "Invalid option. Please enter 'v' to view, 'e' to edit, or 'n' to go to the next variable."
            fi
        else
            read -p "$prompt: " input_value
            echo "$key=$input_value" >> .env
            break
        fi
    done
}

get_input "Enter your MongoDB URI" "link"

get_input "Enter your secret key" "SECRET_KEY"

echo "Setup complete. Installing dependencies..."

# Create a virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    python -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Install required libraries
pip install -r requirements.txt

echo "Installation complete. You can now run the application using './start.sh'."
