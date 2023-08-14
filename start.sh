mount | grep 'type ext4' | grep rw
isRW=$?
echo "booted in ${isRW} (rw:0, ro:1)"
if [[ $isRW != 0 ]]; then
    sudo mount -o remount,rw /
fi
echo "starting e32"
sudo systemctl start e32
echo "e32 started"
if [[ $isRW != 0 ]]; then
    sudo mount -o remount,ro /
fi

# sleep 1
echo "e32ws will start"
python3 -u e32ws
