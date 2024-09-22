json_schema = {
    "type": "object",
    "properties": {
        "ru": {"type": "string"},
        "meta": {"type": "string"},
        "ky": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "object",
                        "properties": {
                            "ky": {"type": "string"},
                            "ru": {"type": "string"},
                        },
                        "required": ["ky", "ru"],
                    },
                    "translations": {"type": "array", "items": {"type": "string"}},
                    "examples": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "ru": {"type": "string"},
                                "ky": {"type": "array", "items": {"type": "string"}},
                            },
                            "required": ["ru", "ky"],
                        },
                    },
                },
                "required": ["description", "translations", "examples"],
            },
        },
        "ref": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "word": {"type": "string"},
                    "description": {
                        "type": "object",
                        "properties": {
                            "ky": {"type": "string"},
                            "ru": {"type": "string"},
                        },
                        "required": ["ky", "ru"],
                    },
                },
                "required": ["word", "description"],
            },
        },
    },
    "required": ["ru", "meta", "ky"],
}

system_message = f"""You are an expert assistant tasked with converting Russian-Kyrgyz dictionary entries into a structured JSON format. Your output should strictly adhere to the given schema, ensuring the data is well-organized and accurate. Follow the field guidelines below:

Field Details:
- "ru": A string field representing the dictionary entry’s key, which is the word or phrase in Russian. This field acts as the main reference for the entry.
- "meta": A string field containing metadata about the word, such as part of speech, grammatical gender, and usage notes. Examples of metadata include "ср.", "сов.", "несов.", "нареч." etc.
- "ky": An array containing multiple objects. Each object includes the following fields:
    - "translations": An array listing the Kyrgyz translations of the Russian word. Each translation is provided as a separate string, and this section must contain only Kyrgyz texts, without any additional explanations or comments.
    - "description": An object with the following subfields:
        - "ky": Contains explanations or additional information about the word, written exclusively in Kyrgyz. Do not include translations here, but you may provide context, usage notes, or cultural explanations.
        - "ru": Contains explanations or additional information written exclusively in Russian, providing context, usage, or cultural notes relevant to the word. Examples could include "полит.", "перен.", "церк.", etc. This section must only include Russian text.
    - "examples": An array of objects that provide example sentences to illustrate the word’s usage:
        - "ru": An example sentence in Russian.
        - "ky": The translation of the example sentence in Kyrgyz. You can list multiple translations to showcase different nuances.
- "ref": An object for linking related dictionary entries, helping users understand connections between words and offering additional context.

Use the schema provided below to structure your output accordingly:

{json_schema}
"""
