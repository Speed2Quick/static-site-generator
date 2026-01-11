from textnode import TextType, TextNode

def main():

    node = TextNode("this is a test node", TextType.TEXT)

    #testing repr
    print(node)


if __name__ == "__main__":
    main()
