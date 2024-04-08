pushd Dependencies

call install-offline.bat

popd


pushd ..\Source

call Build.bat

popd



setlocal
set /p directoryName=<pathToInstall.txt



pushd ..\Source

rmdir /s /q %directoryName%bin
mkdir %directoryName%bin
xcopy DrEase.exe %directoryName%bin\ /i
xcopy DrEase-Console.exe %directoryName%bin\ /i
xcopy Themes\ %directoryName%bin\Themes\ /s /e /i
xcopy Icon\ %directoryName%bin\Icon\ /s /e /i
xcopy databases\ %directoryName%bin\databases\ /s /e /i
xcopy Docs\ %directoryName%bin\Docs\ /s /e /i

popd
start  %directoryName%bin
endlocal
