


SoundGet, master_mute, , mute, 13 ; afficher l'icone en fonction de l'état du microphone
if (master_mute = "Off")
    Menu, Tray, Icon, C:\Users\lukap\Downloads\icons8-microphone-50-modified.png
else
    Menu, Tray, Icon, C:\Users\lukap\Downloads\icons8-mute-unmute-50-modified.png


ScreenPos :=false




F13::
Run Arc
return

F14::
Run, "C:\Users\lukap\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk"
return

F15::
Run "C:\Users\lukap\AppData\Local\Programs\Microsoft VS Code\Code.exe"
return

F16::
Run, https://github.com
return

F17::
Run "C:\Users\lukap\AppData\Local\Programs\Arduino IDE\Arduino IDE.exe"
return

F18::
DesktopIcons( Show:=-1 )                  ; By SKAN for ahk/ah2 on D35D/D495 @ tiny.cc/desktopicons
{
    Local hProgman := WinExist("ahk_class WorkerW", "FolderView") ? WinExist()
                   :  WinExist("ahk_class Progman", "FolderView")

    Local hShellDefView := DllCall("user32.dll\GetWindow", "ptr",hProgman,      "int",5, "ptr")
    Local hSysListView  := DllCall("user32.dll\GetWindow", "ptr",hShellDefView, "int",5, "ptr")

    If ( DllCall("user32.dll\IsWindowVisible", "ptr",hSysListView) != Show )
         DllCall("user32.dll\SendMessage", "ptr",hShellDefView, "ptr",0x111, "ptr",0x7402, "ptr",0)
}
return

F19::
Run, C:\Users\lukap\Downloads\MonitorProfileSwitcher_v0700\MonitorSwitcher.exe -load:C:\Users\lukap\AppData\Roaming\MonitorSwitcher\Profiles\GUICREATEDPROFILENAME.xml, , Hide,
return

F20::
DllCall("PowrProf\SetSuspendState", "int", 0, "int", 1, "int", 0)
return

F21::
DllCall("LockWorkStation")
return


F22::
    F22State := Mod(F22State + 1, 2)
    if (F22State = 1) {
        Send ^a
        Send ^c
        Send {Esc}
    } else {
        Send ^v
        Send {Enter}
        F22State := 0
    }
return

F23::  ; mute le micro
SoundSet, +1, MASTER, mute,13 ;13 was my mic id number use the code below the dotted line to find your mic id. you need to replace all 12's  <---------IMPORTANT
SoundGet, master_mute, , mute, 13

if (master_mute = "Off"){
    Menu, Tray, Icon, C:\Users\lukap\Downloads\icons8-microphone-50-modified.png
    SoundPlay, C:\Users\lukap\Downloads\pop-sound-effect-226108.mp3
}
else{
    Menu, Tray, Icon, C:\Users\lukap\Downloads\icons8-mute-unmute-50-modified.png
    SoundPlay, C:\Users\lukap\Downloads\snap-sound-effect-226112.mp3
}
return




F24::       ;permet de tourner l'écran
if (ScreenPos = false){
    Send ^+{right}
    ScreenPos := true
}
else{
    Send ^+{up}
    ScreenPos := false
}
return