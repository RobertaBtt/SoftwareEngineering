## Python

### Interpreter and compiler

A **compiler** translates the program it receives as in inputn, in machine language.

Are compiled languages like C and C++, Delphi and Visual Basic.
The processor executes the machine's instructions that is
the assembly list of instructions.

The assembler translates it in binary code (0,1).

At the end the Linker converts eventually other binaries (link them together).

An **interpreter** executes the program starting directly from the source code, 
that is without a previous compilation.

Note:
``For whatever language it is possible to write an interpreter or a compiler.``

The lanuages that are interpreter are immediately elaborated:
example of PHP.

**Java** is an example of language that is compiled but also interpreted.
The source code it is compiled into bytecode, and then, this bytecode, it is interpreter
from the Java Virtual Machine that interprets "on the fly" the bytecode machine instructions.

The Java Virtual Machine has to be developed for every Operating System.

The performance is not satisfactory because the code has to be interpreted from the
Java Virtual Machine that delegates the execution to the Operating System.

### Python

Python is a pseudo-compiled language.
The code is analyzed and transformed into bytecode (.pyc, .pyo)
in the pre-compilation phase.

To execute this bytecode, a particular interpreter is used, 
called Python Virtual Machine (PVM)

The fact that is pseudo-interpreted makes it portable, 
but, once the code is written, it can be interpreted on 
the majority of the platforms, if they have the correct version of the interpreter.

Moreover in the match calculations, the speed of execution is not one of the
strengths of Python.

Psyco is an extension, a Just in Time compilation that speed up some types of code.

The Python Language reference describes the exact syntax of the language.

There are different interpretations of Python:

CPython is the most used, it is written in C.

Jython is Python implemented in Java (-_-)

### How interpretation works
A program in Python is read by a parser, that creates the tokens, in Unicode format.
The termination lines can be logical or physical, like a "return to line", 
written as an ASCII "LF" (Line Feed) or ASCII CR (Carriage Return).

Encoding declaration

    # -*- coding: <utf..> -*-
