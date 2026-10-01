# Omnibus

## Project Overview

Omnibus is an AI-powered multimodal comic book discovery and search engine.

The goal is to build a real search and recommendation system that allows users to discover comic books using natural language, structured filters, and eventually images.

This is an AI/ML portfolio project. The project should demonstrate understanding of:

* Semantic search
* Text embeddings
* Vector similarity search
* Information retrieval
* Recommendation systems
* Multimodal search
* API integration
* Data processing
* Database design
* Full-stack development

The project should NOT become a generic chatbot, simple API wrapper, or static comic database.

The AI should be used to solve meaningful search, retrieval, ranking, and recommendation problems.

---

# Primary Goal

Build a search engine where users can ask questions such as:

* "Find dark Batman stories involving organized crime."
* "Find Marvel comics about cosmic horror."
* "Find comics similar to Batman: The Long Halloween."
* "Find comics featuring both Spider-Man and Daredevil."
* "Find superhero comics involving time travel."
* "Find comics written by Grant Morrison involving Batman."
* "Find comics with themes of identity and loss."

The system should understand the meaning of the query rather than relying exclusively on keyword matching.

---

# Core Architecture

The intended architecture is:

```
User
↓
React Frontend
↓
Backend API
↓
Query Processing
↓
Semantic Search
↓
Vector Database
↓
Ranked Results
↓
Frontend
```

Comic data should come from legitimate public APIs or datasets.

Comic metadata should be normalized and stored locally rather than repeatedly requesting external APIs for every search.

Text embeddings should be generated from relevant comic metadata/descriptions.

Vector similarity should be used for semantic retrieval.

Traditional database filters should be combined with semantic search when appropriate.

---

# MVP

The first version should remain intentionally small.

The MVP should include:

1. Comic API/data ingestion
2. Local database
3. Normalized comic records
4. Text embeddings
5. Vector storage/search
6. Natural-language search
7. Search result ranking
8. Comic detail page
9. "Find Similar Comics" functionality
10. Basic responsive frontend
11. GitHub repository with clear commit history

Do NOT implement every planned feature immediately.

The MVP must work end-to-end before major features are added.

---

# Planned Features

Features should be implemented roughly in this order.

## Phase 1: Foundation

* Project setup
* Frontend
* Backend
* Database
* Comic API integration
* Data ingestion
* Normalized comic schema

## Phase 2: Semantic Search

* Select embedding model
* Generate comic embeddings
* Store embeddings
* Implement vector similarity search
* Natural-language search
* Search result ranking

## Phase 3: Recommendations

* "Find Similar Comics"
* Similarity scoring
* Similar comic cards
* Recommendation explanations

## Phase 4: Structured Search

Support filtering by:

* Character
* Creator
* Publisher
* Release year
* Team
* Genre
* Story arc

Semantic search and structured filters should be able to work together.

## Phase 5: Comic Knowledge Graph

Create relationships between:

* Comics
* Characters
* Creators
* Teams
* Publishers
* Events
* Story arcs

Example:

```
Batman
→ appears in → Batman: Year One
→ written by → Frank Miller
→ set in → Gotham City
→ related to → Batman: The Long Halloween
```

The graph should support exploration and potentially graph-based recommendations.

## Phase 6: Multimodal Search

Add image embeddings.

Users should eventually be able to:

* Upload a comic cover
* Find visually similar covers
* Search using an image
* Combine image and text search

Image similarity should be based on an actual embedding model, not an LLM simply describing the image.

---

# AI Principles

## Do Not Build an LLM Wrapper

The project should not simply send every query to an LLM and ask:

"Which comics should I recommend?"

The retrieval system must perform actual search.

Preferred architecture:

```
User Query
↓
Query embedding
↓
Vector similarity search
↓
Candidate comics
↓
Optional metadata filtering/ranking
↓
Results
```

An LLM may be used for:

* Query interpretation
* Query expansion
* Recommendation explanations
* Natural-language summaries

But the LLM should not replace the retrieval system.

---

# Embeddings

Embeddings should represent the semantic content of comics.

Potential text used for embeddings:

* Title
* Description
* Characters
* Creators
* Publisher
* Genres
* Story information

Do not blindly concatenate every field.

Experiment with what information produces useful semantic results.

Document embedding decisions in the project.

For image search, use a multimodal/image embedding model such as CLIP or an appropriate alternative.

---

# Search Requirements

Search should support natural-language queries.

Example:

"dark Batman stories involving crime"

The system should be able to retrieve relevant comics even if the comic description does not contain those exact words.

Search should eventually combine:

```
Semantic similarity
+
Metadata filters
+
Ranking
```

Do not assume vector similarity alone will always produce the best result.

---

# Similar Comic Requirements

Given a comic:

"Batman: The Long Halloween"

the system should be able to find other comics with similar characteristics.

Similarity may consider:

* Story description
* Characters
* Themes
* Genre
* Creators
* Setting
* Other metadata

The system should store enough information to explain why two comics were considered similar.

---

# Recommendation Explanations

If explanations are added, the explanation should be generated from actual retrieved evidence.

Bad:

"This comic is similar because it has a dark atmosphere."

Good:

"This comic was retrieved because its description shares themes of organized crime, corruption, and Batman's investigation of Gotham's criminal organizations."

The explanation must not invent facts that are not present in the available comic data.

---

# Database Principles

Use a real database rather than storing the entire application state in frontend code.

Separate:

* Comic records
* Characters
* Creators
* Publishers
* Teams
* Genres
* Relationships
* Embeddings

Avoid unnecessary duplication.

Database design should support future expansion without requiring a complete rewrite.

---

# API Principles

External APIs should primarily be used during ingestion or synchronization.

Do not make the frontend depend directly on third-party APIs unless there is a strong reason.

The application should have its own backend API.

External API failures should not completely destroy the application's functionality once data has been ingested.

Cache data when appropriate.

Respect API rate limits and terms of use.

Do not scrape websites unless explicitly approved.

---

# Frontend Principles

The frontend should feel like a real search engine rather than an AI demo.

Core interface:

* Search bar
* Search results
* Comic cards
* Filters
* Comic detail page
* Similar comics

The UI should prioritize usability and information density.

Avoid unnecessary animations and decorative components.

---

# Code Quality

Prefer simple, understandable implementations.

Do not introduce unnecessary abstractions.

Do not add libraries when a straightforward implementation already exists.

Keep components and functions focused.

Use descriptive names.

Keep configuration separate from application logic.

Never hardcode API keys or secrets.

Use environment variables for secrets.

Do not commit `.env` files containing secrets.

---

# Testing

Important functionality should have tests.

Prioritize testing:

* Data normalization
* API parsing
* Embedding generation
* Similarity calculations
* Search behavior
* Database operations
* Backend endpoints
* Important frontend behavior

Tests should be added as features are implemented rather than all at the end.

---

# GitHub Workflow

GitHub is an important part of this project.

The commit history should clearly demonstrate incremental development.

## Commit Frequently

Make small, meaningful commits.

Do NOT wait until an entire feature is finished before committing.

Good commit examples:

* `Initialize React frontend`
* `Add FastAPI backend`
* `Add comic database schema`
* `Implement comic API ingestion`
* `Normalize comic metadata`
* `Add embedding generation`
* `Store comic embeddings`
* `Implement vector similarity search`
* `Add semantic search endpoint`
* `Create search results UI`
* `Add similar comics feature`
* `Add comic detail page`
* `Add search filters`
* `Add search tests`

Avoid commits such as:

* `stuff`
* `changes`
* `update`
* `final`
* `fixed everything`

Commit messages should describe the actual change.

---

# Git Rules for Claude Code

Before making major changes:

1. Check the current Git status.
2. Check the current branch.
3. Understand recent commits when necessary.
4. Do not overwrite existing work without understanding it.

After completing a small logical unit of work:

1. Run relevant tests.
2. Check for obvious errors.
3. Check Git diff.
4. Commit the completed change when appropriate.

Claude should favor several small commits over one enormous commit.

Do not automatically push to GitHub unless explicitly instructed.

Do not create commits containing:

* API keys
* passwords
* tokens
* `.env` secrets
* generated credentials
* unnecessary build artifacts
* large temporary files

Before committing, check that sensitive information is not being included.

---

# Development Workflow

For each feature:

1. Understand the existing implementation.
2. Define the smallest useful change.
3. Implement it.
4. Test it.
5. Inspect the diff.
6. Commit it.
7. Move to the next logical feature.

Do not implement multiple unrelated features in one change.

If a feature becomes substantially larger than expected, stop and reassess the scope instead of silently expanding the project.

---

# Scope Control

The biggest risk of this project is scope creep.

The following are NOT MVP requirements:

* Multiple comic APIs
* Full Marvel/DC databases
* Perfect recommendations
* Complete comic knowledge graph
* Image search
* OCR
* Reading-order generation
* AI-generated comic summaries
* User accounts
* Social features
* Mobile application
* Comic purchasing
* Full comic issue text analysis

These may be added later.

Never sacrifice a working MVP to implement advanced features prematurely.

---

# Definition of Done for MVP

The MVP is complete when a user can:

1. Open the website.
2. Enter a natural-language comic query.
3. Submit the query.
4. Have the query converted into an embedding.
5. Search the comic vector database.
6. Receive ranked results.
7. Open a comic.
8. See its metadata.
9. Request similar comics.
10. Receive semantically related comics.

The system should work using real comic data.

---

# Project Philosophy

This project is intended to demonstrate engineering and AI understanding.

Every major AI component should have a reason to exist.

Before adding an AI component, ask:

"What problem does the AI solve here?"

Avoid adding AI merely because the project is supposed to be an AI project.

The project should demonstrate understanding of the difference between:

* Keyword search
* Semantic search
* Vector similarity
* Recommendation
* Structured filtering
* Knowledge graphs
* Generative AI
* Multimodal retrieval

---

# When Unsure

If a requested feature conflicts with the project's scope or architecture:

1. Explain the conflict.
2. Suggest the smallest implementation that fits the project.
3. Prefer preserving the existing architecture.
4. Do not introduce major technologies without a clear reason.

If there are multiple reasonable implementation choices, prefer the one that:

1. Teaches useful concepts.
2. Is easy to understand.
3. Is maintainable.
4. Keeps the MVP achievable.
5. Adds meaningful portfolio value.

Do not optimize for complexity.

The goal is a finished, technically meaningful AI search engine, not the largest possible application.
