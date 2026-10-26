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


4. Enter the project folder:
```bash
cd cyber-grid-sim-team-c





---

## 🔄 Phase 2: Daily Workflow (The Pipeline)

⛔ **GOLDEN RULE & GITHUB PROTECTION:** The `main` branch contains only perfect, tested code. **GitHub is set up to block any direct modifications to `main`.** If you try to push directly to it, you will get an error. You MUST create a separate branch, work there, and ask for permission to merge.

Follow these 5 steps **every single time** you sit down to work:

### Step 1: Update your local code (Pull)

You don't need to "clone" again. To get the latest updates your teammates made while you were away:

```bash
# Go back to the main branch
git checkout main

# Download the latest updates from the server
git pull

```

*Result:* Your PC is now up-to-date with the official team code.

### Step 2: Create your isolated workspace (Branch)

Since GitHub protects `main`, create your own branch for the specific task you are doing:

```bash
git checkout -b feat/t1.1-your-task-name

```

*(Example: `git checkout -b docs/icd-letizia`).* You are now in your safe space.

### Step 3: Work, Save, and Commit

Write your code and save your files in VS Code. When a small part is working, "snapshot" it:

```bash
# Prepare all modified files
git add .

# Take the snapshot and name it
git commit -m "Completed IEEE 14-bus model"

```

### Step 4: Upload your branch to GitHub (Push)

Send your isolated branch to the online server:

```bash
git push -u origin YOUR_BRANCH_NAME

```

### Step 5: The Pull Request (Merging)

Your code is online, but it's isolated. Now you must ask GitHub to merge it into `main`.

1. Go to the repository page on GitHub.
2. You will see a yellow banner. Click **Compare & pull request**.
3. Briefly explain what you did and click **Create pull request**.
4. **The GitHub Block:** Because of the protection rules, the green Merge button will be disabled. **You must text the WhatsApp group and ask a teammate to go to GitHub, review your code, and approve it.**
5. Once you get 1 approval, the code is officially merged into `main`.

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
