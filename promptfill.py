from pathlib import Path
from string import Template
from typing import Union

def load_prompt(file_path: Union[str, Path], **kwargs) -> str:
    """
    Loads a prompt text or markdown file and injects variables dynamically.
    
    Args:
        file_path: Path to the .md or .txt prompt file.
        **kwargs: Variables to replace inside the template.
    
    Returns:
        Formatted prompt string ready for an LLM.
    """
    path = Path(file_path)
    
    if not path.is_file():
        raise FileNotFoundError(f"Prompt file not found at: {file_path}")

    # Read the file content
    content = path.read_text(encoding="utf-8")
    
    # Use built-in string.Template for variable substitution ($variable)
    template = Template(content)
    
    try:
        return template.substitute(**kwargs)
    except KeyError as e:
        raise ValueError(f"Missing prompt variable for placeholder: {e}")