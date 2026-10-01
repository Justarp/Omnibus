# ComicSeek

A semantic search and recommendation engine for comic books.

Search with natural language, like *"dark Batman stories involving organized crime"* or *"Marvel comics about cosmic horror"*. Results come from what the comics are about, not only from matching keywords.

> **Status:** early development. Phase 1 (foundation) is in progress.

## How it works

```
Query ──► embedding model ──► query vector
                                   │
                                   ▼
           Postgres + pgvector: cosine similarity over comic embeddings
                                   │
                                   ▼
                 metadata filters + ranking ──► results
```

1. **Ingestion:** comic metadata is pulled from the [ComicVine API](https://comicvine.gamespot.com/api/), normalized and stored locally in Postgres.
2. **Embeddings:** each comic's description and key metadata are turned into a vector by a local sentence-transformers model.
3. **Search:** each query is embedded with the same model and compared to comic vectors with pgvector.
4. **Similar comics:** a comic's own vector is used to find its nearest neighbours.

Retrieval is done by actual vector search. An LLM does not choose the results.

## Tech stack

| Layer      | Choice                                   |
|------------|------------------------------------------|
| Frontend   | React + Vite + TypeScript                |
| Backend    | Python, FastAPI, SQLAlchemy              |
| Database   | PostgreSQL 16 + pgvector (Docker)        |
| Embeddings | sentence-transformers (runs locally)     |
| Data       | ComicVine API                            |

## Roadmap

- [ ] **Phase 1: Foundation:** database, backend, ComicVine ingestion, normalized schema
- [ ] **Phase 2: Semantic search:** embeddings, vector search, search endpoint
- [ ] **Phase 3: Recommendations:** similar comics with evidence-based explanations
- [ ] **Phase 4: Structured search:** filters by character, creator, publisher, year and more
- [ ] **Phase 5: Knowledge graph:** relationships between comics, characters and creators
- [ ] **Phase 6: Multimodal search:** cover-image search with CLIP embeddings

## Running locally

Requires [Docker Desktop](https://www.docker.com/products/docker-desktop/).

```bash
cp .env.example .env          # then fill in real values
docker compose up -d          # start Postgres + pgvector on localhost:5432
```

More setup instructions will be added as each component is built.
