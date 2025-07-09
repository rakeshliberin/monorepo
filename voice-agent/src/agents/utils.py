from pathlib import Path

import yaml


def load_prompt(filename: str) -> str:
    """
    Load prompt from a YAML file.
    """
    prompt_dir = Path(__file__).parent / "prompts"
    with open(prompt_dir / filename, "r") as file:
        content = yaml.safe_load(file)
    return content.get("instructions", "")


def load_instructions(filename: str) -> str:
    base_prompt = load_prompt("base_prompt.yaml")
    router_prompt = load_prompt(filename)

    return base_prompt.replace("[[Agent-specific instructions]]", router_prompt)


def load_markdown(filename: str) -> str:
    """
    Load prompt from a Markdown file.
    """
    prompt_dir = Path(__file__).parent / "prompts"
    with open(prompt_dir / filename, "r") as file:
        return file.read()
