#check if python3.6 is installed
if ! [ -x "$(command -v python3.6)" ]; then
  echo 'python3.6 is not installed, going to install python3.6'
  sudo add-apt-repository ppa:jonathonf/python-3.6
  sudo apt-get update
  sudo apt-get install python3.6
fi

#check if virtualenv is installed
if ! [ -x "$(command -v virtualenv)" ]; then
  echo 'virutalenv is not installed, going to install virtualenv'
  pip install virtualenv==16.0.0
fi

#Create VirtualEnv
if [ $1 ]; then
  virtualenv -p python3.6 RunEnv
fi
#activate Virutal Enviroment
source RunEnv/bin/activate

#install packages
pip install -r requirements.txt

# add directories to python path with python scripts
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src:$(pwd)/utils"
echo "########################################"
echo "#         Setup was succesfull!        #"
echo "########################################"
