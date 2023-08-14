mount | grep 'type ext4' | grep rw
isRW=$?
echo "booted in ${isRW} "
if [[ $isRW != 0 ]]; then sudo mount -o remount,rw /; fi
sudo systemctl start e32
if [[ $isRW != 0 ]]; then sudo mount -o remount,ro /; fi
sleep 1
./e32ws
