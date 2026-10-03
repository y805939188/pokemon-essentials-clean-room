# Pokémon Essentials Clean-Room Specification Project

## Mission

This workspace exists only to study Pokémon Essentials as a reference implementation and extract:

* observable behavior
* game rules
* functional requirements
* domain concepts
* state transitions
* mathematical rules
* input/output behavior
* edge cases
* user-facing workflows
* feature dependencies
* compatibility requirements

The final purpose is to support a later independent clean-room implementation.

This workspace MUST NOT implement the new framework.

---

# Core Principle

Pokémon Essentials is a behavioral reference, NOT an architectural template and NOT a source-code template.

The goal is to answer:

> What behavior and capability does the system provide?

Do NOT answer:

> How should we translate the existing Ruby implementation into TypeScript?

---

# Strict Source Separation Rules

The directory:

`reference/pokemon-essentials/`

contains reference source material.

It is READ-ONLY for this project.

Never:

* modify files under `reference/`
* generate patches for Pokémon Essentials
* refactor Pokémon Essentials
* translate Ruby code into another language
* output copied source-code fragments into specifications
* reproduce substantial source expressions
* preserve source-specific implementation structure unless necessary for analysis
* propose a TypeScript class hierarchy based directly on the Ruby class hierarchy

---

# Clean-Room Output Rules

Specifications must describe behavior independently of source implementation.

Allowed outputs include:

* functional requirements
* domain concepts
* rules
* algorithms expressed mathematically or behaviorally
* state machines
* inputs and outputs
* preconditions and postconditions
* edge cases
* invariants
* examples
* test vectors
* user-visible behavior
* feature dependencies
* compatibility requirements
* implementation-independent pseudocode only when absolutely necessary

Prefer prose, tables, diagrams, state machines, equations and test cases.

Do not reproduce source code.

Do not convert Ruby syntax into pseudocode line-by-line.

Do not preserve method structure merely because the original implementation used it.

---

# Architecture Neutrality

Do NOT assume the future implementation will use:

* Ruby
* RPG Maker XP
* RPG Maker MZ
* TypeScript
* classes
* inheritance
* the original Essentials module structure

Specifications must remain implementation-independent whenever possible.

Architecture recommendations belong in a later independent architecture phase.

---

# Classification Model

Every discovered feature should be classified into one of these conceptual groups when possible:

## Generic Kernel

Capabilities useful to many kinds of games, such as:

* persistence
* random-number services
* events
* configuration
* resource identifiers
* registries
* plugin/extensibility mechanisms

## Creature-RPG

Generic monster/creature collection RPG capabilities, such as:

* creatures
* species
* parties
* inventory
* storage
* encounters
* progression
* evolution
* breeding
* capture
* player/trainer concepts

These specifications should avoid Pokémon-specific assumptions where possible.

## Pokémon Rules

Pokémon-specific mechanics such as:

* Pokémon stats
* IVs
* EVs
* Nature
* Types
* Pokémon-specific evolution conditions
* Pokédex behavior
* Poké Balls
* Pokémon-specific capture mechanics
* Pokémon-specific progression rules

## Combat Requirements

Requirements that the future combat subsystem must satisfy.

Do not prescribe the combat implementation.

## Engine / Overworld Integration

Behavior currently connected to RPG Maker XP or RGSS, such as:

* maps
* events
* player movement
* terrain interaction
* scenes
* graphics
* audio
* input
* save integration

Describe required behavior, not the RMXP implementation.

## User Interface

Observable UX and interaction requirements.

## Demo / Developer Experience

Capabilities demonstrated by the bundled example project and workflows needed by future game developers.

---

# Feature Documentation Standard

Each detailed feature specification should contain, where applicable:

1. Purpose
2. User-visible behavior
3. Domain concepts
4. Inputs
5. Outputs
6. Preconditions
7. State changes
8. Rules and invariants
9. Edge cases
10. Failure behavior
11. Dependencies on other features
12. Configuration/data requirements
13. Example scenarios
14. Test cases or test vectors
15. Classification
16. Open questions
17. Source traceability

---

# Source Traceability

For each specification, record which reference files or demo behavior were inspected.

Traceability is for audit purposes only.

Do NOT reproduce source code in the specification.

Use paths and concise descriptions, for example:

* `Data/Scripts/...`
* inspected demo event behavior
* observed runtime behavior

---

# Workflow

Always work incrementally.

The required order is:

1. Repository reconnaissance
2. High-level module inventory
3. Feature inventory
4. Dependency mapping
5. Specification extraction plan
6. Detailed module-by-module extraction
7. Cross-module consistency review
8. Coverage review
9. Final sanitized specification set

Do not attempt to fully document the repository in a single pass.

---

# Completeness Discipline

When analyzing a domain:

* search for all relevant files
* inspect callers and dependencies when necessary
* look for configuration and data definitions
* inspect related demo usage
* check edge-case handling
* update the global Feature Matrix
* explicitly record uncertainty

Never infer that a feature does not exist simply because it was not found in the first file inspected.

---

# Output Quality

Specifications should be:

* concise but complete
* implementation-independent
* structured
* human-readable
* suitable as input to another AI agent
* suitable for later automated test design

Avoid unnecessary historical commentary.

Avoid documenting Ruby implementation details unless they materially affect observable behavior.

---

# No New Framework Implementation

During this phase, DO NOT:

* create TypeScript packages
* design concrete TypeScript APIs
* create RPG Maker MZ plugins
* implement combat systems
* implement engine adapters
* write production framework code

The deliverable is specification and analysis only.
