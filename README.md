pytest -m smoke
pytest -m regression\

Our CI architecture

GitHub Actions Runner
│
├── PostgreSQL 15
│     :5432
│
├── Redis 7
│     :6379
│
├── Medusa
│     Node 20
│     pnpm 10
│     :9000
│
└── QA Repository
      Python
      Poetry
      Playwright
      Pytest

dtc-starter-clean
        ↓
   Application

DTC-STARTER-FRESH-QA
        ↓
   Automation