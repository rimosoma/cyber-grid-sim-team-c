```markdown
# ⚡ Cyber-Attack & Defense Simulator - Team C

Welcome to the official Team C repository (Letizia, Simone, Shayan, Soheil).  
This manual explains our team workflow so we don't overwrite or break each other's code.

---

## 🛠️ Phase 0: Grant Access (Simone only)

1. Go to the repository page on GitHub.
2. Click **Settings** > **Collaborators** > **Add people**.
3. Add the GitHub usernames for Letizia, Shayan, and Soheil.

---

## 📥 Phase 1: The First Time (Clone)

**You only do this ONCE.** This links a folder on your PC to the GitHub server.

1. Open your terminal.
2. Navigate to where you want to save the project (e.g., `cd Documents`).
3. Clone the repository:
   ```bash
   git clone [https://github.com/rimosoma/cyber-grid-sim-team-c.git](https://github.com/rimosoma/cyber-grid-sim-team-c.git)

```

4. Enter the project folder:
```bash
cd cyber-grid-sim-team-c

```



---

## 🔄 Phase 2: Daily Workflow (The Pipeline)

⛔ **GOLDEN RULE & GITHUB PROTECTION:** The `main` branch contains only perfect, tested code. **GitHub blocks any direct modifications to `main`.** You MUST create a separate branch for each task, work there locally, and ask for permission to merge only when the task is fully finished.

Follow this exact sequence every time you start a new task on the Gantt chart.

*(Note: These commands are exactly the same on Windows, Mac, and Linux)*

### Step 1: Update your local code (Pull)

Always start by getting the latest approved team code from the server:

```bash
git checkout main
git pull

```

### Step 2: Create a NEW Branch for the specific task

**IMMEDIATELY after pulling, and BEFORE writing a single line of code**, create a new branch. A branch is like a temporary workspace. You must create a *new* branch for every single task on the Gantt chart (e.g., one for T-1.1, a new one for T-1.2, etc.).

```bash
# Replace with your actual task name
git checkout -b feat/t1.1-your-task-name

```

### Step 3: Work locally for days/weeks (Commit)

Now you are in your safe space. You will likely work on this task for several days or weeks. **You don't need to upload (push) to GitHub every day.** Instead, save your progress locally on your PC by taking "snapshots" (commits) whenever a small part of your code is working:

```bash
# Add all changed files
git add .

# Take a snapshot and describe what you did
git commit -m "Drafted the first part of the task"

```

*You can repeat Step 3 (Code -> Add -> Commit) as many times as you want while working on the task locally.*

### Step 4: Upload your FINISHED task to GitHub (Push)

**ONLY when the entire task is 100% complete**, send your isolated branch to the GitHub server so the rest of the team can see it:

```bash
git push -u origin YOUR_BRANCH_NAME

```

### Step 5: The Pull Request (Merging)

Your finished code is now online. To merge it into `main`:

1. Go to the repository page on GitHub.
2. Click the yellow **Compare & pull request** button.
3. Click **Create pull request**.
4. Ask a teammate on WhatsApp to review and approve it. Once approved, it officially becomes part of `main`.

---

## 📁 Phase 3: Folder Structure (Who does what)

Work **strictly** inside your assigned Work Package folders.

* `docs/` ➔ Requirements, ICD, Manuals
* `wp1_power_grid/` ➔ pandapower physics simulation (**Shayan**)
* `wp2_scada_network/` ➔ NS-3 topology & SCADA gateway (**Simone**)
* `wp3_attack_generator/` ➔ DDoS and FDI logic (**Simone**)
* `wp4_defense_module/` ➔ WLS Estimator and Chi-Squared test (**Letizia**)
* `wp5_control_center/` ➔ Manual Control and OPF (**Shayan**)
* `wp6_orchestrator_db/` ➔ HELICS sync and SQLite Database (**Letizia & Soheil**)
* `wp7_dashboard/` ➔ React UI and FastAPI Backend (**Soheil**)

---

## 🆘 Troubleshooting (Cheat Sheet)

**I messed up my code and want to undo all UNSAVED (uncommitted) changes:**

```bash
git restore .

```

**I forgot which branch I am on or what files I modified:**

```bash
git status

```

**I tried to `git pull` but I got a weird error and it blocked me:**

This means you have uncommitted changes on your PC. Save them first (`git add .` + `git commit -m "saving before pull"`) and then try `git pull` again.

```

```
