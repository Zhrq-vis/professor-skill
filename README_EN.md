<div align="center">

# Cyber Professor.skill

> *“A professor does not need to be online forever for their research style to stay usable.”*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

**Cyber Professor.skill** turns a professor's published work, public materials, research preferences, and advising style into an interactive research mentor.

It does more than imitate a professor's prior papers. It can also combine:
- the professor's own research corpus,
- the model's general reasoning ability,
- current task context from the student,
- and, when available, fresh literature search results.

The result is a reusable AI research advisor that helps with **topic selection, literature review, experiment design, paper logic, rebuttal preparation, and code scaffolding**.

[Installation](#installation) · [Usage](#usage) · [Core Features](#core-features) · [Project Structure](#project-structure)

</div>

---

## What it does

This is a meta-skill for Agent Skills / Claude Code style environments.

You feed it materials such as:
- papers and preprints
- homepage / CV / lab description
- slides, lectures, interviews, grant text
- a hand-written “professor profile” summary
- the student's draft, experiment plan, and code

It distills them into three layers:

| Layer | Purpose |
|---|---|
| **Research Memory** | topics, methods, trajectory, terminology, representative results |
| **Advising Persona** | advising style, review habits, writing preferences, standards |
| **Action Playbook** | how to guide topic scoping, experiments, writing, defense, code |

---

## Installation

```bash
mkdir -p .claude/skills
git clone https://github.com/YOUR_USERNAME/cyber-professor-skill .claude/skills/create-cyber-professor
```

Optional dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Start with:

```bash
/create-cyber-professor
```

Then provide:
1. alias / short professor handle
2. field, direction, lab or institution
3. source materials
4. desired advisor roles

Invoke the generated skill with:

```bash
/{slug}
```

Useful modes inside the conversation:
- advisor mode
- literature review mode
- experiment design mode
- reviewer mode
- code coach mode
- defense simulation mode

---

## Core Features

- Distill a professor's research agenda and advising style
- Guide students on topic framing and paper positioning
- Design baselines, ablations, metrics, and error analysis
- Produce minimal runnable code scaffolds
- Simulate harsh reviews or oral defenses
- Build a multi-agent “research committee” workflow

---

## Project Structure

```text
create-cyber-professor/
├── SKILL.md
├── prompts/
├── tools/
├── professors/
├── docs/PRD.md
└── LICENSE
```

---

## Credits & References

This project follows common public Agent Skill packaging patterns such as a main `SKILL.md`, supporting prompt templates, and helper scripts. The overall structure was inspired by public repositories including OpenAI `skills`, Anthropic `skills`, and SkillHub. citeturn984477search1turn984477search2turn984477search4turn984477search5

Thanks to:
- colleague.skill
- ex.skill
- yourself.skill
- GPT-5.4
- Claude Code
- VS Code

