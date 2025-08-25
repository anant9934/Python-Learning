import pyjokes
def get_joke():
    """
    Returns a random joke from the pyjokes library.
    """
    return pyjokes.get_joke()
if __name__ == "__main__":
    print(get_joke())
# This code defines a function to get a random joke and prints it if run as a script.
