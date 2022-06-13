"""
PLA - Pull Accumulator.

Pulls an 8 bit value from the stack and into the accumulator. The zero andi
negative flags are set as appropriate.

Processor Status after use:

+------+-------------------+--------------------------+
| Flag | Description       | State                    |
+======+===================+==========================+
|  C   | Carry Flag        | Not affected             |
+------+-------------------+--------------------------+
|  Z   | Zero Flag         | Set is A = 0             |
+------+-------------------+--------------------------+
|  I   | Interrupt Disable | Not affected             |
+------+-------------------+--------------------------+
|  D   | Decimal Mode Flag | Not affected             |
+------+-------------------+--------------------------+
|  B   | Break Command     | Not affected             |
+------+-------------------+--------------------------+
|  V   | Overflow Flag     | Not affected             |
+------+-------------------+--------------------------+
|  N   | Negative Flag     | Set if bit 7 of A is set |
+------+-------------------+--------------------------+

+-----------------+--------+-------+--------+
| Addressing Mode | Opcode | Bytes | Cycles |
+=================+========+=======+========+
| Implied         |  0x68  |   1   |   4    |
+-----------------+--------+-------+--------+

See also: PHA
"""
import m6502


def test_cpu_ins_pla_imp() -> None:
    """
    Pull Accumulator, Implied.

    TODO: Add check to not cross page

    return: None
    """
    memory = m6502.Memory()
    cpu = m6502.Processor(memory)
    cpu.reset()
    cpu.reg_a = 0x00
    cpu.stack_pointer = 0x01FB
    memory[0xFCE2] = 0x68
    memory[0x01FB] = 0xF0
    cpu.execute(2)
    assert (
        cpu.program_counter,
        cpu.stack_pointer,
        cpu.cycles,
        cpu.reg_a,
    ) == (0xFCE3, 0x01FC, 2, 0xF0)
