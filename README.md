# 🧠 Monorepo Deployment Guide

This monorepo contains a multi-service architecture for building and running AI-driven voice applications. The stack includes Langfuse (Observability), LiteLLM (LLM proxy), Voice Agent, SIP Gateway, LiveKit (Audio/Video infra), Redis, PostgreSQL, and Prometheus. All services are containerized using Docker Compose.

---

## 🚀 Prerequisites

Ensure the following are installed on your system:

- Docker & Docker Compose
- Node.js and `pnpm` (for Langfuse development)
- macOS or Linux system (recommended)
- Ports like `3000`, `4000`, `5432`, `6379`, `7880`, and `5060` should be free

---

## 🛠️ Full Deployment Steps

### Step 1: Start Langfuse

Langfuse is used to trace and debug interactions between the LLM and the voice agent.

```bash
cd monorepo/langfuse
docker compose -f docker-compose.dev.yml up -d

- Once started, open http://localhost:3000 in your browser.

Step 2: Create Langfuse Project and Generate API Keys
Go to http://localhost:3000

Create a new project

Navigate to Project Settings → API Keys

Generate both Public Key and Secret Key

Step 3: Configure Environment Variables
Update the Langfuse keys in the following environment files:

voice-agent/.env

litellm/.env.example

env

LANGFUSE_PUBLIC_KEY=your_public_key_here
LANGFUSE_SECRET_KEY=your_secret_key_here
You can also configure additional variables as needed for each service.

Step 4: Start Core Services
This command starts PostgreSQL, Redis, Prometheus, and LiteLLM.

bash
cd monorepo
docker compose up db redis prometheus litellm -d


Step 5: Start Voice Agent
Make sure .env is updated with Langfuse keys, then:

docker compose up voice-agent -d

Step 6: Start SIP Gateway
This component handles SIP protocol integration.

# Manual Step 7: Login
lk login --api-key <YOUR_KEY> --api-secret <YOUR_SECRET>

# Step 1: Create the project
lk projects create --name "voice-agent"

# Step 2: Set the current project
lk use-project voice-agent

# Step 3: Create trunks
lk trunks create --from-file inbound-trunk.json
lk trunks create --from-file outbound-trunk.json

# Step 4: Create dispatch rule
lk trunks dispatch-rules create --from-file dispatch-rule.json


