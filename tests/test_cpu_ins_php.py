"""
PHP - Push Processor Status.

Pushes a copy of the status flags on to the stack.

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
| Implied         |  0x08  |   1   |   3    |
+-----------------+--------+-------+--------+

See also: PLP
"""
import m6502


def test_cpu_ins_php_imp() -> None:
    """
    Push Accumulator, Implied.

    TODO: Implement instruction and test
    TODO: Add check to not cross page

    return: None
    """
    memory = m6502.Memory()
    cpu = m6502.Processor(memory)
    cpu.reset()
    memory[0xFCE2] = 0x08
    assert True
