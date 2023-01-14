import importlib
import filechanges


def change():
    try:
        importlib.reload(filechanges)
        filechanges.print_onchange()

    except:
        pass


for i in range(5):
    change()
    input('hit enter to change...')
