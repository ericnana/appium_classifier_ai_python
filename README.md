# Steps

Pre-requisites:
Install Android SDK and configure ANDROID_HOME
Install Java SDK and configure JAVA_HOME

-------------------------------------------------------------------



Environment

Ubuntu 20.04
Tensorflow=2.3.1
Tensorflow-estimator=2.3.0
Tensorflow-gpu=2.2.0
python=2.7.18
appium = 1.19.1
node = 12.14.0
npm=6.13.4
test-ai-classifies=1.0.0

Put this at the enad of your bashrc
#Nodejs
VERSION=v12.14.0
DISTRO=linux-x64
export PATH=/usr/local/lib/node-$VERSION-$DISTRO/bin:$PATH

-------------------------------------------------------------------


Appium installation steps(I did not install appium globally):

On the command line, in your home directory, create a directory for global installations: mkdir ~/.npm-global

Configure npm to use the new directory path: npm config set prefix '~/.npm-global' 

In your prefer text editor, open or create a  ~/.profile file and add this line to it: 
export PATH=~/.npm-globa/bin:$PATH

On the command line, update your system variables: source ~/.profile

To test your new configuration, install a package globally without using sudo: npm install -g jshint

Instead of steps 2-4, you can use the corresponding ENV variable (e.g. if you don't want to modify ~/.profile): NPM_CONFIG_PREFIX=/home/user/.npm-global

npm install appium
npm install wd  --> in the command line start appium
npm install appium-doctor --> in the command line start appium-doctor

Do not forget to set the path of appium in your bashrc (export NODE_PATH=~/.npm-global/lib/node_modules/appium:$PATH)

If you want to do it globally just do the following:
npm install -g appium --drivers=xuitest,uiautomator2
npm install -g wd  --> in the command line start appium
npm install -g appium-doctor --> in the command line start appium-doctor


-------------------------------------------------------------------


test-ai-classifier installation - in appium path:

go to  cd ~/.npm-global/lib/node_modules/appium
npm install test-ai-classifier@1.0.0

You might want to install this if you ever face some problems:
npm install node-pre-gyp@0.11.0
npm install --unsafe-perm --verbose node-sass
npm install node-gyp --unsafe-perm=true
npm install @tensorflow/tfjs-node@1.2.3

-------------------------------------------------------------------
In order to make sure that test-ai-classifier is installed do the following:

cd ~/.npm-global/lib/node_modules/appium
Enter node
Enter  require('test-ai-classifier');
If you get an error, it means the classifier module is not correctly installed and accessible to appium.
If not, it means everything is good, just make sure you restarted the appium server after installing it.

-------------------------------------------------------------------

Create your python class using your favorite IDE (Android Studio in my case)
Go to your command line and start appium(appium -a 127.0.0.1 -p 4723)
Check as well if appium-doctor does not show any error. Start it from where you installed it
Connect your device or start your simulator from your IDE
Go to command line and start your python script. In my case I used python3 for the shebang but working with python 2.7
