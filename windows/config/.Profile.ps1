$ENV:__ShellDepth = [int] $ENV:__ShellDepth + 1

Import-Module PSColor
$global:PSColor = @{
    File = @{
        Default    = @{ Color = 'White' }
        Directory  = @{ Color = 'DarkGray'}
        Hidden     = @{ Color = 'White'; Pattern = '^\.' } 
        Code       = @{ Color = 'Magenta'; Pattern = '\.(java|c|cpp|cs|js|css|html)$' }
        Executable = @{ Color = 'Red'; Pattern = '\.(exe|bat|cmd|py|pl|ps1|psm1|vbs|rb|reg)$' }
        Text       = @{ Color = 'Yellow'; Pattern = '\.(txt|cfg|conf|ini|csv|log|config|xml|yml|md|markdown)$' }
        Compressed = @{ Color = 'Green'; Pattern = '\.(zip|tar|gz|rar|jar|war)$' }
    }
    Service = @{
        Default = @{ Color = 'White' }
        Running = @{ Color = 'DarkGreen' }
        Stopped = @{ Color = 'DarkRed' }     
    }
    Match = @{
        Default    = @{ Color = 'White' }
        Path       = @{ Color = 'DarkGray'}
        LineNumber = @{ Color = 'Yellow' }
        Line       = @{ Color = 'White' }
    }
	NoMatch = @{
        Default    = @{ Color = 'White' }
        Path       = @{ Color = 'DarkGray'}
        LineNumber = @{ Color = 'Yellow' }
        Line       = @{ Color = 'White' }
    }
}


function Prompt_git_repo_status {
    $is_repo = $false
    $dir = $PWD

    while ($dir -ne '') {
        if (Test-Path "$dir\.git" -PathType Container) {
            $is_repo = $true
            break
        }
        $dir = Split-Path $dir -Parent
    }
    
    if (-not $is_repo) {
        return ''
    }

    $ESC = [char]27
    $result = "$ESC[01;34m[git:"

    # Get branch name, change color depending on edits
    $branch = git rev-parse --abbrev-ref HEAD
    $result += "$ESC[00;37m" + $branch

    # Check for uncommitted changes
    $git_status = git status --porcelain
    if (-not [string]::IsNullOrEmpty($git_status)) {
        $result += "$ESC[01;37m{" + $git_status.Split("`n").Count + "}"
    }

    $result += "$ESC[01;34m] "

    return $result

}

function Prompt_shell_level {
    $ESC = [char]27

    if ($env:__ShellDepth -gt 1) {
        return "$ESC[01;30m(" + $env:__ShellDepth + ") "
    }

    return ''
}

function Prompt_user_priv {
    $ESC = [char]27

    $is_running_as_admin = (New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator);

    if ($is_running_as_admin) {
        return "$ESC[01;31m"  + $env:USERNAME + "@" + $env:USERDOMAIN + " ";
    }
    return "$ESC[01;32m"  + $env:USERNAME + "@" + $env:USERDOMAIN + " ";
}

function Prompt {
    $ESC = [char]27

    $prompt = Prompt_shell_level
    $prompt += Prompt_git_repo_status
    $prompt += Prompt_user_priv
    $prompt += "$ESC[01;36m" + $PWD
    $prompt += "$ESC[0m " + '>' * ($nestedPromptLevel + 1) + ' '

    return $prompt
}