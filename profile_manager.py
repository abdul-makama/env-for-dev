import os
import json

PROFILE_DIR = "profiles"
os.makedirs(PROFILE_DIR, exist_ok=True)

# Template profiles
TEMPLATE_PROFILES = {
    "Product Manager": {
        "role": "Product Manager",
        "domain_experience": ["software", "startup"],
        "skills": ["roadmapping", "stakeholder management"],
        "tone": "professional",
        "language": "English",
        "response_size": "medium",
        "max_response_tokens": 300,
        "knowledge_cutoff": "2024"
    },
    "UX Designer": {
        "role": "UX Designer",
        "domain_experience": ["web design", "app UX"],
        "skills": ["user research", "prototyping"],
        "tone": "friendly",
        "language": "English",
        "response_size": "short",
        "max_response_tokens": 200,
        "knowledge_cutoff": "2024"
    }
}

def list_profiles():
    return [f.replace(".json", "") for f in os.listdir(PROFILE_DIR) if f.endswith(".json")]

def save_profile(name, profile):
    with open(os.path.join(PROFILE_DIR, f"{name}.json"), "w") as f:
        json.dump(profile, f)

def load_profile(name):
    with open(os.path.join(PROFILE_DIR, f"{name}.json")) as f:
        return json.load(f)

def delete_profile(name):
    os.remove(os.path.join(PROFILE_DIR, f"{name}.json"))

def list_template_profiles():
    return list(TEMPLATE_PROFILES.keys())

def get_template_profile(name):
    return TEMPLATE_PROFILES.get(name)
