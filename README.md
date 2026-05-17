# greek-grammar-agent-skill Hermes Agent Skill

A Hermes Agent / Agent Skills compatible skill for Modern Greek grammar.

## Purpose

This skill helps an agent correct, explain, teach, and generate exercises for Modern Standard Greek grammar, including tonos, spelling, cases, nouns, adjectives, pronouns, verbs, aspect, syntax, particles, clitics, and register.

## Installation

Copy the folder to one of these locations:

```bash
mkdir -p ~/.hermes/skills
cp -R greek-grammar-agent-skill ~/.hermes/skills/greek-grammar-agent-skill
```

Or place it in a project skill directory if your Hermes setup scans project-local skills:

```bash
mkdir -p ./skills
cp -R greek-grammar-agent-skill ./skills/greek-grammar-agent-skill
```

Then verify in Hermes:

```bash
hermes skills list
```

Use it by natural language or slash command, depending on your Hermes interface:

```text
/greek-grammar-agent-skill Correct this sentence: Με ο φίλος μου πήγαμε σινεμά.
```

## Structure

```text
greek-grammar-agent-skill/
├── SKILL.md
├── README.md
├── LICENSE
├── assets/
│   └── exercise_templates.md
├── references/
│   ├── ERROR_PATTERNS_AND_FEEDBACK.md
│   ├── NOUNS_ADJECTIVES_PRONOUNS.md
│   ├── ORTHOGRAPHY_AND_ACCENTS.md
│   ├── QUICK_TABLES.md
│   ├── SYNTAX_USAGE_STYLE.md
│   └── VERBS_AND_ASPECT.md
├── scripts/
│   └── validate_skill.py
└── tests/
    └── sample_prompts.md
```

## Scope

Primary scope: Modern Standard Greek / Νέα Ελληνικά.

Out of primary scope: Ancient Greek, Koine, Katharevousa, Cypriot Greek, and dialect-specific grammar. The skill includes instructions to handle those cautiously if requested.

## Validation

Run:

```bash
python3 scripts/validate_skill.py .
```

The validator uses only the Python standard library and checks the basic Agent Skills naming/frontmatter requirements.
