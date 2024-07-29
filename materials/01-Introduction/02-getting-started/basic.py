"""
One of the most basic gem5 scripts you can write.

This boots linux (just the kernel) and exits. However, we will only run it for
20 ms to save time.

This takes just a minute or so to run.

gem5 basic.py
"""

from gem5.prebuilt.demo.x86_demo_board import X86DemoBoard
from gem5.resources.resource import obtain_resource
from gem5.simulate.simulator import Simulator

# We're going to use one of the pre-built demo boards

board = X86DemoBoard()

board.set_workload(obtain_resource("x86-ubuntu-24.04-boot-no-systemd"))  # type: ignore

sim = Simulator(board=board)
sim.run(20_000_000_000)  # 20 ms, 20 billion ticks = 20 billion picoseconds

# run with `gem5-mesi basic.py`
