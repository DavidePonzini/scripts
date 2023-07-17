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


function Prompt {
    $ESC = [char]27

    $prompt = "$ESC[1mPS"
    $prompt += "$ESC[0m(" + $ENV:__ShellDepth + ") "
    $prompt += "$ESC[01;32m" + $env:USERNAME + "@" + $env:USERDOMAIN + " "
    $prompt += "$ESC[01;36m" + $PWD
    $prompt += "$ESC[0m" + '>' * ($nestedPromptLevel + 1) + ' '

    return $prompt
}