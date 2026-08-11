param(
    [Parameter(Mandatory=$true)][string]$InputPath,
    [Parameter(Mandatory=$true)][string]$OutputPath
)

$extension = [System.IO.Path]::GetExtension($InputPath).ToLowerInvariant()
if ($extension -eq '.pptx') {
    $application = New-Object -ComObject PowerPoint.Application
    try {
        $presentation = $application.Presentations.Open($InputPath, $true, $true, $false)
        try { $presentation.SaveAs($OutputPath, 32) } finally { $presentation.Close() }
    } finally {
        $application.Quit()
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($application) | Out-Null
    }
} elseif ($extension -eq '.docx') {
    $application = New-Object -ComObject Word.Application
    $application.Visible = $false
    try {
        $document = $application.Documents.Open($InputPath, $false, $false)
        try {
            foreach ($toc in $document.TablesOfContents) { $toc.Update() }
            $document.Repaginate()
            foreach ($toc in $document.TablesOfContents) { $toc.UpdatePageNumbers() }
            $document.Fields.Update() | Out-Null
            $document.Repaginate()
            foreach ($toc in $document.TablesOfContents) { $toc.UpdatePageNumbers() }
            $document.Save()
            $document.ExportAsFixedFormat($OutputPath, 17)
        } finally { $document.Close(0) }
    } finally {
        $application.Quit()
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($application) | Out-Null
    }
} else {
    throw "Unsupported Office extension: $extension"
}

if (-not (Test-Path -LiteralPath $OutputPath)) {
    throw "PDF export did not create $OutputPath"
}
