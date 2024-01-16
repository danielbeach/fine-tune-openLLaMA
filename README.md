### Fine Tuning OpenLLaMA on blog posts.

This repo is to showcase how to fine-tune `OpenLLaMA` on a `GPU` machine. This codebase
is for a `Data Engineering` audience. It's not really about doing a LLM fine-tune correctly,
as much as simply learning the general flow and steps that would be, and should be automated
in a Production environment.

This is a learning exercise.

The dataset used to fine-tune this model was a series of `100` blog posts
from `https://dataengineeringcentral.substack.com/`. It seems most probable that
fine-tuning a LLM would be done on `unstructured` data ... meaning a fair amount
of Data Engineering would need to be done to take `unstructured` data -> `semi-structured` data.

`There are a few main steps at the high level`
- gather data
- format data
- code to train
- deploy to GPU machine
- setup tooling (installs etc.)
- run training
- save model adapter


#### General Notes for Data Engineers interested in `LLM` fine-tuning etc.
Here are some general comments that some DE's might find useful when it comes to 
playing with LLMs in a Production environment (which probably includes fine tuning).
- You will probably be working on a `Linux` instance to do that actual work.
- You will probably heavily use `Docker` because of the above.
- There are lots of Python tools to `pip` install and manage.
- Playing with LLMs requires ALOT of `memory` AND `disk` in real life.
- Eventually you will need GPUs (check out `vast.ai` for cheap by the hour rentals.)
- Because of remote GPU machines, `Docker` etc. You need to understand `bash` and `ssh` commands.
- Data cleaning and prep is going to be the hardest part and the most code.
- Choose your LLM model upfront because it will affect everything downstream.
- Choose your perfered libraries up front for training and inference (ex, `huggingface`)
- Lots of scripts to deploy your `code` and `data` to cloud storage (ex `s3`) will make your life easier when deploying to remote `GPU` machines.

#### This codebase can be read in conjunction with a  blog post to make this more clear.
Coming soon to `https://dataengineeringcentral.substack.com/` search `LLM` to see Part 1
that gives a high level overview of LLMs (local inference on a laptop).
https://dataengineeringcentral.substack.com/p/demystifying-the-large-language-models


#### The Idea
In this codebase I decided to scrape my own blog posts to use for data for fine-tuning the `openLLaMA`
model. I wanted the model to "pick up on my voice and style."

#### The Code
1. `src/extracting_blog_posts.py` <- this script extracted the blog posts that
were `HTML` files. A sample can be see in `blog_posts` folder.

`bs4` is used to extract the contents, eventually the final data is written to a `JSON` file.
See `src/blog_posts.json` for a sample of what it looked like in the end.

The raw data sample can be seen in `blog_posts/` folder (`HTML` files)

Below you can see the format that the raw data is pushed into ...
```
[{
"conversations":[
{"from": "human", "value": "Write a blog post titled {blog post title}"},
{"from": "gbt", "value": "{blog post text}"}
]}]
```

2. The actual training on the `GPU` is done with `src/fine_tune_openllama.py`
See that script for more details.

Check out `vast.ai` to rent cheap GPUs by the hour. This training only cost me a few dollars.

3. the `GPU` machine must have all the requirements installed. This includes all tooling, the base model, etc. (depending on how you're getting your data onto the machince, you might need the `aws cli` etc.)
See `requirements.txt`
- `openllama_7b` parameter model is used as the base.
- `git clone https://huggingface.co/openlm-research/open_llama_7b`
- of course you need `apt-get install git-lfs` to get that above command to work.

#### Docker
Run the following Docker command to build the image `docker build . --tag=llm-fine-tuning`

If you want to manually drop into the container and tie the local volume to play around ... 
`docker run -v ${PWD}:/app/ -it llm-fine-tuning /bin/bash`

#### To Extract the Blog Posts
`docker-compose up blogs` 

#### To Fine-Tune the Model
`docker-compose up finetune`
