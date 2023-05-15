# -*- coding: utf-8 -*-
"""YT Koala7B 8bit for Free in Colab with T4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10QPfcDt39uGciEDqdYBAbPBNZQDoC99O
"""

!pip -q install git+https://github.com/huggingface/transformers # need to install from github
!pip -q install datasets loralib sentencepiece 
!pip -q install bitsandbytes accelerate

"""# Koala 7B loading in 8bit on a T4"""

!nvidia-smi

from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig, pipeline
import torch
import textwrap

tokenizer = LlamaTokenizer.from_pretrained("samwit/koala-7b")

base_model = LlamaForCausalLM.from_pretrained(
    "samwit/koala-7b",
    load_in_8bit=True,
    device_map='auto',
)

!nvidia-smi

import textwrap

pipe = pipeline(
    "text-generation",
    model=base_model, 
    tokenizer=tokenizer, 
    max_length=512,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.15
)

def wrap_text_preserve_newlines(text, width=110):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')

    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text

"""## Run it as a HF model"""

# Commented out IPython magic to ensure Python compatibility.
# %%time 
# output = pipe('BEGINNING OF CONVERSATION: USER: \
# What are the difference between Llamas, Alpacas and Koalas?')
# print(wrap_text_preserve_newlines(output[0]['generated_text']))
#

# Commented out IPython magic to ensure Python compatibility.
# %%time 
# output = pipe('BEGINNING OF CONVERSATION: USER: \
# Write a short note to Sam Altman giving reasons to open source GPT-4')
# 
# print(wrap_text_preserve_newlines(output[0]['generated_text']))

# Commented out IPython magic to ensure Python compatibility.
# %%time 
# output = pipe('BEGINNING OF CONVERSATION: USER: What is the capital of England? \n')
# 
# print(wrap_text_preserve_newlines(output[0]['generated_text']))

# Commented out IPython magic to ensure Python compatibility.
# %%time 
# output = pipe('BEGINNING OF CONVERSATION: USER: Write a story about a Koala playing pool and beating all the camelids.')
# 
# print(wrap_text_preserve_newlines(output[0]['generated_text']))

# Commented out IPython magic to ensure Python compatibility.
# %%time 
# output = pipe('BEGINNING OF CONVERSATION: USER: As an AI do you like the Simpsons? What dow you know about Homer?')
# 
# print(wrap_text_preserve_newlines(output[0]['generated_text']))