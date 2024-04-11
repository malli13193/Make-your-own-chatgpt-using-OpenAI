import openai
mykey="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"
openai.api_key=mykey
all_models=openai.models.list()
list(all_models)
