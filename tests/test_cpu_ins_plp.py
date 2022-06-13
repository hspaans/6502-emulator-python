"""
PLP - Pull Processor Status.

Pulls an 8 bit value frm the stack and into the processor flags. The flags
will take on new states as determined by value pulled.

Processor Status after use:

+------+-------------------+----------------+
| Flag | Description       | State          |
+======+===================+================+
|  C   | Carry Flag        | Set from stack |
+------+-------------------+----------------+
|  Z   | Zero Flag         | Set from stack |
+------+-------------------+----------------+
|  I   | Interrupt Disable | Set from stack |
+------+-------------------+----------------+
|  D   | Decimal Mode Flag | Set from stack |
+------+-------------------+----------------+
|  B   | Break Command     | Set from stack |
+------+-------------------+----------------+
|  V   | Overflow Flag     | Set from stack |
+------+-------------------+----------------+
|  N   | Negative Flag     | Set from stack |
+------+-------------------+----------------+

+-----------------+--------+-------+--------+
| Addressing Mode | Opcode | Bytes | Cycles |
+=================+========+=======+========+
| Implied         |  0x28  |   1   |   4    |
+-----------------+--------+-------+--------+

See also: PHP
"""
import m6502


def test_cpu_ins_plp_imp() -> None:
    """
    Pull Processor Status.

    TODO: Implement instruction and test
    TODO: Add check to not cross page

    :return: None
    """
    memory = m6502.Memory()
    cpu = m6502.Processor(memory)
    cpu.reset()
    memory[0xFCE2] = 0x28
    assert True
