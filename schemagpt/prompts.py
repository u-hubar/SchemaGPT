SCHEMA_EXAMPLES = {
    "JSON-LD": (
        """{
    "@context": "https://schema.org",
    "@type": "Car",
    "name": "Tesla Model X",
    "brand": {
        "@type": "Brand",
        "name": "Tesla"
    },
    "model": "Model X"
}"""
    ),
}

rdf_schema_prompt = (
    """You are given the initial RDF Schema using {standard} standard and a prompt. Update RDF
Schema using information from the prompt, use only official types, properties, datatypes,
enumerations and enumeration members from schema.org vocabulary.

Example:
initial schema: {{}}

prompt: Tesla Model X

updated schema:
{example}

initial schema: {initial_schema}

prompt: {prompt}

updated schema:"""
)
