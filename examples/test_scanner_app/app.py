"""
Detection callback w/ scanner
--------------

Example showing what is returned using the callback upon detection functionality

Updated on 2020-10-11 by bernstern <bernie@allthenticate.net>

"""

import asyncio
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
import logging
from tkinter import *

logging.basicConfig()


async def run_tk(root, interval=0.05):
    '''
    Run a tkinter app in an asyncio event loop.
    '''
    try:
        while True:
            root.update()
            await asyncio.sleep(interval)
    except TclError as e:
        if "application has been destroyed" not in e.args[0]:
            raise


async def main():

    ws = Tk()
    ws.title('TestScanner')
    ws.geometry('800x600')
    text_box = Text(ws)
    text_box.pack(expand=True)

    scanner = BleakScanner()

    def on_scan_result(device: BLEDevice, advertisement_data: AdvertisementData):
        message = 'Discovered {} - {}\n'.format(device.name, device.address)
        print(message)
        text_box.insert('end', message)

    scanner.register_detection_callback(on_scan_result)
    
    await scanner.start()
    await run_tk(ws)


if __name__ == "__main__":
    asyncio.run(main())
