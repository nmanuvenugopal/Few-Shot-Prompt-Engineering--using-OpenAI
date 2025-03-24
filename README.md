# Text classification-using-OpenAI Prompt Engineering Techniques
## Prompt engineering is used to classify the text. I have used the OpenAI models for this purposes.

Few thing to remember to while doing few shot classification using OpenAI services:
1. We need the subscription from either OpenAI or Miscrosoft Azure (Since I have Microsoft Azure subscription I have used that).
2. Prompts are very very important in this case, a proper prompt can give even better results. It is well tought in tutorials provided by OpenAI.
3. I have kept the tempearture parameter to 0, because it was giving me the best result.

I have used the following prompt for classify the incoming input to either positive , negative or nuetral:
 user_content = f"""
                    Classify the text into one of the classes.
                    Classes: ['positive', 'negative', 'neutral']

                    Text: Dancing in rain makes me happy.
                    Class: 'positive'

                    Text: Journey was terrible beacuse my flight got cancelled due to bad weather.
                    Class: 'negative'
                    
                    Text: I love my pet dog Bruno.
                    Class: 'positive'

                    Text: Movie is neither too good nor too bad, It's just average.
                    Class:'neutral'

                    Text:{text}
                    Class:
                """
If you notice the prompt we are feeding the model with some example, basically we are telling the model that if a similar type sentence or input comes in, then try to classify it to most appropriate category. For example "Dancing in rain makes me happy" conveys a positive statement, so classify it to positive. Similarly "Journey was terrible beacuse my flight got cancelled due to bad weather" in this case the user is sad because his flight got cancelled, so it conveys negative statement, hence classify it to negative category.

The process of giving example like above to make the model to think like human and thus helping model to do their task efficiently and accurately is known as few shot classification.
