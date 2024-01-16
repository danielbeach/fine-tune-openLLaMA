import bs4
from glob import glob
import json


def get_blog_posts(dir: str = "blog_posts/*.html") -> list:
    blog_posts = glob(dir)
    return blog_posts


def extract_blog_posts(blog_posts: list) -> list:
    blogs = "[\n"
    for blog_post in blog_posts:
        print(f"Extracting {blog_post}...")
        blogs += "{\n"
        blogs += '"conversations":[\n'
        blog_post_title = extract_blog_title_from_filename(blog_post)
        human_template = {"from": "human", "value": "Write a blog post titled {}".format(blog_post_title)}
        blogs +=json.dumps(human_template)
        blogs += ","
        with open(blog_post, "r") as f:
            soup = bs4.BeautifulSoup(f.read(), "html.parser")
            content = soup.get_text()
            ai_template = {"from": "gpt", "value": "{}".format(content)}
            blogs += "\n"
            blogs += json.dumps(ai_template)
            blogs += "\n]"
            blogs += "\n},"
    blogs += "]"
    with open("blog_posts.json", "w") as f:
        f.write(blogs)


def extract_blog_title_from_filename(file_name: str) -> str:
    return file_name.split(".")[1].split(".html")[0].replace("-", " ")



if __name__ == "__main__":
    blog_posts = get_blog_posts()
    prepped_blogs = extract_blog_posts(blog_posts)
