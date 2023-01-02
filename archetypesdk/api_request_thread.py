from threading import Thread
import asyncio

def _start_request_loop(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)
    loop.run_forever()


def start_request_thread():
    loop = asyncio.new_event_loop()
    thread = Thread(target=_start_request_loop, args=(loop,), daemon=True)
    thread.start()
    return loop


requests_loop = start_request_thread()