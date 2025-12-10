# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a **teaching repository** for 4Geeks Academy Spain Full Stack Part-Time cohort 129. It contains daily lessons, exercises, and learning materials organized by day (e.g., `day_01/`, `day_04/`). The repository is structured to guide students through progressive web development concepts.

### Key Characteristics
- **Language**: Primary instruction in Spanish (español)
- **Student Level**: Beginner (fundamentals of HTML, CSS, JavaScript)
- **Structure**: Day-by-day folders containing lessons and exercises
- **Technologies**: HTML, CSS, JavaScript, Python (Flask for local dev server)

## Running Projects

### Starting the Development Server

Most HTML exercises use a Flask development server. To run any HTML project:

```bash
pip3 install flask && python3 server.py
```

The server runs on `http://*******:3000` (check `server.py` for the exact host configuration).

### How `server.py` Works
- Looks for `index.html` in the current directory and serves it
- If `app.py` exists, runs it as a Python application
- Serves static files (CSS, JS, images) automatically
- Disables caching for development

## Repository Structure

```
4geeks_academy_spain_fs_pt_129/
├── day_01/           # HTML/CSS fundamentals
│   └── html-hello/   # Basic HTML template & Instagram card project
├── day_04/           # Terminal, commands, and file paths
│   └── index.md      # Tutorial on CLI usage and paths
└── WARP.md          # This file
```

### Day-by-Day Organization
Each `day_XX/` folder represents a teaching session with:
- Tutorial documents (`.md` files in Spanish)
- Exercise projects (e.g., `html-hello/`)
- Progressive learning materials

## Current Teaching Projects

### Day 01: HTML Hello & Instagram Card

**Location**: `day_01/html-hello/`

**Purpose**: Incremental learning project teaching HTML/CSS layout through building an Instagram post card in three steps:

1. **Step 1** (`step1-layout-boxes.html`): Basic structure with colored boxes to visualize layout
2. **Step 2** (`step2-flexbox-layout.html`): Apply Flexbox for positioning
3. **Step 3** (`step3-final-styled.html`): Final styling with real content

**Key Files**:
- `index.html` - Landing page with links to all three steps
- `README-instagram-card.md` - Teaching guide with learning goals
- `server.py` - Flask development server

**Teaching Approach**: Visual progression from abstract boxes → flexbox layout → finished design

### Day 04: Terminal Commands and Paths

**Location**: `day_04/index.md`

**Purpose**: Comprehensive tutorial (in Spanish) covering:
- Terminal/CLI basics
- Essential commands (`pwd`, `ls`, `cd`, `mkdir`, `touch`, `rm`, `cp`, `mv`)
- Absolute vs relative paths (both system-level and in HTML/CSS)
- Practical exercises

**Key Topics**:
- System paths: `/Users/erwin/projects/file.txt`
- HTML relative paths: `css/style.css`, `../images/logo.png`
- HTML absolute paths: `/css/style.css`, full URLs

## Working with This Repository

### When Creating New Lessons
- Follow the `day_XX/` naming convention
- Include Spanish tutorials as `.md` files
- For HTML projects, copy the `html-hello/` structure (including `server.py`)
- Create progressive examples when teaching complex concepts

### When Modifying Existing Projects
- Preserve the incremental learning approach
- Keep colored boxes in early steps for visual learning
- Update both English (`README.md`) and Spanish (`README.es.md`) documentation
- Test with `python3 server.py` before committing

### File Naming Conventions
- Use lowercase and hyphens: `my-file.html`
- Progressive steps: `step1-description.html`, `step2-description.html`
- Spanish READMEs: `README.es.md`
- Teaching guides: `README-project-name.md`

## Student Context

Students in this cohort are:
- Learning web development fundamentals
- Following a part-time schedule
- Working through materials in Spanish
- Building projects incrementally
- Expected to practice terminal commands alongside coding

### Common Student Tasks
- Running local development servers with Flask
- Creating HTML/CSS layouts
- Understanding file paths (both system and web)
- Using terminal commands for file management
- Building projects step-by-step with guidance

## Technologies & Dependencies

### Python
- **Flask**: Local development server for HTML projects
- Installation: `pip3 install flask`

### Web Technologies
- HTML5
- CSS3 (Flexbox focus)
- JavaScript (minimal, for future lessons)

### No Build Tools
This is a beginner repository - no webpack, npm, or complex build processes. Everything runs directly in the browser via Flask server.
