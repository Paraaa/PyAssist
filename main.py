from wake_word.astra import Astra


if __name__ == "__main__":
    astra = Astra()

    while True:
        astra.listen()
