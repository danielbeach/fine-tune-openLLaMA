### Fine Tuning OpenLLaMA on blog posts.

This repo is to showcase how to fine-tune `OpenLLaMA` on a `GPU` machine.
The dataset used to fine-tune this model was a series of `100` blog posts
from `https://dataengineeringcentral.substack.com/`.

There are a few main steps at the high level
- gather data
- format data
- code to train
- deploy to GPU machine
- run training
- save model adapter

#### The main files
1. `extracting_blog_posts.py` <- this script extracted the blog posts that
were `HTML` files. A sample can be see in `blog_posts` folder.

`bs4` is used to extract the contents.

The script also formats the data into a format that an be ingested by the
`huggingface` code.

```
[
{
"conversations":[
{"from": "human", "value": "Write a blog post titled {blog post title}"},
{"from": "gbt", "value": "{blog post text}"}
]
}
]
```

2. The actual training on the `GPU` is done with `fine_tune_openllama.py`
See that script for more details.

3. the `GPU` machine must have all the requirements installed.
See `requirements.txt`
- `openllama_7b` parameter model is used as the base.
- `git clone https://huggingface.co/openlm-research/open_llama_7b`
- of course you need `apt-get install git-lfs` to get that above command to work.

#### Docker
Run the following Docker command to build the image `docker build . --tag=llm-fine-tuning`

If you want to manually drop into the container and tie the local volume ... 
`docker run -v ${PWD}:/app/ -it llm-fine-tuning /bin/bash`

#### To Extract the Blog Posts
`docker-compose up blogs` etc.