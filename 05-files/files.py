def readFile(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as error:
        return f'Soubor nebyl nalezen: {error}'
    except Exception as error:
        return f'Doslo k nejakemu problemu pri otevirani souboru {error}'
    finally:
        file.close()
    return data

print(readFile('./python.txt'))