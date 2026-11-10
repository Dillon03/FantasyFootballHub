# FantasyFootballHub

## User Stories

### 1. User Registration
As a **user**, I want to **create an account**, so I can **save and manage my fantasy football team**.

**Acceptance Criteria:**
- Users can register with a username and password.
- Users can log in and log out.
- Duplicate usernames are not allowed.

### 2. Create a Team
As a **user**, I want to **create a fantasy football team**, so I can **organize my players**.

**Acceptance Criteria:**
- Users can create and name a team.
- Teams are saved to the database.
- Users can view their team.

### 3. Add Players
As a **user**, I want to **add players to my roster**, so I can **build my fantasy football team**.

**Acceptance Criteria:**
- Users can enter a player's name, NFL team, and position.
- Added players appear on the roster.
- Required fields cannot be left empty.

### 4. Manage Roster
As a **user**, I want to **edit or remove players**, so I can **keep my roster updated**.

**Acceptance Criteria:**
- Users can edit player information.
- Users can remove players.
- Changes are saved to the database.

### 5. Set Starting Lineup
As a **user**, I want to **choose starters and bench players**, so I can **organize my lineup**.

**Acceptance Criteria:**
- Users can assign players as starters or bench players.
- Lineup changes are saved.
- Players cannot occupy multiple starting positions.

### 6. View Dashboard
As a **user**, I want to **view my team dashboard**, so I can **quickly see my roster**.

**Acceptance Criteria:**
- The dashboard displays the team name.
- The dashboard displays roster players.
- Users can access roster management from the dashboard.

## Misuser Stories

### 1. Unauthorized Access
As an **attacker**, I want to **access another user's team**, so I can **view their private information**.

**Mitigation Criteria:**
- Users must log in to access their teams.
- Users can only access teams they own.

### 2. Unauthorized Changes
As an **attacker**, I want to **change another user's roster**, so I can **disrupt their team**.

**Mitigation Criteria:**
- Team ownership is checked before changes.
- Unauthorized changes are rejected.

### 3. SQL Injection
As an **attacker**, I want to **submit malicious input**, so I can **manipulate the database**.

**Mitigation Criteria:**
- Database operations use Django's ORM.
- Input is validated before saving.

### 4. Password Guessing
As an **attacker**, I want to **guess another user's password**, so I can **access their account**.

**Mitigation Criteria:**
- Passwords are securely hashed.
- Login attempts are rate-limited.

### 5. Malicious Input
As an **attacker**, I want to **insert harmful content into team or player names**, so I can **affect how the application works**.

**Mitigation Criteria:**
- Input fields have length limits.
- User input is escaped when displayed.