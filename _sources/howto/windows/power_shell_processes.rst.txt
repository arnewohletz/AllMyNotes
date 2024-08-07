Control processes with PowerShell
=================================
Processes can be manipulated by referring to their Process ID (PID).

**Get all running processes** (including PIDs):

.. code-block:: powershell

    PS C:\> Get-Process

To **stop a certain process** use its PID:

.. code-block:: powershell

    PS C:\> Stop-Process <PID>

The process is quit immediately and the PID is released for new processes.

To **change the priority of a process** for *APPLICATION.EXE* (edit!) to *XXX* run:

.. code-block:: powershell

    PS C:\> Get-WmiObject Win32_process-filter 'name="APPLICATION.EXE"'|ForEach-Object {$_.SetPriority(XXX)}

where XXX ist set to

    +-------+-------------------+
    | 64    | low               |
    +-------+-------------------+
    | 16384 | less than normal  |
    +-------+-------------------+
    | 32    | normal            |
    +-------+-------------------+
    | 32768 | more than normal  |
    +-------+-------------------+
    | 128   | high              |
    +-------+-------------------+
    | 256   | real-time         |
    +-------+-------------------+

To **get more info** about a process:

.. code-block:: powershell

    PS C:\> Get-Process PROCESS_NAME | Format-List *

like the priority, the process executable path or version

To see the **user rights of a running process** (requires admin console), run

.. code-block:: powershell

    PS C:\> Get-Process PROCESS_NAME -Include-UserName
