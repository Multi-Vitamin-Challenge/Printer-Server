import win32api
import win32print


class Driver:
    def __init__(self):
        self.__device__ = 0
        self.__printers__ = []

    def all_printers(self):
        self.__printers__ = [printer[2] for printer in win32print.EnumPrinters(2)]
        return self.__printers__

    def choose_device(self, device):
        self.__device__ = device
        win32print.SetDefaultPrinter(self.__printers__[self.__device__])


    def print(self, location):
        win32api.ShellExecute(0, "print", location, None,  ".",  0)


if __name__ == "__main__":
    temp = Driver()
    print(temp.all_printers())
    temp.choose_device(2)
    temp.print(r"\\wsl$\Ubuntu\home\trx\Printer-Server\TempPdf\print.pdf")