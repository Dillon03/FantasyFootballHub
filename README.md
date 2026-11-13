## FantasyFootballHub

FantasyFootballHub is a web application designed to help fantasy football players create and manage their own teams. Users can build their rosters, add or remove players, organize their starting lineups, and keep track of their team in one place.

Managing a fantasy football team should be simple and organized. FantasyFootballHub provides an easy-to-use interface where users can make changes to their rosters without having to navigate a complicated fantasy football platform.

The goal of FantasyFootballHub is to provide a straightforward way for users to manage their fantasy football teams while keeping their information secure. Each user will have their own account and will only be able to manage teams that belong to them.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dillon03/FantasyFootballHub.git
   ```

2. Navigate to the project folder:
   ```bash
   cd FantasyFootballHub
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Install the required dependencies:
   ```bash
   venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```bash
   venv\Scripts\python.exe manage.py migrate
   ```

## Getting Started

1. Start the Django development server:
   ```bash
   venv\Scripts\python.exe manage.py runserver
   ```

2. Open a browser and visit:
   http://127.0.0.1:8000/

3. The FantasyFootballHub homepage will appear.