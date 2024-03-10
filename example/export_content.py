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
