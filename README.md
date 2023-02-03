# SchemaGPT

> **Note:** The generated RDF Schemas are not 100% accurate and may require manual correction.

SchemaGPT is a Python library that utilizes the power of OpenAI's GPT-3 and [schema.org](https://schema.org) vocabulary to generate RDF Schemas from natural language.

The library aims to simplify the process of creating RDF Schemas by automatically generating them from a user-defined description written in natural language.

The generated Schemas are in the form of RDF, a popular data model for semantic web technologies, making it easier for developers to work with linked data.

## Who can benefit from using this library?

Anyone who wants to simplify the process of creating RDF Schemas for linked data can benefit from using the SchemaGPT library. This includes software developers, data scientists, semantic web practitioners, and anyone else who needs to work with RDF data. The library is especially useful for those who are not familiar with the intricacies of RDF Schema creation, as it provides a way to generate Schemas from a natural language description, making the process much easier and faster.


## Installation

To install SchemaGPT, simply run the following command using `pip`:

```bash
pip install schemagpt
```
or using `Poetry`:
```bash
poetry add schemagpt
```

## Usage

Using SchemaGPT is straightforward. Here's a simple example:

```python
from schemagpt import SchemaGPT

generator = SchemaGPT(<YOUR_OPENAI_API_KEY>)
schema = generator.schema("Tesla Model X")
print(schema)
```

This will generate the following RDF Schema:
```json
{
  "@context": "https://schema.org",
  "@type": "Car",
  "name": "Tesla Model X",
  "brand": {
    "@type": "Brand",
    "name": "Tesla"
  },
  "model": "Model X"
}
```

## Features
| Feature | Status |
| :------- | :------: |
| Schemas generation/updates using natural language | :white_check_mark: |
| Schemas validation/fixes (according to schema.org) with Pydantic | :construction: |

## Supported formats for RDF Schemas

| Format | Description | Status |
| :------ | :----------- | :------: |
| RDF/XML | The standard XML format for RDF | :x: |
| Turtle | A terse, human-readable RDF syntax | :x: |
| N-Triples | A line-based, plain-text format for RDF | :x: |
| N-Quads | A line-based, plain-text format for RDF with context information | :x: |
| JSON-LD | A JSON-based format for RDF | :white_check_mark: |

## Contribution
SchemaGPT is open-source. If you have an idea for a new feature, or you've found a bug, please feel free to open an issue or submit a pull request.
