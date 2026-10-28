# ⚡ Cyber-Attack & Defense Simulator - Team C

Welcome to the official Team C repository (Letizia Grassi, Simone Romano, Shayan Khoshrou, Soheil Tavakoli).
This manual explains how to configure your PC for the first time, how to use the Docker virtual environment, how to work daily with Git without overwriting each other's code, and how to use automated tests.

## 💻 Phase 1: The First Time (Clone + Setup)
**⚠️ ATTENTION: You only do this phase ONCE in your life.** This phase is strictly for downloading the repository for the first time and setting up the software. **Do not use this phase for your daily coding work.** For your daily programming routine, jump to Phase 2.

### Step 1.1: Software Prerequisites (Windows or Mac)
Before starting, ensure you have the following installed on your PC:
1. **Git** (On Windows install *Git for Windows*; on Mac it is usually pre-installed).
2. **Visual Studio Code (VS Code)**.
3. **Docker Desktop** (Download from the official Docker website, install it, and **run it** until the whale icon is steady and active).
   * *Tip for Mac (Apple Silicon M1/M2/M3/M4) and Windows:* Open Docker Desktop Settings (⚙️) > **Resources** > set the **Memory (RAM)** to at least **6 GB or 8 GB**, then click *Apply & Restart*.
4. Open VS Code, go to the **Extensions** section (the four squares icon on the left), and install the official **Dev Containers** extension by Microsoft.

### Step 1.2: Download (Clone) the Repository to Your PC
Never download the project as a `.zip` file from the website, otherwise Git will not work. Use the terminal to link a folder on your PC to the GitHub server:
1. Open your terminal (or Git Bash / PowerShell on Windows).
2. Navigate to where you want to save the project (e.g., `cd Documents`).
3. Clone the repository:
   ```bash
   git clone [https://github.com/rimosoma/cyber-grid-sim-team-c.git](https://github.com/rimosoma/cyber-grid-sim-team-c.git)
Enter the project folder:

Bash
cd cyber-grid-sim-team-c
(Note: During this first setup phase, you stay on the main branch. You do NOT create your task branch yet. Branch creation is explained in Phase 2).

### Step 1.3: Enter the Docker Dev Container from VS Code
To avoid the "it works on my machine" problem, we do not use the Python installed on Windows or Mac. Instead, we all work inside the Docker container configured in the hidden .devcontainer folder:

Make sure Docker Desktop is open and running.

Open VS Code, click File > Open Folder..., and select the cyber-grid-sim-team-c folder.

Click the green >< button in the bottom-left corner of VS Code (or press F1 / Cmd+Shift+P / Ctrl+Shift+P) and select "Dev Containers: Reopen in Container".

The first time, VS Code will take about 3-5 minutes to download Linux (Debian Bookworm) and install all the libraries from requirements.txt. Subsequent times it will open in 3 seconds.

How to verify you are inside the container?

In the bottom-left green rectangle, you will read: Dev Container: Cyber-Grid Simulator (Team C).

Open the integrated terminal in VS Code (Terminal > New Terminal) and type pip list: you will see pandapower, helics, scipy, fastapi, and pytest ready to go!

## 🔄 Phase 2: Daily Workflow (The Git Pipeline)
⛔ GOLDEN RULE & GITHUB PROTECTION: The main branch contains only tested, approved, and working code. GitHub is configured to block any direct modifications to main. If you try to push directly to main, the server will block you with an error. You MUST create a separate branch for each task, work locally, and ask for permission to merge only when the task is finished.

##Follow these exact 5 steps every single day you work on the project (the commands are identical on Windows, Mac, and Linux):

### Step 1: Update Your Local Code (Pull)
You never have to git clone again. To check if your teammates have added new features to main while you were away, and download them to your PC:

Bash
 1. Open terminal and enter the local folder
cd cyber-grid-sim-team-c

 2. Move to the main branch
git checkout main

 3. Download the latest approved updates from the server
git pull
Result: Your PC is now synced with the team's latest official version.

### Step 2: Create a NEW Branch for Your Task
IMMEDIATELY after running git pull, and BEFORE writing a single line of code, create a new branch.Why do we do this? Think of main as an original master document locked in a safe. Creating a branch is like placing a transparent sheet of tracing paper over the original: you can draft, experiment, and make mistakes on your tracing paper without ever ruining the original.
You must create a new branch for every single Gantt task (do not reuse old branches):

Bash
Replace with the ID and name of your current task
git checkout -b feat/t1.1-your-task-name
(Examples: git checkout -b feat/t1.1-ieee14-model, git checkout -b feat/t2.1-ns3-topology).

### Step 3: Work Locally and Save Daily Progress (Add + Commit)
Now you are in your safe, isolated space. Open the Dev Container (if you haven't already) and start coding.

You do not need to upload (push) to GitHub every day. Instead, save your progress locally on your PC by taking "snapshots" (commit) whenever you finish working for the day or complete a small piece.

To save your progress, you MUST run BOTH commands in sequence:

Bash
 1. Prepare all modified files (put them in the staging cart)
git add .

 2. Take the snapshot to permanently save them (checkout the cart)
git commit -m "Drafted the first part of the task"
You can repeat Step 3 (Write code -> git add . -> git commit) every day for weeks while working locally. Just remember that add alone doesn't save your progress without the commit!

### Step 4: Run Tests and Upload Your FINISHED Task to GitHub (Push)
ONLY when the entire task is 100% complete, verify first that all automated tests pass (see Phase 3 below) by running this in the container terminal:

Bash
pytest
If everything is green (PASSED), send your branch to the GitHub server:

Bash
git push -u origin YOUR_BRANCH_NAME

### Step 5: The Pull Request (Merging to main)
Your finished code is online, but it is still in your isolated branch. To merge it into main:

Go to the repository page on GitHub.

Click the green/yellow Compare & pull request button.

Write a brief explanation of what you did and click Create pull request.

Automated Check + Approval:

GitHub will automatically start the Tests (CI). Wait 30 seconds for the green checkmark ✅ to appear.

Due to branch protection rules, the Merge button will be disabled until a teammate reviews the work. Message the WhatsApp group and ask a teammate to go to GitHub, review your Pull Request, and approve it.

Once you receive 1 approval (and tests are green), click Merge pull request. Your work is officially part of main!

How to Close Your Work at the End of the Day
On VS Code: Click the green rectangle in the bottom-left and choose Close Remote Connection (or simply close the VS Code window).

On Docker Desktop: If you want to free up your PC's RAM when you are done studying, open Docker Desktop, go to Containers, and press the Stop (⏹️) button next to the project container.

## 🧪 Phase 3: Automated Tests (Pytest & GitHub Actions)
The tests/ folder contains automated tests that protect the project from syntax errors, broken libraries, or JSON messages that violate the ICD (shared/schemas.py).

How to Run Tests on Your PC (Before Pushing)
Open the terminal inside the VS Code Dev Container and type:

Bash
pytest -v
What happens: Pytest will execute all tests/test_*.py files.

If you see green PASSED text, your code is healthy and you can git push.

If you see red FAILED text, read the error message in the terminal, fix your code, and re-run pytest -v until everything turns green.

How to Add New Tests for Your Work Package
As you develop your modules (wp1...wp7), add your unit tests in the tests/ folder:

tests/test_environment.py ➔ Checks folder structure, syntax of all .py files, baseline pandapower IEEE 14-bus, and HELICS installation.

tests/test_icd_schemas.py ➔ Checks that JSON payloads comply with the ICD (shared/schemas.py).

You can create new files (e.g., tests/test_wp1_grid.py or tests/test_wp4_defense.py): just ensure the filename and the test functions inside start with test_, and both pytest and GitHub will run them automatically!

## 📁 Phase 4: Folder Structure (Who Does What)
Everyone must work exclusively inside their assigned Work Package folders to avoid conflicts:

.devcontainer/ ➔ Linux Docker environment setup for VS Code

.github/workflows/ ➔ GitHub Automated Tests (CI) setup

config/ ➔ Global HELICS config and JSON attack schedule

docs/ ➔ Official docs: SysReq, ICD.md, meeting logs

shared/ ➔ Shared data schemas (schemas.py) and constants (constants.py)

tests/ ➔ Automated tests run with pytest and GitHub Actions

wp1_power_grid/ ➔ pandapower physics simulation (IEEE 14-bus) and actuators (Shayan)

wp2_scada_network/ ➔ NS-3 topology, SCADA protocol, and latency (Simone)

wp3_attack_generator/ ➔ Scheduler and DDoS/FDI attack injection (Simone)

wp4_defense_module/ ➔ WLS State Estimator and Chi-Squared Bad Data Detection (Letizia)

wp5_control_center/ ➔ Manual Control and Auto-OPF (Shayan)

wp6_orchestrator_db/ ➔ HELICS Sync and SQLite Database (Letizia & Soheil)

wp7_dashboard/ ➔ React Web UI and FastAPI Backend (Soheil)

## 🆘 Phase 5: Troubleshooting (Cheat Sheet)
I messed up my code and want to undo all UNSAVED (uncommitted) changes:

Bash
git restore .
I forgot which branch I am on or what files I modified:

Bash
git status
I tried to git pull but I got an error and it blocked me:
This means you have local changes that are not yet committed. Save them first (git add . and git commit -m "saving state") or undo them (git restore .), then try git pull again.

I added a new Python library to requirements.txt, how do I update the Dev Container?
Press F1 (or Cmd+Shift+P / Ctrl+Shift+P) in VS Code and click on Dev Containers: Rebuild Container.
