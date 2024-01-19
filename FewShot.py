import os
from openai import AzureOpenAI
import re

client = AzureOpenAI(api_key=os.getenv("AZURE_OPENAI_KEY"),
                    api_version="2023-12-01",
                    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
                    )

def perfrom_few_shot_classification(text):

    print('training few shot examples started')

    user_content = f"""
                    Classify the text into one of the classes.
                    Classes: ['positive', 'negative', 'neutral']

                    Text: Dancing in rain makes me happy.
                    Class: 'positive'

                    Text: Journey was terrible beacuse my flight got cancelled due to bad weather.
                    Class: 'negative'
                    
                    Text: I love my pet dog "Bruno".
                    Class: 'positive'

                    Text: Movie is neither too good nor too bad, It's just average.
                    Class:'neutral'

                    Text:{text}
                    Class:
                """



    deployment_name='gpt-35-turbo'
    response = client.completions.create(
                model=deployment_name,
                prompt=[user_content],
                temperature=0
            )

    return response.choices[0].text


sample = "I am so addicted to movies from the Marvel studio are outstanding and world class"
#sample = "It's so disgusting to see ManUtd losing to Bayern in the Champions league quater finals."


category = perfrom_few_shot_classification(sample)

category_match = re.search(r'positive|nagative|neutral', category)

if category_match:
    category = category_match.group()
    print(category)
else:
    print("Category not found.")