@echo off
rem Run SonarScanner using Docker (no local installation required)
rem Ensure Docker Desktop is running and environment variables SONAR_HOST_URL and SONAR_TOKEN are set.

set "PROJECT_ROOT=%~dp0..\.."
pushd "%PROJECT_ROOT%"

docker run --rm ^
    -e SONAR_HOST_URL=%SONAR_HOST_URL% ^
    -e SONAR_TOKEN=%SONAR_TOKEN% ^
    -v "%CD%":/usr/src ^
    -w /usr/src ^
    sonarsource/sonar-scanner-cli

popd
