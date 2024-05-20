$venvFolders = Get-ChildItem -Path "C:\Users*" -Filter "venv" -Recurse -Directory
Write-Host "Found virtual environments:"
$venvFolders | ForEach-Object { Write-Host $_.FullName }
