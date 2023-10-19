sudo cp ./change_host.plist /Library/LaunchDaemons
sudo launchctl unload /Library/LaunchDaemons/change_host.plist
sudo launchctl load /Library/LaunchDaemons/change_host.plist
rm -f *.log
