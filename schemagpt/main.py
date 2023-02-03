import json
import logging
import sys
from typing import Any

import openai

from schemagpt.exceptions import EmptyPromptError, UnsupportedRDFSchemaStandard
from schemagpt.prompts import SCHEMA_EXAMPLES, rdf_schema_prompt
from schemagpt.types import GPTModel, SchemaStandard

logging.basicConfig(
    stream=sys.stdout, level=logging.INFO, format="%(name)s - %(message)s"
)
logger = logging.getLogger("SchemaGPT")


class SchemaGPT:
    _supported_schema_standards = SCHEMA_EXAMPLES.keys()

    def __init__(
        self,
        openai_api_key: str,
        model: GPTModel = "text-davinci-003",
        temperature: float = 0.0,
        max_tokens: int = 800,
        top_p: float = 1.0,
        frequency_penalty: float = 0.0,
        presense_penalty: float = 0.0,
    ):
        openai.api_key = openai_api_key
        self.model_params = {
            'model': model,
            'temperature': temperature,
            'max_tokens': max_tokens,
            'top_p': top_p,
            'frequency_penalty': frequency_penalty,
            'presence_penalty': presense_penalty,
        }

    @property
    def model(self) -> GPTModel:
        return self.model_params['model']

    @model.setter
    def model(self, model: GPTModel) -> None:
        self.model_params['model'] = model

    @property
    def temperature(self) -> float:
        return self.model_params['temperature']

    @temperature.setter
    def temperature(self, temperature: float) -> None:
        self.model_params['temperature'] = temperature

    @property
    def max_tokens(self) -> int:
        return self.model_params['max_tokens']

    @max_tokens.setter
    def max_tokens(self, max_tokens: int) -> None:
        self.model_params['max_tokens'] = max_tokens

    @property
    def top_p(self) -> float:
        return self.model_params['top_p']

    @top_p.setter
    def top_p(self, top_p: float) -> None:
        self.model_params['top_p'] = top_p

    @property
    def frequency_penalty(self) -> float:
        return self.model_params['frequency_penalty']

    @frequency_penalty.setter
    def frequency_penalty(self, frequency_penalty: float) -> None:
        self.model_params['frequency_penalty'] = frequency_penalty

    @property
    def presence_penalty(self) -> float:
        return self.model_params['presence_penalty']

    @presence_penalty.setter
    def presence_penalty(self, presence_penalty: float) -> None:
        self.model_params['presence_penalty'] = presence_penalty

    def schema(
        self,
        prompt: str | None = None,
        initial_schema: dict = {},
        standard: SchemaStandard = "JSON-LD"
    ) -> dict[str, Any]:
        if prompt is None:
            raise EmptyPromptError("Prompt cannot be empty for schema generation request!")

        if standard not in self._supported_schema_standards:
            raise UnsupportedRDFSchemaStandard(f"{standard} standard isn't supported for schemas!")

        prompt = rdf_schema_prompt.format(
            standard=standard,
            example=SCHEMA_EXAMPLES[standard],
            initial_schema=initial_schema,
            prompt=prompt,
        )

        try:
            response = openai.Completion.create(**self.model_params, prompt=prompt)

            return json.loads(response.choices[0].text)

        except Exception as error:
            logger.error(error)
