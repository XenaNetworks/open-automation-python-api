import asyncio

from xoa_driver import testers
from xoa_driver import modules

async def my_awesome_func():
    # create tester instance and establish connection
    tester = await testers.L23Tester("192.168.1.200", "xoa")

    # get access to instance of module under slot 0
    my_module = tester.modules.obtain(0) 

    # check if module is of types which we are suspecting
    if not isinstance(my_module, modules.ModuleChimera):
        print(my_module.info.media_info_list)

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()