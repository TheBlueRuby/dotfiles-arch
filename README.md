# Dotfiles

dotfiles 2 or something  
i use arch btw

![](screenshots/screenshot.png)

## Dependencies

- hyprland (i use hyprland-hidpi-xprop-git)
    - brightnessctl (for backlight control)
    - pw-volume (volume control)
        - pipewire
- wezterm
- waybar
- gtklock

also includes configs for:  

- alacritty
- swaylock
    - Loads background from ~/Pictures/desktop-bg.png
- ironbar
    - `bc` needed for volume
- fuzzel
- wlogout

## Installation

The dotfiles repo directory will be represented as $REPO_DIR

1. Backup your .config folder, your .bashrc/.zshrc and .wezterm.lua
2. Install all dependencies above through pacman and aur (i recommend using paru or yay for aur stuff)
3. clone or download this repo
4. copy the contents of this .config folder into your home folder
    - `$ cp -r $REPO_DIR/.config/* ~/.config`
5. copy .wezterm.lua and screenshot.sh into your home directory
6. install the powerline10k theme if using zsh
7. (***OPTIONAL***) copy aliases.sh into your shell rc file
    - Bash: `$ cat aliases.sh >> ~/.bashrc`
    - Zsh: `$ cat aliases.sh >> ~/.zshrc`
