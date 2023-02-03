from schemagpt import SchemaGPT
import os


if __name__ == "__main__":
    openai_api_key = os.environ["OPENAI_API_KEY"]
    generator = SchemaGPT(openai_api_key)

    lambo_schema = generator.schema('Lamborghini Aventador LP 700-4')

    #  Simple schema:
    #
    # {
    #     "@context": "https://schema.org",
    #     "@type": "Car",
    #     "name": "Lamborghini Aventador LP 700-4",
    #     "brand": {
    #         "@type": "Brand",
    #         "name": "Lamborghini"
    #     },
    #     "model": "Aventador LP 700-4",
    # }

    lambo_schema = generator.schema(
        'Car is black, it was produced on 12 June 2019, has 2 doors and 6.5 litres vehicle engine',
        initial_schema=lambo_schema,
    )

    #  Updated schema:
    #
    # {
    #     "@context": "https://schema.org",
    #     "@type": "Car",
    #     "name": "Lamborghini Aventador LP 700-4",
    #     "brand": {
    #         "@type": "Brand",
    #         "name": "Lamborghini"
    #     },
    #     "model": "Aventador LP 700-4",
    #     "vehicleEngine": {
    #         "@type": "EngineSpecification",
    #         "engineDisplacement": {
    #             "@type": "QuantitativeValue",
    #             "value": 6.5,
    #             "unitCode": "LTR"
    #         }
    #     },
    #     "numberOfDoors": 2,
    #     "productionDate": "2019-06-12",
    #     "color": "black"
    # }
