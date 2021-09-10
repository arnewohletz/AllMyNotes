Command Pattern
---------------
Issue
`````
* The invoker (i.e. a button of a remote control) is supposed to be linked to various
  actions being executed when invoked
* The amount and behaviour of these actions are open to change and must therefore be
  configurable
* As a plus, the executed action(s) should be reversible

For example, the remote control's "On" button is supposed to turn a TV on, but also turn
it off, if it is already running.

Naming
``````

:Client:
    class that requests a command being executed

:Receiver:
    class which actually performs the requested actions behind a command

:Invoker:
    class that maps all possible command slots (i.e. button of a remote) to a certain
    command's *execute()* method

:Command:
    interface class that defines a structure of any concrete command class

:ConcreteCommand:
    implementation of *Command* interface that calls certain functions on the *Receiver*
    upon being executed

Solution
````````

.. admonition:: Definition
    :class: pattern_definition

    The **Command Pattern** encapsulates a request as an object, thereby letting you
    parameterize other objects with different requests, queue or log requests, and support
    undoable operations.

.. mermaid::
    :align: center

    classDiagram
        Command "0..*" <-- Invoker : HAS-A
        Command<|--ConcreteCommand : implements
        Receiver<--ConcreteCommand : HAS-A
        class Invoker {
            +set_command(Command)
        }
        class Command {
            <<interface>>
            +execute()
            +undo()
        }
        class Receiver {
            +action_1()
            +action_2()
        }
        class ConcreteCommand {
            +execute()
            +undo()
        }

* The *Receiver* contains all possible action methods (e.g. *action_1()*, *action_2()*, ...)
  -> these are depending on the actual nature of the *Receiver* (i.e. a light might have an
  *on()* and *off()* method)
* The *Invoker* has a *Command* interface instance for every "slot" that requires a *Command*
  being executed upon activation (i.e. a four button remote requires four *Command* instances)
* The *Invoker* defines a method for calling each "slot"-Command's *execute()* method (i.e.
  *light_on_button_pressed()*)
* The *Command* interface defines an *execute()* method and should also contain an *undo()*
  method to revert an executed command's action
* Any *ConcreteCommand* class contains a *Receiver* instance, which the *execute()* and
  *undo()* methods act upon
* The *Client* is the one actually using the pattern:

    * it instantiates an *Invoker* ("You have access to the methods I want to execute") -> HAS-A
    * it instantiates a *Receiver* ("You are the one I actually want to do something!") -> HAS-A

Routine:
    * The *Client* instantiates the *Invoker*, thereby passing the *ConcreteCommand* 's as arguments,
      which themselves take a receiver as an argument
    * The *Client* calls the *Invoker*'s method, that executes the corresponding command's
      *execute()* method

Advantages:

    * Commands can execute other commands instead of directly acting on the *Receiver* (Macro-Commands
      like turning on multiple lights)
    * Undoing commands is easy to do -> enable the user to undo previous commands is often a smart
      way to structure and application, instead of just executing things

Example
```````
Find a template example for Python at https://refactoring.guru/design-patterns/command/python/example

.. hint::

    As an alternative to using "Command setter" methods in the *Invoker* class, you may pass the
    *ConcreteCommand* instances into the Invoker's constructor and assign it right away.

    It might be safer, not being able to reassign the commands in the invoker during runtime,
    but instead create multiple *Invoker* classes, which all assign commands differently. It
    also ensures, that Invokers cannot be instantiated without specifying all required commands.

.. literalinclude:: _code/command.py
    :language: python

