#!/usr/bin 

source IPS

#--------------------Input-------------------
echo -e "File Name with:\r"
read file_name
echo -e "Please Put The Client Ip Address:\r"
echo -e "The Ip Please:\r"; read user_input 
sleep 1
echo -e "Choose DNS: [1=Server  2=Google  3=Both  4=noDNS]";read DNS
sleep 1
echo -e "Share Network With Other-Clients:\n"
echo -e "[Yes=1 \ No=2]";read allow
sleep 1
echo -e "QR-code AND File[1] \ Only File[2]: \r"
read user_wish 
sleep 1
#--------------------End---------------------

#------------- Update-Variables--------------
file_name+=".conf"
user_input+="/24"
#---------------Start-Checking---------------
echo -ne '#                     (1%)\n'
sleep 1
#Checking IPS
echo "Checking.....";sleep 1
python3 -c 'import cat;cat.cat_search()'
check_ip () {
	for ip in "${ips[@]}" 
	do 
		if [[ "$ip" == "$user_input"  ]];then
			echo "ip exist"
			echo "Try Again !!"
			echo "The Cat Found Existing IP."
			checked= return 1
			exit 0
		fi
	done
	#Checking if the ip net exist do this:
	if  [[ $checked -ne 1 ]]
      	then
		echo "Ip Accepted:"
		sleep 2
		gen #Function for generate the config.
		echo "Done generating config:"
		mv $file_name config_file
		mv "$file_name.png" qr-code
		push #Function for Pushing on Gitea.
		echo -ne '##########################(100%)\n'
		python3 -c 'import cat;cat.cat_done()'
	fi
}
echo -ne '#####                     (33%)\n'
sleep 1
#---------------End-Checking-----------------

#---------------Start-Build------------------
echo -ne '#########                 (40%)\n'
sleep 1
gen () {
#gen keys for Clinet:
wg genkey | tee privatekey | wg pubkey > publickey

touch $file_name;echo "[Interface]" >> $file_name;echo "Address = $user_input" >> $file_name
echo "PrivateKey = $(cat privatekey)" >> $file_name
echo "$user_input = privatekey= $(cat privatekey) publickey= $(cat publickey)" >> user_info
echo -ne '#############             (50%)\n'
sleep 1

if [ $DNS -eq 1 ];then
	echo "DNS = 10.10.11.1" >> $file_name
elif [ $DNS -eq 2 ];then
	echo "DNS = 8.8.8.8" >> $file_name
elif [ $DNS -eq 3 ];then
	echo "DNS = 10.10.11.1,8.8.8.8" >> $file_name
elif [ $DNS -eq 4 ];then
	:
else
	echo "Wrong Input"
	exit 1
fi

echo -ne '################          (60%)\n'
sleep 1
echo "Adding peer......";sleep 2
echo "[Peer]">>$file_name;
echo "PublicKey = iEVq4lvvKFfqjcoYYyNkA0MS8rcSGaDfPwQGN3C7+D0=">> $file_name
echo "Endpoint = 45.158.40.162:18900">> $file_name

if [ $allow -eq 1 ];then
	echo -e "AllowedIPs= 10.10.11.0/24 " >> $file_name
elif [ $allow -eq 2 ];then
	echo -e "AllowedIPs= $user_input ">> $file_name
else 
	echo "Wrong input."
	exit 1
fi

echo "PersistentKeepalive = 25" >> $file_name
echo -ne '##################        (65%)\n'
sleep 1
if [ $user_wish -eq 1 ];then
	qrencode -t PNG -o "$file_name.png" < "$file_name"
	echo "Please scan this code with wireguard-app"
elif [ $user_wish -eq 2 ];then
	echo "Your file is ready"	
else
	echo "Oops wrong input"
	exit 1
fi
echo -ne '###################       (70%)\n'
sleep 1
#---------------Done-Build------------------


#--------------Writing-New-Data-------------
sed -i '' '7i\'$'\n'' "'$user_input'" ' IPS
#--------------Done--Writing----------------

echo -ne '######################    (85%)\n'
sleep 1
#--------------cleaning-files---------------
echo "Cleaning....";sleep 1
rm privatekey publickey
echo -ne '########################  (90%)\n'
sleep 1
echo -ne '\n'

}

#---------------Pushing-to-repo-----------------
push (){
	echo -e "Start Pushing To Repo:"
	git add .
	git commit -m "add new client"
	git push
	echo -e "Done Pushing."
    echo -ne '#########################  (95%)\n'
}

#-------------Done--Pushing--------------------


#---------------Call-Functions-----------------
check_ip
#-----------------End--Call------------------
exit 0
