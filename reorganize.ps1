# Move core application files
Move-Item -Path "app.py" -Destination "src/core/" -ErrorAction SilentlyContinue
Move-Item -Path "main.py" -Destination "src/core/" -ErrorAction SilentlyContinue

# Move utility files
Move-Item -Path "utils/*" -Destination "src/services/" -ErrorAction SilentlyContinue

# Move test files
Move-Item -Path "test_*.py" -Destination "tests/" -ErrorAction SilentlyContinue
Move-Item -Path "basic_test.py" -Destination "tests/" -ErrorAction SilentlyContinue

# Move analysis files
Move-Item -Path "auto_investor.py" -Destination "src/analysis/" -ErrorAction SilentlyContinue
Move-Item -Path "stock_dashboard.py" -Destination "src/analysis/" -ErrorAction SilentlyContinue

# Create cache directory in data
New-Item -ItemType Directory -Force -Path "data/cache"
Move-Item -Path "cache/*" -Destination "data/cache/" -ErrorAction SilentlyContinue

# Move configuration to config directory
Move-Item -Path "*.bat" -Destination "config/" -ErrorAction SilentlyContinue
