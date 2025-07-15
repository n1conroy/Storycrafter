def build_story(character, genre, twist, style):
    return (
        f"Write the opening scene of a {style} {genre} story. "
        f"The main character is {character}. The story should include this twist: {twist}. "
        "End the scene with two exciting options for what could happen next."
    )

def continue_story(history, choice):
    full_story = "\n\n".join(history)
    return (
        f"Continue the following story based on the user choice: '{choice}'.\n\n"
        f"{full_story}\n\n"
        "End the new scene with two new choices."
    )

def generate_choices(text):
    import re
    return re.findall(r"\b(?:1\.|2\.|-)\s*(.+)", text)[-2:]
