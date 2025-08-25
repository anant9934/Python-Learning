def func(name, ending="thank you!"):
    print("good day, ",name)
    print(ending)

func("John")
func("John", "goodbye!")  # Using a different ending
func("John", ending="see you later!")  # Using a keyword argument
func("John", ending="take care!")  # Using another keyword argument
    