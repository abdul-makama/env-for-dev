
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

```
📁 smart-agent-env/
│
├── app.py                   # Streamlit main interface
├── .env                     # (Optional) Store GEMINI_API_KEY here
├── profiles/                # JSON profile storage
│   └── example_profile.json
│
├── profile_manager.py       # Load/save/edit/delete profiles
├── utils.py                 # AI interaction and LLM tools
├── requirements.txt         # Dependencies
└── README.md                # 📘 You are here
```

---

## 🧑‍💻 Getting Started

### 🔧 Requirements
- Python 3.8+
- A free [Google Generative AI API key](https://makersuite.google.com/app/apikey)

### 📥 Installation

```bash
git clone https://github.com/yourusername/smart-agent-env.git
cd smart-agent-env
pip install -r requirements.txt
```

Create a `.env` file and add your API key:
```
GEMINI_API_KEY=your_google_genai_key_here
```

Or enter it at runtime in the UI.

### 🚀 Run the App

```bash
streamlit run app.py
```

---

## 💡 How It Works

When a user submits a prompt:
1. The system checks if the prompt is an **exit signal** (e.g. "I'm done", "quit").
2. It then checks if the prompt is **in scope** for the selected agent profile.
3. If valid, it builds a tailored prompt and queries Gemini 2.0 Flash.
4. Otherwise, it returns a graceful message or exits.

---

## 🔄 Future Improvements

- ✅ Session memory persistence (optional)
- 🌍 Multilingual support
- 📊 User analytics dashboard
- ☁️ Cloud-based profile syncing
- 🔒 Role-based access control

---

## 🤝 Contributing

Pull requests are welcome! Please open issues to suggest features or report bugs.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Abdulmalik Auwal Makama**  
Student, Computer & Communication Engineering – ATBU Bauchi  
Contributor @ Smart Data Links | GDSC ATBU | 3MTT Nigeria

---

## 🌐 Connect

- 📫 Email: [your-email@example.com]
- 💼 LinkedIn: [your-linkedin-profile]
- 💻 GitHub: [github.com/yourusername]
