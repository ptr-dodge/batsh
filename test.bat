@echo off
setlocal EnableDelayedExpansion
setlocal EnableExtensions

rem Function call
set _1=World
set _0=Hello
call :func1 _7 0 _0 _1
echo | set /p ^=!_7!
rem Global and local variables
set v1=Global V1
set v2=Global V2
set v3=Global V3
set _2=Var
call :func2 _8 0 _2
echo | set /p ^=!_8!
echo !v1!
echo !v3!
rem Return value
set /a _3=4
call :func3 _9 0 _3
echo | set /p ^=!_9!
echo:
set /a _4=1
call :func3 _10 0 _4
set ret=!_10!
echo Returned: !ret!
rem Argument containing space
set _5=Param with space
call :f _11 0 _5
set test=!_11!
echo !test!
rem List files
for /f "delims=" %%i in ('dir /w') do set files=%%i
rem Test existence
if exist file1.txt (
  echo file1.txt exists.
)
if exist file2.txt (
  set /a existence=1
) else (
  set /a existence=0
)
if !existence! EQU 1 (
  echo file2.txt exists.
)
if exist file3.txt (
  set /a _6=1
) else (
  set /a _6=0
)
if !_6! NEQ 1 (
  echo file3.txt does not exist.
)

goto :EOF
:func1
set p1_%~2=!%~3!
set p2_%~2=!%~4!
echo !p1_%~2! !p2_%~2!

goto :EOF
:func2
set p_%~2=!%~3!
set v1_%~2=Local !p_%~2!
echo !v1_%~2!
echo !v2!
set v3=V3 Modified.

goto :EOF
:func3
set num_%~2=!%~3!
set /a _0_%~2=^(!num_%~2! + 41^)
set %~1=!_0_%~2!
goto :EOF

goto :EOF
:g
set text_%~2=!%~3!
set %~1=!text_%~2!
goto :EOF

goto :EOF
:f
set text_%~2=!%~3!
set _0_%~2=!text_%~2!
set /a _2_%~2=^(1 + %~2^)
call :g _3_%~2 !_2_%~2! _0_%~2
set _1_%~2=!_3_%~2!
set %~1=!_1_%~2!
goto :EOF