# uep_rag_assistant


## 📁 Struktura projektu

Stosujemy podejście oparte na przejrzystej architekturze z modułowymi komponentami. Poniżej znajduje się układ katalogów:

```text
uep_rag_assistant/
├── .github/                      # Workflowy CI/CD 
│   └── workflows/
├── docs/                         # Dokumentacja dla deweloperów i użytkowników 
├── scripts/                      # Skrypty pomocnicze (np. uruchamianie scrapera, reset bazy)
├── src/
│   ├── uep_rag_assistant/        # Główna paczka projektu (serce całej logiki aplikacji)
│   ├── config/                   # Konfiguracje Pydantic (zmienne środowiskowe, flagi, sekrety)
│   ├── core/                     # Logika domenowa: modele danych, walidacja, enumy
│   │   └── models.py             # np. Program, CandidateQuery, SurveyResponse
│   ├── ingestion/                # Web scraping i pobieranie/przetwarzanie plików PDF
│   ├── preprocessing/            # Czyszczenie tekstu, segmentacja, dzielenie na fragmenty
│   ├── embeddings/               # Logika embedowania (Jina)
│   ├── vectorstore/              # Interfejs do bazy wektorowej (FAISS – możliwa podmiana)
│   ├── retrieval/                # Logika RAG: retriever, prompty, klient LLM
│   ├── api/                      # Endpointy FastAPI: chatbot, admin, healthcheck
│   ├── ui/                       # Frontend 
│   ├── evaluation/               # Ankiety, AI-as-a-judge, benchmarking
│   └── tests/                    # Testy jednostkowe/integracyjne (pytest)
├── Dockerfile                    # Kontener do uruchamiania aplikacji (produkcja/dev)
├── docker-compose.yml            # Lokalny stack developerski (np. wektor DB, UI, Redis)
├── pyproject.toml                # Konfiguracja Poetry: zależności, meta, skrypty, config
├── poetry.lock                   # Zablokowane wersje pakietów dla pełnej powtarzalności
├── Makefile                      # Skróty poleceń: `make lint`, `make run`, `make docs`
├── README.md                     # Opis projektu, instalacja, diagram architektury
└── CHANGELOG.md                  # Historia zmian, wersjonowanie, nowe funkcjonalności
```

Każdy podfolder może zawierać plik README z opisem logiki, jeśli to potrzebne. Dzięki temu baza kodu pozostaje skalowalna, testowalna i łatwa do zrozumienia dla członków zespołu.
