import asyncio
import typing
from xoa_driver import testers

# high-level function
def create_testers(hosts: typing.List[str], username: str) -> typing.List["testers.GenericAnyTester"]:
    return [ testers.L23Tester(host, username) for host in hosts ]

async def my_awesome_func():
    known_hosts = [
        "192.168.1.195",
        "192.168.1.196",
        "192.168.1.197",
        "192.168.1.198",
        "192.168.1.199",
        "192.168.1.200",
        ]
        
    testers_pool = create_testers( known_hosts, "xoa")
    # now we can do ``await testers_pool[0]`` which establishes the connection

    # we also can use asyncio.gather for await all testers at once in concurrent mode
    await asyncio.gather(*testers_pool) 
    print(testers_pool[0].session.is_online)

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()