"""
PHA - Push Accumulator.

Pushes a copy of the accumulator on to the stack

Processor Status after use:

+------+-------------------+--------------+
| Flag | Description       | State        |
+======+===================+==============+
|  C   | Carry Flag        | Not affected |
+------+-------------------+--------------+
|  Z   | Zero Flag         | Not affected |
+------+-------------------+--------------+
|  I   | Interrupt Disable | Not affected |
+------+-------------------+--------------+
|  D   | Decimal Mode Flag | Not affected |
+------+-------------------+--------------+
|  B   | Break Command     | Not affected |
+------+-------------------+--------------+
|  V   | Overflow Flag     | Not affected |
+------+-------------------+--------------+
|  N   | Negative Flag     | Not affected |
+------+-------------------+--------------+

+-----------------+--------+-------+--------+
| Addressing Mode | Opcode | Bytes | Cycles |
+=================+========+=======+========+
| Implied         |  0x48  |   1   |   3    |
+-----------------+--------+-------+--------+

See also: PLA
"""
import m6502


def test_cpu_ins_pha_imp() -> None:
    """
    Push Accumulator, Implied.

    TODO: Add check to not cross page

    return: None
    """
    memory = m6502.Memory()
    cpu = m6502.Processor(memory)
    cpu.reset()
    cpu.reg_a = 0xF0
    memory[0xFCE2] = 0x48
    memory[cpu.stack_pointer] = 0x00
    cpu.execute(3)
    assert (
        cpu.program_counter,
        cpu.stack_pointer,
        cpu.cycles,
        memory[cpu.stack_pointer + 1],
    ) == (0xFCE3, 0x01FC, 3, 0xF0)
