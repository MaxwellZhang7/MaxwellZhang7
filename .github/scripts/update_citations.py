from scholarly import scholarly
import re

USER_ID = "xIPk_pgAAAAJ"  # 替换成你自己的 Google Scholar user id

def get_citations(user_id):
    author = scholarly.search_author_id(user_id)
    scholarly.fill(author, sections=["indices"])
    return author["citedby"]

citations = get_citations(USER_ID)
print(f"Latest citations: {citations}")

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"Google%20Scholar-Citations%20.*?-brightgreen",
    f"Google%20Scholar-Citations%20{citations}%2B-brightgreen",
    content
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
