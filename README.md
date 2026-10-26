# ⚡ Cyber-Attack & Defense Simulator - Team C

Welcome to the Team C repository (Letizia, Simone, Shayan, Soheil). This is our official project workspace.

---

## 🛠️ Phase 0: Grant Access *(For Simone)*

1. Go to the repository page on GitHub.
2. Click **Settings** > **Collaborators** > **Add people**.
3. Add the GitHub usernames for Letizia, Shayan, and Soheil.

---

## 📥 Phase 1: Download (Clone) the Code

*(Everyone does this ONCE on their PC)*

1. Open your terminal (or Git Bash/VS Code terminal).
2. Navigate to your target folder and run:
```bash
git clone https://github.com/rimosoma/cyber-grid-sim-team-c.git
cd cyber-grid-sim-team-c

```



---

## 🚦 Phase 2: Team Workflow

**🚨 GOLDEN RULE: NEVER commit directly to the `main` branch. The `main` branch is only for fully working, approved code.**

Follow these exact steps every time you start a new task:

### 1. Update your local code

Always get the latest approved code before starting:

```bash
git checkout main
git pull

```

### 2. Create your isolated workspace (Branch)

Create a new branch for your specific task:

```bash
git checkout -b feat/t1.1-task-name

```

### 3. Work, Save, and Commit

Write your code, save your files, and then "snapshot" your progress:

```bash
git add .
git commit -m "Added IEEE 14-bus model"

```

### 4. Upload to GitHub (Push)

Send your branch to the online server:

```bash
git push -u origin feat/t1.1-task-name

```

### 5. Create a Pull Request (PR)

1. Go to the repository on GitHub.
2. Click the green **Compare & pull request** button.
3. Write a brief description and click **Create pull request**.
4. Ask a teammate to review your code. Once approved, they will click **Merge pull request** to combine it with the `main` branch.

---

## 📁 Phase 3: Folder Structure (Who does what)

Work **only** in your assigned folders to avoid code conflicts.

* `docs/` ➔ Official documents (SysReq, ICD)
* `wp1_power_grid/` ➔ physical grid simulator (**Shayan**)
* `wp2_scada_network/` ➔ NS-3/OMNeT++ and SCADA gateway (**Simone**)
* `wp3_attack_generator/` ➔ DDoS and FDI injection (**Simone**)
* `wp4_defense_module/` ➔ WLS Estimator and Chi-Squared test (**Letizia**)
* `wp5_control_center/` ➔ Auto OPF and manual control (**Shayan**)
* `wp6_orchestrator_db/` ➔ HELICS engine and SQLite (**Letizia & Soheil**)
* `wp7_dashboard/` ➔ React Frontend and FastAPI Backend (**Soheil**)

---

## 🆘 Quick Cheat Sheet

**How do I undo all unsaved changes?**

```bash
git restore .

```

**Where am I? (Check current branch and uncommitted files)**

```bash
git status

```
