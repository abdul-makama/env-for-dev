# 🧠 Smart AI Agent Environment (Gemini 2.0 Flash)

An intelligent, customizable development assistant built using Google Gemini 2.0 Flash — designed for developers and professionals who want AI agents tailored to their roles, skills, tone, and domains of expertise.

---

## 🚀 Features

- 🛠️ **Agent Profiles** – Create, edit, and manage AI agent configurations.
- 🧠 **Context-Aware Interaction** – AI replies are scoped to agent settings (e.g. role, domain experience).
- 🔄 **Session Memory** – (Optional) Retain history during runtime for smarter conversations.
- 🧪 **Smart Exit & Out-of-Scope Detection** – Dynamically detects when to exit or reject prompts beyond the agent’s domain.
- 🧰 **Streamlit UI** – Clean, interactive visual interface to manage and chat with agents.
- 📦 **Profile Storage** – Load, rename, delete, and save profiles as JSON files.
- 🔑 **API Key Handling** – Supports both `.env` and runtime key entry.

---

## 🖼️ Interface Overview

| Section | Description |
|--------|-------------|
| 🔑 API Key Input | Enter your Google Generative AI key if not found in `.env`. |
| 📂 Profile Manager | Add, rename, delete, or switch agent profiles. |
| 🧠 Agent Settings | Define role, domain experience, skills, tone, response size, and more. |
| 💬 Chat Panel | Prompt your agent based on the selected profile. |
| ❌ Smart Guardrails | Auto-detects irrelevant prompts or exit intentions. |

---

## 🧩 Agent Profile Attributes

Each agent has the following configurable fields:

- `name`: Profile identifier
- `role`: AI agent role (e.g. Product Manager, Software Engineer)
- `domain_experience`: List of expertise domains (e.g. finance, agriculture)
- `skills`: Specific abilities or tools the agent should be familiar with
- `tone`: Casual, professional, friendly, etc.
- `response_size`: Small, medium, or large
- `max_response_tokens`: Upper limit for LLM output
- `language`: Preferred language (e.g. English)
- `knowledge_cutoff`: Knowledge scope (e.g. "2024")

---

## 🏗️ Project Structure

