# publish.ps1
# Run this any time Claude gives you a new index.html in this folder.
# It commits whatever changed and pushes it to GitHub, which triggers
# an automatic GitHub Pages redeploy (usually live within ~1 minute).

Set-Location "$HOME\OneDrive - University of Waterloo\Desktop\Portfolio\Yoav-Gudes-Portfolio"

git add -A

if (git status --porcelain) {
    git commit -m "Update portfolio"
    git push
    Write-Host "`nPublished! Check https://yoavgud.github.io/Yoav-Gudes-Portfolio/ in about a minute." -ForegroundColor Green
} else {
    Write-Host "`nNo changes to publish - the folder already matches the last push." -ForegroundColor Yellow
}
