class HelloWorld:
    def __new__(cls, text: str = None):
        if text is None:
            print("Hello World")
        else:
            print(text)
        return None
# world hello
