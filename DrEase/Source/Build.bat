
rmdir /s /q build
rmdir /s /q dist
del Sandbox.exe DrEase-Console.exe DrEase.exe config.JSON Sandbox.spec


pyinstaller --onefile --windowed --icon="Icon\meds.ico" Sandbox.py
move dist\Sandbox.exe
rename Sandbox.exe DrEase.exe
pyinstaller --onefile --icon="Icon\meds.ico" Sandbox.py
move dist\Sandbox.exe
rename Sandbox.exe DrEase-Console.exe

rmdir /s /q build
rmdir /s /q dist
del Sandbox.exe config.JSON Sandbox.spec
