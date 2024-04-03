mkdir bin


pushd Install

call install-offline.bat

popd


pushd Content

rmdir /s /q build
rmdir /s /q dist
del Sandbox.exe DrEase-Console.exe DrEase.exe  config.JSON
pyinstaller --onefile --windowed --icon="Icon\meds.ico" Sandbox.py
move dist\Sandbox.exe
rename Sandbox.exe DrEase.exe
pyinstaller --onefile --icon="Icon\meds.ico" Sandbox.py
move dist\Sandbox.exe
rename Sandbox.exe DrEase-Console.exe
rmdir /s /q build
rmdir /s /q dist

popd

xcopy /hiev Content\DrEase.exe bin
xcopy /hiev Content\DrEase-Console.exe bin
xcopy /hiev Content\Themes bin
xcopy /hiev Content\databases bin
PAUSE
