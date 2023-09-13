from transformers import pipeline

generate = pipeline('text-generation',model='bert')