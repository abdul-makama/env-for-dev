import google.generativeai as genai

def configure_api(api_key):
    genai.configure(api_key=api_key)

def ask_gemini(user_input, profile=None):
    if detect_exit(user_input):
        return "EXIT_SIGNAL"

    if profile:
        if not is_in_scope_llm(user_input, profile):
            return "❌ This query seems out of scope for this assistant profile."

    prompt = build_prompt(user_input, profile)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

def detect_exit(user_input):
    prompt = f"""
You are a helpful assistant. Determine if this message indicates the user wants to exit or end the conversation.

Message: "{user_input}"

Respond with only "YES" if they want to exit, or "NO" if they want to continue.
"""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return "yes" in response.text.lower()

def is_in_scope_llm(user_input, profile):
    profile_context = f"""
The assistant is a {profile['role']} with experience in {', '.join(profile['domain_experience'])}.
They only respond to questions related to these areas and subtopics.
"""
    prompt = f"""
{profile_context}

Determine whether the following user input is relevant to this assistant's scope.

User Input: "{user_input}"

Respond with only "YES" if it is in scope, or "NO" if it is out of scope.
"""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return "yes" in response.text.lower()

def build_prompt(user_input, profile):
    if not profile:
        return f"You are a general-purpose helpful AI assistant. Respond to: {user_input}"

    return f"""
You are an AI assistant acting as a {profile['role']} with experience in {', '.join(profile['domain_experience'])}.
You have the following skills: {', '.join(profile['skills'])}.
Respond in a {profile['tone']} tone.
Language: {profile['language']}
Limit your response to {profile['response_size']} size (around {profile['max_response_tokens']} tokens).
Your knowledge cutoff is {profile['knowledge_cutoff']}.

User query: {user_input}
"""
