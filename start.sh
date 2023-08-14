sudo mount -o remount,rw /
sudo systemctl start e32
sudo mount -o remount,ro /
sleep 1
./e32ws
