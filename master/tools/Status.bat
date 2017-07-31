@Echo Off
setlocal enabledelayedexpansion

set Times=0
for /f "skip=1" %%p in ('wmic cpu get loadpercentage') do (
    set Cpusage!Times!=%%p
    set /A Times+=1
)


echo CPU Percentage = %Cpusage0%%%
echo CPU Percentage = %Cpusage0%%%>>.\..\\..\\Result\log\System_Status.txt

SetLocal EnableExtensions

For /F "Skip=1 Tokens=*" %%A In (
   'WMIc OS Get FreePhysicalMemory^,TotalVisibleMemorySize') Do (
   For %%B In (%%A) Do If Not Defined _ (Set/A _=100*%%B) Else (Set/A _=_/%%B)
)
Echo(Free Memory = %_%%%>>.\..\\..\\Result\log\System_Status.txt
Echo(Free Memory = %_%%%