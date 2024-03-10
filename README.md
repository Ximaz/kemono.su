# kemono.su

This project aims to export all the content from a `creator` from the
[`https://kemono.su`](https://kemono.su) website.

# The exposed functions

You may want to use some exposed function to write your own scripts, or use the
ones in the `example` folder.

### Exposed functions

- `get_creators`: Returns the list of all the `creator`s from `kemono.su`
- `get_creator`: Returns a specific `creator` depending on their usernmae
- `get_creator_gallery`: Returns up to **`50`** gallery URLs for a `page` of a `creator`
- `get_creator_entire_gallery`: Computes all possible iterations of the `get_creator_gallery` for a `creator`
- `get_creator_posts`: Returns all the posts for one gallery URL
- `get_creator_entire_posts`: COmputes all possible iterations of the `get_creator_posts`

### Example

Here is a short snippet in order for you to export all the content of a creator.

```python
# File path: example/export_content.py
import json
import sys


sys.path.append("..")
import kemono


def main(argc: int, argv: list[str]):
    if 1 == argc:
        print("You must supply a creator username")
        sys.exit(1)

    creator = kemono.get_creator(name=argv[1])
    if None is creator:
        print("The specified creator was not found: %s" % (argv[1]))
    gallery_urls = kemono.get_creator_entire_gallery(creator=creator)
    posts = kemono.get_creator_entire_posts(gallery_urls=gallery_urls)
    with open("posts.json", "w+") as output:
        json.dump(posts, output, indent=4)
    output.close()

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
```
